# Quantitative Analysis of Rap from 1989 to 2020

by Parth Wokhlu and Mihir Nakra 

# I. Introduction

After spending the past year delving into every era of rap music, the intricacies of the genre and its change became extremely intriguing to us. We were interested in quantifying how rap music has evolved over the past 30 years, specifically in regards to its origin, and how that evolution correlates to African-American culture. Specifically, an article, titled "How Polticial Hip-hop Has Evolved Over Time" by Dan Runcie, explains that the style of music was created as a way to express the oppression experienced by underrepresented African-Americans. Since then, there's been a wide consesnsus that the themes of systemic racism, police brutality, and generational poverty have fallen out of rap music, so we decided to use deep learning to find a correlation between changes in the content of hip hop and racial injustices.


# II. Methodology

All the code for this project is open sourced (not all of it is written completely by us, so please give the original authors their due credit).

## Data Collection
The first step was collecting the names of all the popular rap songs of the past 30 years. Because Billboard had not started a "Hot 100" List for Rap in its earlier eras, we began by taking songs from the weekly charts that have been updated since March of 1989. We used [Allen Guo’s Python API](https://github.com/guoguo12/billboard-charts) for retrieving the song and artist names and saved them to a json file, sorting them by the year that they were on the charts. The full list of the yearly top rap songs can be found in the file named “rapData.json”. 
After that testing data was compiled, we then had to go through the most gruesome process: collecting training data. Using Google and our own playlists, we came up with 75 songs stretching across every era that were good examples of rap music that discussed systemic inequalities. Then, we repeated the same process for 75 songs that discussed any content besides anti-black oppression. The full list of training data can be found in the “master song database.csv” file. We switched around the training data for different trials in order to make sure there was consistency within the results. 

## Neural Network

## Implementing the Code
Now that we had an accurate model and the required testing and training data, the rest of the code was pretty simple. The syntax for the class can be found under the title of “mainSVC.py”. After training the model on the given data, it was time to run it through the rap lyrics of the past 30 years. We did this by utilizing [John Miller’s Genius API](https://github.com/johnwmillr/LyricsGenius), which is a website that stores the lyrics of nearly every song we needed. 

From there, the process was standard. We created a for loop to stop when the year the AI was analyzing was equal to 2021 and established a new count of songs the computer deemed as about racism, and the total number of songs. At the end of processing the songs for the respective year, the computer returned the percentage of songs it thought discussed racism, and we put it into our data. This cycle repeated until we had quantified the content of rap song for every year of every era (see more details about results in the next section). 

## Limitations/Flaws

# III. Results


# IV. Conclusion and Implications 


