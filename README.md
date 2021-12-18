# Quantitative Analysis of Rap Music from 1989 to 2020

by Parth Wokhlu and Mihir Nakra 

Parth Wokhlu: parth.wokhlu.843@gmail.com

Mihir Nakra: nakramihir@gmail.com

# I. Introduction/Purpose

After spending the past year delving into every era of rap music, the intricacies of the genre and its change became extremely intriguing to us. We were interested in quantifying how rap music has evolved over the past 30 years, specifically in regards to its origin, and how that evolution correlates to trends in black culture. Specifically, an article, titled ["How Polticial Hip-hop Has Evolved Over Time"](https://trapital.co/2019/08/28/how-political-hip-hop-has-evolved-over-time/) by Dan Runcie, explains that the style of music had become a way to express the effects of oppression experienced by black people. Since then, there's been a wide consensus that the themes of systemic racism, police brutality, and generational poverty have fallen out of rap music, so we decided to use machine learning to see the truth of these claims.

Note: As non-black people we're aware that we're guests in the culture of hip-hop, and in no means are trying to push a certain narrative on non-conscious music (we absolutely love trap artists like Playboi Carti and Future). This was simply a project done out of interest in a genre of music that we love. If we've used any ignorant phrases or remarks, please don't hesitate to email us and we'll take care of it immediately. 

# II. Methodology

All the code for this project is open sourced (not all of it is written completely by us, so please give the original authors their due credit). 

## Data Collection
The first step was collecting the names of all the popular rap songs of the past 30 years. Because Billboard had not started a "Hot 100" List for Rap in its earlier eras, we began by taking songs from the weekly charts that have been updated since March of 1989. We used [Allen Guo’s Python API](https://github.com/guoguo12/billboard-charts) for retrieving the song and artist names and saved them to a json file, sorting them by the year that they were on the charts. The full list of the yearly top rap songs can be found in the file named “rapData.json”. 

After that testing data was compiled, we then had to go through the most gruesome process: collecting training data. Using Google and our own playlists, we came up with 75 songs stretching across every era that were good examples of rap music that discussed systemic inequalities. Then, we repeated the same process for 75 songs that discussed any content besides anti-black oppression. The full list of training data can be found in the “master song database.csv” file. We switched around the training data for different trials in order to make sure there was consistency within the results. 

## Neural Network
At first, the idea of a neural network seemed interesting, but we didn’t know anything about artificial intelligence or machine learning.. As we delved into the topic, we found numerous [YouTube videos](https://www.youtube.com/watch?v=aircAruvnKk&feature=youtu.be) and [articles](https://news.codecademy.com/taylor-swift-lyrics-machine-learning/) that allowed us to wrap our heads around these concepts. 

After researching, we decided to classify songs based on their lyrics by utilizing a linear support vector machine. A linear support vector machine mathematically determines a hyperplane and classifies data points accordingly. A hyperplane is, put simply, a line of best fit that acts as a decision boundary to segregate and classify the data on the two sides of it. The calculations are done by the machine to create a hyperplane with the largest margin possible between the two sections so that data can be classified as accurately as possible.

![hyperplane example](https://randlow.github.io/images/ml/svm_hyperplane.png)

Then came the hard part; how do we turn words into data points for the machine to use? We decided to use a count vectorizer, which creates a matrix of numerical data using the words given to it. An example of this is below:

![Example of count vectorizer matrix](https://kavita-ganesan.com/wp-content/uploads/how-hashingvectorizer-works.png)

After receiving the count vectorizer’s matrix, we used a tfidf transformer to allow the machine to get a better understanding of what words matter in terms of classifying a song’s subject matter. A tfidf transformer highlights the words that are unique to certain songs and helps reduce the influence of words like “the,” which appears in all songs numerous times regardless of their subject matter. After applying these calculations to our text, we fed the training data to the model and allowed it to determine the hyperplane. All of this was done with the Python Sklearn library.

To determine the accuracy of our newly trained model, we ran simulations utilizing our training data and found out that it had an average accuracy of 85%.

After determining that our model was fairly accurate, we could use it to classify the content of the list of songs we had compiled. To predict if a song had themes of racial injustice or systemic racism in it, we could give that model the count vectorized and tfidf transformed song lyric, and it would identify where the song lyrics would lie on the graph in relation to the predetermined hyperplane (effectively classifying it as a politically charged song or not).

The credit for providing us with the design of this model goes to [Shanglun Wang](https://www.toptal.com/machine-learning/nlp-tutorial-text-classification), who made another linear support vector machine to classify wine reviews. He was kind enough to open source the code and explain it thoroughly, which allowed us to understand it and adapt it to our needs.


## Implementing the Code
Once we had an accurate model as well as the required testing and training data, the rest of the code was pretty simple. The syntax for the class can be found under the title “mainSVC.py”. After training the model on the given data, it was time to run it through the rap lyrics of the past 30 years.  We did this by utilizing [John Miller’s Genius API](https://github.com/johnwmillr/LyricsGenius), which is a website that stores the lyrics of nearly every song we needed. 

We created a for loop to cycle through Billboard’s Top 100 Rap Songs chart for every week from 1989 to 2020 and established a count of songs the computer deemed as about racism and the total number of songs (while accounting for repetitions). With these numbers, the code returned the percentage of rap songs about racism each year. This cycle repeated until we had quantified the content of rap songs for the past 30 years (more detail in the results category).

## Limitations/Flaws
The first limitation of this study is the most obvious. We’re two high schoolers that conducted this “experiment” during winter break, there’s a relatively moderate margin of error (8%, to be exact).

Second, this project isn’t reflective of every rap song ever created, only the most popular, as we pulled the songs from the Billboard charts. Hypothetically, there could be the same amount of songs about systemic racism being created, but people are simply listening to songs about other topics more. This distinction is especially key when realizing that during the early 2000s, hip-hop audiences grew massively to non-black people with artists like Ms. Lauryn Hill and Eminem.

Third, institutional racism is a system that influences every aspect of the lives of the people who it affects. For example, a song about drug dealing is still directly linked to policies like the War on Drugs and redlining, but our AI won't pick up that correlation. Every expression of black success and culture is inherently political in a state built on white supremacy and tearing black people down.

# III. Results
<p align="center">
  <img src="https://github.com/fatlips222/Quantiative-Analysis-of-Rap-Music-from-1989-to-2020/blob/main/Results/Evolution%20of%20Rap%20(Graph%201).png">
</p>
<p align="center">
  <img src="https://github.com/fatlips222/Quantiative-Analysis-of-Rap-Music-from-1989-to-2020/blob/main/Results/Evolution%20of%20Rap%20(Avg.%20Trendline%2C%20Graph%202).png">
</p>

Although the numbers aren’t perfectly consistent, they all tell a very similar story. In the early ’90s, the themes of systemic racism occupied around 35% of rap music, and now, these explicitly politically driven songs only consist of about 10% of rap music, dropping even lower in the years before. To see our data in its raw format, check out the open-sourced Excel file titled “Rap Analysis Results.”

Some notable events that correspond with the peaks and dips in the graph consist of Nas’s *Illmatic* in 1994, the deaths of Tupac Shakur and Biggie Smalls in 1996 and 1997 respectively, *The Miseducation of Lauryn Hill*’s Album of the Year award in 1998, Eminem’s Hollywood debut in 2002, Kanye West’s *808s & Heartbreak* in 2008, and the critically acclaimed *To Pimp a Butterfly by Kendrick Lamar* in 2015.

# IV. Conclusion and Implications 
Utilizing a natural language processing neural network model, we conclude that the explicit themes of systemic racial inequality in hip-hop music have become increasingly insignificant over the past 30 years. This is consistent with how black culture as a whole has evolved, with improved social standings and decreasing unemployment levels for African Americans. Although the unemployment rate has decreased overall, spikes in unemployment coincide with an increase in the popularity of songs concerning racial inequality. For example, the unemployment spike in the early 1990s and 2010s correlates with a spike in the popularity of songs about racial injustice.
 
<p align="center">
  <img src="https://i.imgur.com/p7XZQTa.png">
</p>

This doesn’t ignore the fact that systemic racism is still very much alive and is the reason why African-Americans are disproportionately incarcerated to this day. Although songs about racism are not as popular, it doesn't necessarily mean that there are fewer of these songs. Considering that the rap industry has grown tremendously over the past years, it is extremely likely that there are even more of these types of songs. The issue is that big record labels who have the resources to brand and market an artist dismiss songs dealing with racial injustice in exchange for music that would resonate with fans of all races. Rolling Stone wrote a [great article](https://www.rollingstone.com/music/music-features/music-industry-racism-1010001/) about how record labels have influenced rap music to make it more "appealing", essentially gentrifying it. We encourage fellow non-black fans of hip-hop to listen to more of those heavy songs that describe the feelings non-black folk will never experience (“Sing About Me, I’m Dying of Thirst” by Kendrick Lamar is a personal favorite of ours).

<p align="center">
  <img src="https://www.pewresearch.org/wp-content/uploads/2014/07/incarceration1.jpg">
</p>

Greg Whitt and Keith Reid-Cleveland wrote an excellent [article](https://uproxx.com/music/hip-hop-social-justice-intersection/) about how hip-hop and its stars have consistently been a key projector of anti-racist activism, spawning anthems to rally around and placing the oppression felt by African-Americans into the mainstream. Rap has been revolutionary in the past, and we hope it can revolutionize the future as well.








