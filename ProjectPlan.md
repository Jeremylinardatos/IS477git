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
