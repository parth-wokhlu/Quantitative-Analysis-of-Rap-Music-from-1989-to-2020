import lyricsgenius
import numpy as np
import json
import config
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from collections import Counter
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import SVC

# Initialize the genius object from the lyricsgenius api
genius = lyricsgenius.Genius(config.geniusToken)

# Initialize the global count_vect and tfidf_transformer variables
# These will be used to format the song lyrics
count_vect = CountVectorizer()
tfidf_transformer = TfidfTransformer()


# This method reads the training data from the data folder and formats it using the count_vect and tfidt_transformer
# It then creates an SVC linear model and trains it with the data it formatted
# It returns the trained model
def train():
    global count_vect, tfidf_transformer
    df = pd.read_csv('data/songdatabase3.csv')

    counter = Counter(df['Topic'].tolist())
    top_2_varieties = {i[0]: idx for idx, i in enumerate(counter.most_common(2))}
    print(top_2_varieties)
    df = df[df['Topic'].map(lambda x: x in top_2_varieties)]

    description_list = df['Lyrics'].tolist()
    varietal_list = [top_2_varieties[i] for i in df['Topic'].tolist()]
    varietal_list = np.array(varietal_list)
    x_train_counts = count_vect.fit_transform(description_list)
    x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts, 15)

    clf = SVC(kernel='linear').fit(x_train_tfidf, varietal_list)
    return clf


# This removes the extra phrases (such as "[Chorus]") that are returned from the lyricsgenius api
def removeExtra(lyrics):
    for i in range(0, 10):
        try:
            a = lyrics.index("[")
            b = lyrics.index("]")
            lyrics = lyrics[0:a] + lyrics[b + 1:len(lyrics)]

        except:
            break

    temp = lyrics.split("\n")
    str = ""
    for l in temp:
        str += l + " "

    return str


# Gets the starting year and intializes the songs variable with the song names
# Intializes the variables needed to quantify the data (i.e. numTotal, numRacist, count, totalSongs)
year = input("Enter the year: ")

with open("rapData.json", "r") as file:
    songs = json.load(file).get(year)

songLyrics = []
clf = train()

numTotal = 0
numRacist = 0
totalSongs = len(songs)
count = 0


# Gets the prediction using the song lyrics and model
# returns an array this is either equal to [0] if the song has themes of racism or
# [1] if it does not
def getPredict(lyrics, clf):
    global count_vect, tfidf_transformer
    x_train_counts = count_vect.transform([lyrics])
    x_test = tfidf_transformer.transform(x_train_counts)
    return clf.predict(x_test)


# Gets predictions for all the songs through 2020
# Saves the predictions in a text file
while year != "2021":
    numTotal = 0
    numRacist = 0
    totalSongs = len(songs)
    count = 0
    for title in songs:
        try:
            song = genius.search_song(title=title, artist=songs.get(title))
            lyrics = removeExtra(song.lyrics)
            score = getPredict(lyrics, clf)
            print(score)
            if score[0] == 0:
                numRacist += 1
            numTotal += 1
        except:
            print("song missed")

        count += 1
        print("Done with " + str(count) + "/" + str(totalSongs))

    print("\n\n")
    print(numRacist / numTotal)
    file = open("trial3.txt", "a")
    file.write(year + ": " + str(numRacist / numTotal) + "\n")

    temp = int(year)
    temp += 1
    year = str(temp)
    print("Now on " + year)

    with open("rapData.json", "r") as file:
        songs = json.load(file).get(year)
