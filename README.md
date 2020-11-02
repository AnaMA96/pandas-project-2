# SHARKS PROJECT 
![](https://dl16txa2az7pk.cloudfront.net/cms/fileadmin/_processed_/9/8/csm_hai-2507375_960_720_529ee2de69.jpg)

In this project I use the [Shark Attack](https://www.kaggle.com/teajay/global-shark-attacks) downloaded from the Kaggle API.

My goal is to get to know if my hypothesis is correct or not: 
**Is surfing in USA the most dangerous activity? Are the attacks usually provoked? Is the white shark the most aggressive species?**


When I printed the columns to see what data the file contained, the first conclusion I came to was that most of the attacks occurred in the USA, and that the activity that was most frequently attacked was "surfing". After this conclusion I deduced that most of the attacks would be "unprovoked" since people who surf tend to be respectful of the marine environment, a question that I try to affirm or refute through the analysis of the data.

## Data cleaning

In this project I treat the data and clean it to be able to work as accurately as possible. I have had remove null values, duplicates, or regroup data that belong to the same category but that originally we could not group because they were called (erroneously) differently.

After creating a new dataframe with the necessary columns and rows to work on my hypothesis and clean them up as I mentioned in the previous paragraph, I have collected the data obtained in graphics to make the conclusions more visually attractive and made the **storytelling.ipynb** where you can see all the conclusions.

## Technology stack

·The dataset has been downloaded from the Kaggle API.
·The cleaning has been done mostly with Pandas.\
·The visualization has been done with Matplotlib, Wordcloud and Plotly.

To get the data necessary to plot the Bubble map I've used the [OpenCageGeocoding API](https://opencagedata.com/api).
