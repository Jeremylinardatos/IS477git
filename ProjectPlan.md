# IS 477 Milestone 2 | Project Plan

## Overview (Naylor)
The goal of our project is to examine the relationship between weather and home runs in baseball. When the wind is blowing into the park (away from the outfield) it is harder to hit home runs, and vice versa. Temperature also affects run production; warmer temperatures allow balls to travel farther, and colder temperatures slow balls down. Our objective is to quantify this relationship and its significance. 
As a proof of concept, this project will focus on one ballpark; Wrigley Field in Chicago. We will use data from a weather station in Chicago as well as baseball data from Statcast and Baseball Reference to get information about every home run hit in Wrigley during the 2025 regular season as well as the weather (average wind speed and temperature) for the day it was hit. This is to minimize the amount of data wrangling needed; we are already planning on combining three datasets, but this project could easily be expanded to other seasons and other parks using much more data (and much more time).
Once we have the data, we plan to perform some exploratory data analysis, finding summary statistics and constructing visualizations to quantify the relationship of interest. This could also include statistical tests of significance. Ultimately, our deliverables will include graphs and charts that will determine whether or not baseball teams should be adjusting their play based on the day’s weather.

## Team (Naylor)
The team working on this project is Addison Naylor and Jeremy Linardatos. Addison’s responsibilities will include most of the programming and some of the writing, and Jeremy’s responsibilities will include some of the programming and most of the writing.

## Research Questions (Naylor)
Our ultimate research question is this; should managers, pitchers, and batters make adjustments to their play based on the day’s weather, or is its effect not significant enough to matter?

## Datasets (Naylor)

### Weather Dataset
The first dataset we will be using is a weather dataset from the National Oceanic and Atmospheric Administration. This dataset contains information about the weather in Chicago as recorded from their real-time meteorological observation network. Each observation in the table contains information about a single day in 2025’s average wind speed and direction as well as information about the temperature. While they also offer more specific datasets that record down to the minute, we could not find any data about home runs that had the same level of detail, so we decided to look only at daily averages. The dataset comes as a “.avg” file that can be downloaded here. This is a strange file format and will most likely require some manual wrangling before it can be used.

### Home Run Dataset
We downloaded our second dataset using Baseball Savant’s Statcast Search, a feature that essentially lets you filter and wrangle Statcast data through their website into the exact dataset for which you are looking. For those unfamiliar with sabermetrics, Statcast is the premier pitch-by-pitch data collector and is used by all thirty MLB teams to collect extremely detailed information about every event (usually every pitch) in a ballgame. Our specific dataset has a row for each home run hit in Wrigley Field in 2025 and contains information such as its exit velocity and launch angle. Information about the pitch itself is also provided, such as its type, release speed, and spin. This dataset can be linked to the last using the date of the home run; just match that to the weather on the given day. The data can be downloaded as a CSV file.

### Batting Dataset
Our third and final dataset was downloaded from Baseball Reference’s “Player Standard Batting” table here. Baseball Reference is another very trustworthy sabermetrics source commonly used by baseball analysts. This dataset contains a row for each batter and provides information about their stats in 2025, including BA, OBP, SLG, etc. This can be linked to the home run dataset using the player’s name. This dataset can also be downloaded as a CSV file.

Ultimately, our plan is to combine these three datasets into one, where each row represents one home run hit in Wrigley Field in 2025. Each row will contain information about the home run, the batter that hit it, the pitch thrown, and the weather in Chicago on that day. 

## Timeline (Linardatos)
3/10/2026
Description: For this part of the project, we will first decide what it is that we aim to answer through this project. Additionally, we would like to start thinking about potential applications of this research question. After deciding this we will explore sets of data that could potentially be of use for this goal.
Tasks:
  Formulate research questions and explore potential usages 
  Explore data options 
3/23/2026
Description: For this part of the project, we will be mainly focused on the actual acquisition of our selected data. We will download two of our three datasets directly via a CSV download. Our third dataset will require some wrangling before use. Lastly, we will make sure to review and terms of use or privacy policies and make sure we are staying within our bounds. We will document our process of acquisition. 
Tasks:
  Identify legal notices of datasets and understand usage limitations
  Acquire baseball data via CSV download
  Acquire wind data via NOAA website 
  Ensure data integrity 
  Document steps to acquiring data 
3/30/2026
Description: For this part of the project we will include a deep dive into each of our three datasets. For each of our datasets, we will identify any missing values, rows, duplicative data, irrelevant data, etc. We will need to identify the best and most effective way to convert our Chicago wind data into a format that will be usable and able to integrate with our other data later in this project. Lastly, as always, we will document this process to adhere to high levels of transparency and reproducibility. 
Tasks:
  Clean data by identifying any missing, repeated, or irrelevant data
  Make wind data directly usable (CSV format)
  Document data cleaning process
4/6/2026
Description: For this part of the project, we will be mainly focusing on the storage of our data. After we have cleaned our data, we want to ensure we have stored our updated dataset separately identifiable from our raw original data. This is to once again ensure reproducibility and for ease of use later on in our project timeline. We will document this storage process. 
Tasks:
  Store cleaned data 
  Document storage process 
4/13/2026
Description: For this part of the project, we will be mainly focused on integrating our three datasets. After processing our datasets, we will be looking to integrate the three together to help us make meaningful conclusions about our research question. We will need to identify how to integrate(Python/SQL) and search for elements to integrate on. We will document our integration process to ensure transparency and adequate integration between the three datasets.
Tasks:
  Integrate data from the three datasets using appropriate model
  Document integration process
4/20/2026
Description: For this part of the project we will be focused on data analysis. We will be using our processed and integrated data to make meaningful conclusions based on our research question. We will use the data to create meaningful visualizations. We will document the process of the analysis and visualization creation. 
Tasks:
  Analyze combined data to identify points of interest, trends, and useful data 
  Document analysis process
  Use select data to create meaningful visualizations
  Document visualization process 
4/27/2026
Description: For this part of the project we will be mainly focused on creating the end to end automatic workflow. This will help make our process more simple to run and recreate. We will document this process. 
Tasks:
  Create automatic workflow
  Document workflow creation process 
5/1/2026
Description: For this final step, we want to make sure our project is reproducible and we provide the information necessary to do so. This could include a codebook, metadata, etc. We want to take the necessary steps to ensure that our data and our findings are transparent and reproducible.
Tasks:
  Ensure final reproducibility 




## Constraints (Linardatos)

There are a number of potential constraints that we could face within this project. The Chicago wind data we chose is in an odd format, which may cause some issues with integration with our other two datasets; work will need to be done to make it ready to use. Additionally, our Chicago wind data may not reflect exact conditions at Wrigley Field (but they should be close enough). For our purposes, both of our baseball datasets appear to be free to use, however, we likely need accreditation to the source and we have to abide by their terms of use. Additionally, we also had to opt to use less detailed wind data due to the fact that the level of specification could not be matched by our baseball dataset, which may make our findings slightly less accurate. Outside of these, we may potentially run into other issues with integration between the different datasets, data cleaning, and more. 



## Gaps (Linardatos)

We may have potential gaps within the integration portion of this project. Our Chicago wind dataset may cause some trouble due to the format it is provided in. This may cause some extra work on our end in terms of data wrangling and management; additional input may be needed here.


