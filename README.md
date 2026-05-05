<h1>How Weather Conditions Affect Batting in Wrigley Field</h1>

<h2>Contributors: Jeremy Linardatos & Addison Naylor</h2>


<h2>Project Summary:</h2> 
Our project mixes the world’s most famous sports and weather data to conclude what type of impact weather conditions have on the sport and if so, what steps should be taken to adjust for this. For this project, our chosen sport is America’s pastime: baseball. Baseball has a long history of intricate data analysis. From exit velocities on home runs to on base percentages, everything in baseball is tracked at a microscopic level. Being that both of us are born and raised in Illinois, we share a favorite team of the Chicago Cubs. When you think of Chicago, you think of the Cubs, but you also think of the ‘Windy City.’ It’s no secret that weather can have an impact on sports performance. From a windy and cold day, to a hot and dry day, performance can drastically change. For example, when wind is blowing out of the park and when the temperature is warmer, the ball tends to travel further, whereas the opposite has a negative effect on ball flight. Because of this discrepancy, for this project we decided to integrate these two areas to see what impact weather has on performance. 

Our definitive research question is:  Should managers, pitchers, and batters make adjustments to their play style based on the day’s weather, or is its effect not significant enough to matter?


As proof of concept, we have focused on our state’s largest city and also home to our favorite team of the Cubs: Chicago. Using data tracking home runs in the Cubs home field, Wrigley Field in the last season, player batting data, and Chicago wind data, we aim to quantify the relationship between weather and batting. 

For this project, we found three datasets to integrate. Our first dataset was collected using Baseball Savant’s Statcast Search feature. We used this search feature to select data pertaining to each home run hit in Wrigley Field during last year’s regular season. The data included critical information, such as the player who hit the home run, pitch type, exit velocity, hit distance, and more. Our second dataset was found through Baseball Reference, using their ‘Player Standard Batting’ table. Baseball Reference is extremely trustworthy and is commonly used by analysts. Whereas our last dataset was more focused on the home run rather than the player who hit it, this dataset focuses more on a specific player. Each row contains information regarding a single player’s batting stats, including on base and slugging percentages. Our last dataset holds data for Chicago weather conditions. This data comes from the National Oceanic and Atmospheric Administration and contains real-time observational data from their site in Lake Michigan 2.75 miles offshore. The dataset includes information regarding wind speed, temperature, and direction. NOAA actually provides very specific data that is updated by the minute, but for purposes of clean integration, we selected the dataset with daily averages. 

After loading in our datasets, we performed various cleaning tasks to prepare for integration. This included searching for missing or outlying values, filtering down to only necessary columns, properly separating rows, and more. After cleaning our data, we prepared to integrate our datasets, which included a bit more work to ensure proper merging between attributes that were semantically the same. Ultimately, we merged the datasets on attributes, such as player names and date. 

With a completely merged dataset, we now began to run some analysis. We created graphs to show the visual impact of wind direction and temperature on hit distance. Ultimately, our graphs showed little correlation between these, showing little to no impact on hit distance. To confirm this, we also created a heat map. Our largest correction came between wind speed and hit distance, but still at a measly 0.24. So, ultimately we conclude that there is not a substantial enough impact from wind in Wrigley Field to warrant players or managers making adjustments to their play style. 

<h2>Data Profile:</h2>

<h3>Dataset #1 | Home Run Data:</h3>

Our home run dataset comes from Baseball Savant’s Statcast Search feature. Statcast is the premier pitch-by-pitch data collector and is used by all thirty MLB teams to collect extremely detailed information about every event (usually every pitch) in a ballgame. Knowing this, we feel that we can trust the data’s accuracy. This feature essentially allows us to select the specific data we are looking for, in our case, home runs in Wrigley Field during the regular season last year. 

When using this feature, we are presented with data in an interactive tabular format that we can explore further, such as links to video clips of the actual home run, pitch placement, and more. For our purposes, we have filtered down to these attributes to be shown on the websites search feature: 

* Rk → Arbitrary index number 
* <mark>Player → Player name (home run hitter)</mark>
* Team → Team the player is on (home run hitter)
* Result → Result of the play (these are all home run as we filtered it this way)
* <mark>Game Date → Date the game was played on</mark>
* Vs. → Team the player was playing against 
* Pitch (MPH) → Pitch speed 
* Spin Rate (RPM) → Rotations per minute of pitch 
* <mark>Pitch Type → Type of pitch thrown</mark>
* <mark>EV (MPH) → Exit velocity of hit</mark>
* <mark>LA (°) → Launch angle of hit</mark>
* <mark>Dist (ft) → Distance of hit</mark>
* <mark>full_name → This was a variable we created in the dataset after cleaning</mark> 

While selecting certain features to be shown on the website will shorten the amount of attributes shown on its interface, when downloading this data as a CSV file, all the attributes will be present. Due to this, we had to filter down to the attributes we deemed important for this project after importing (those included in our analysis are highlighted above). 

Each row within this dataset represents a singular home run. The attributes mainly focus on the actual hit itself, but basic identifying data is included, such as name and date, which is also important for integration later in the project. 

Additionally, we had to consider certain legal and ethical restraints with regard to our acquisition of this data. While there is no official license provided, because of our usage of the data for educational purposes (along with other factors such as our limited use of the data, no monetization, etc.) we are more than likely within our bounds to use the data in the capacity needed for this project. No API key was provided, so instead of directly downloading as  CSV we used a python library called pybaseball. This package allows us to scrape data straight from Baseball Savant and gives us Statcast data. Using this will also help us in terms of verifying integrity through SHA-256 check sums.

The raw home run data set can be found within our repository in the data folder under the name home_runs.csv. As mentioned before, despite selecting specific attributes within the Statcast feature, when importing the raw data, all attributes will be present, if you do a direct CSV download. An explanation of each attribute within the raw data can be found here.

Lastly, while there is not a lot of information directly on the website regarding metadata and provenance, because of the proximity Statcast works with the MLB, we don’t have too many concerns in this respect. They do provide a link to the process data collection goes through if it is not directly observed/measured within the game. 

<h3>Dataset #2 | Player Specific Batting Data:</h3>

Our player specific batting data comes from Baseball Reference. Data on the site is provided by Sportsradar, which is the official stats partner of the MLB, so once again we feel confident in the accuracy of the data. Much like the home run dataset, the batting dataset is provided in a tabular format on their website and is already presorted by player for last season. 

The dataset includes every player that took an at bat last season. Each row in the dataset represents an individual player. With this, in each row either an aggregate or average of that player’s stats is provided. For example, something like home runs for the season would be totaled, but on the other hand on base percentage is averaged. Having attributes such as the player name will allow us to integrate this dataset with our other data later on in our project. 

While once again in our project we filter down to only the relevant attributes we need to complete our analysis, the raw data has a number of attributes. A link to the glossary is provided here. The attributes we eventually use in our filtered dataset for analysis include:

* Player → Name of the player
* OBP → On base percentage
* SLG → Slug percentage 

The acquisition process for this dataset is similar to that of the last. Although once again we are able to directly download our data using a function on the website, we are opting to use the pybaseball package to reflect the best reproduction process. Baseball reference does not provide an API as most of the data on their site is sold by third parties to them and APIs are not part of their business model. In addition, we are making sure to stay within the proper bounds to ensure that we don’t violate any guidelines. 

Lastly, in terms of metadata, some more work could be done on their end. For complex and uncommon stat calculations, there are some links provided to explain how they are calculated. While explicit information on how data is collected is not provided, as with sports data its quite straightforward and observational, information on where the data comes from and contributors is provided to create more transparency. 

The raw data can be found within our repository under the data folder called batting.csv. 


<h3>Dataset #3 | Wind Data</h3>

This last piece of data is the strangest of the bunch, especially in terms of formatting. Our wind data comes from the National Oceanic and Atmospheric Administration, so it really doesn’t get any more officially verifiable than that. The data is collected at a site 2.75 miles offshore from the City of Chicago in Lake Michigan. 

The file format is a bit strange in that it comes in as a .avg file, which is really a genuine supported file type; it’s called that more so because it is a file with a list of averages. Each row in this dataset represents the average data for a singular day in 2025. 

This dataset does not have many attributes and therefore does not have an extensive glossary. There is a bit of information within the actual file itself that explains each attribute.

* WS=Wind Speed (m/s)
* WD=Wind Dir (deg)
* AT=Air Temp (C)

Extensive information regarding metadata is provided in a separate section on the NOAA Great Lakes Environmental Research Laboratory website. This includes information regarding the site itself (site elevation, air temperature height, etc.), equipment (sensors, processors, etc.), and collection procedures. 

In terms of acquisition, this is once again a direct download to CSV. There is no API or webscrapping ability here. We are not concerned with issues regarding reproducibility as this data is static due to it being observational and from last year, meaning it’s no longer being updated. With regards to usage, the guidelines are a bit looser for this data. Our weather data comes from NOAA, a federal agency. Generally speaking, unless stated otherwise, data in this case will be free to use and have no real restrictions under a Creative Commons CC0 or CC BY 4.0 license. However, we do want to provide a citation according to NOAA’s guidelines and make sure we are not claiming the data is our own, claim we are endorsed by NOAA, alter the data and present it as governmental material, etc.

Our wind data can be found in the data folder under weather.avg, which is a text file that we will later properly convert to a usable CSV to be joined on date with the other datasets. 


<h2>Data Quality:</h2>
Overall, we feel quite pleased with our data quality across the three datasets. 

Our home run dataset is of extremely high quality. Looking at Baseball Savant’s embedded search feature, which we used to find our data, there is a luxury of very detailed data available to use. We feel confident in the data’s accuracy as it comes straight from MLB Advanced Media, so there is no real ‘middle man’ between the data collection and compiling. Additionally, this data is collected using the Statcast system. This system uses highly advanced cameras and radars to collect data across each of the MLB’s 30 stadiums. While extensive metadata or provenance data is not provided, because of the close proximity to the MLB itself we feel that it is accurate. We do believe, however, that more work could be done in this respect. There is a little blurb about how some data might be calculated based on available technology and how tracking was done. Additionally, a dictionary is provided and a video to a tutorial on how to use the search feature. Beyond this, there is not much information provided on the data. We would like to see more information provided, but with sports data we also understand that much of it is observed observationally. Further, we were actually pleased with the data with respect to the data quality pillars. The data was accurate as it was collected using the latest available technology. However, we do have some concerns with inconsistencies in terms of attributes. For example, both launch speed and exit velocity semantically represent the same thing, however, under Baseball Savant’s search feature it is represented under EV (MPH), while under the imported CSV file it is under launch_speed. The completeness of the data is also in good standing; none of the attributes used for this project were found to be incomplete. Seeing as this data is from last year and unlikely to be updated, unless new formulas are implemented, we have no concerns with timeliness. Additionally, consistency seems to be upheld as there are not any clear schema or semantic violations other than the previously mentioned issues of inconsistency in column naming between the actual site and imported CSV file (also apparent with launch angle and hit distance columns).  

Our batting dataset is also of extreme high quality. Once again, as the data is provided from an official stat partner of the MLB, we feel its accuracy is pristine. It is a highly regarded source and used by many in the industry. Baseball Reference also provides an extensive dictionary that explains both statistics and terms. Details regarding the collection and sources of data are also provided on a separate page for transparency. We are fairly pleased with the accuracy of the data. While we believe that the data itself is accurate, we do have some concerns regarding syntax. Specifically, within the player name attribute, there are some concerns with extra characters included (these characters carry meaning within the website interface, but not within the actual dataset). In terms of completeness, this dataset includes every player that took an at bat during last year’s regular season, so we aren’t concerned with this. However, we did identify some missing values. These missing values were mainly for summary attributes on base percentage or slugging percentage, meaning they are likely missing because the player in question did not meet the requirements for an average to be calculated, so this is not an immediate concern. In terms of timeliness and consistency, everything seems to be solidly in order. Once again this is a dataset from last year, so it is completely updated. Additionally, no semantic or schema rules seem to be violated. 

Lastly, we look at our wind dataset quality. If there is a dataset that we have the least concerns with in terms of trustworthiness, it’s this one. There is a plethora of information provided by NOAA and the Great Lakes Environmental Research Laboratory regarding recording and collection processes, so believe this data to be accurate. Now, in terms of formatting, this data presents the largest concern. The data is provided in an .avg file, which is not a real file type, but rather reflective of the fact that the data is a collection of daily averages. Information is provided regarding attributes, albeit limited, but it is useful in the quality of data. Some overall summary statistics are also provided, but they are not relevant for our work, and further, they will present a problem later in terms of our cleaning. We also have some concerns regarding the recording of the data. While we believe the data to be entirely accurate, as extensive information is provided regarding the collection process, we do notice that there are days that have a strange amount of records used to calculate a daily average. There doesn’t seem to be an explanation nor an obvious pattern for this inconsistency. Lastly, consistency and timeliness. We’ve already discussed some potential consistency issues with the number of observations used to record daily averages, but outside of this no rules are violated and no issues present themselves. Timeliness is not a concern, this data was promptly updated, and once again is from last year, so we don't have real concerns with it changing. The data for daily averages was calculated (for most days) using an aggregate average of observations recorded every two minutes. However, one last inconsistency we found after manually going through old data, is that there is some rollover. Data for 2 minute averages (which is ultimately what is used to calculate daily averages) begins recording at 11:52 P.M. the day prior to recording and ends at 11:50 P.M. on the day of recording. For example, if the observed day is May 1, 2026, data for that day will begin recording at 11:52 PM April 30 and end recording at 11:50 PM May 1. This is a bit odd as we are including data from a previous day in our overall daily recording, but in the grand scheme of things, and considering this is a consistent recording process, this isn’t a huge concern, just something to be aware of. 

<h2>Data Cleaning:</h2>

As expected, all of our datasets had to go through some type of cleaning in order to make it fit for use and ready to integrate with each of the other datasets. 

<h3>Home run dataset (Baseball Savant Statcast):</h3> Prior to even doing any cleaning work, we needed to use pybaseball to import our data properly and verify integrity using SHA-256. Within our larger imported dataset, we filtered down to just home runs hit in Wrigley Field. We also had to reconfigure the column representing player names to format it in a merge friendly way. This dataset included extensive information about home runs hit in Wigley Field during the 2025 regular season. 118 attributes were provided for each home run hit, however, for our analysis we filtered down to only 6 attributes:

* game_date 
* player_name 
* launch_speed 
* launch_angle 
* hit_distance_sc 
* pitch_type 

After filtering down our dataset, we explored missing values and data types. We did not identify any missing values and confirmed that each attribute was in its correct data type; no explicit or implicit missing values were found. This dataset was now ready to go.


<h3>Batting dataset (Baseball Reference Player Standard Batting Table):</h3> As with the prior dataset, instead of directly downloading as a CSV from the website’s feature, we used pybaseball to scrape the data and then verified integrity. We then filtered down to only 3 attributes that were necessary for this analysis.

* Name
* OBP 
* SLG

After filtering, we once again searched for missing values and looked at data types. We did identify a number of missing values, however, these are presumably for those players who do not have enough at bats to warrant calculating batting average statistics. If these are an issue, they will present themselves later in the integration process and we will address it there. After looking at data types, we confirmed that all data types are accurate for the attributes, confirming there are no issues there. 

<h3>Wind dataset (NOAA Great Lakes Environmental Research Laboratory data):</h3> This data came in a bit of an odder format, so its process of importation looked slightly different from the others. We read in the data as a CSV file, however, we had to skip the first 11 rows as they included summary statistics (max wind speeds, etc.) that were irrelevant to our project and would’ve called issues with integration. Additionally, in order to correctly format the data, we had to use a regex pattern to separate. After successfully importing the data, we were left with these attributes:

* DOY → Day of year 
* WS → Wind speed 
* WD → Wind direction 
* AT → Air temperature 
* n → Number of observations 

We opted to drop the n column, as it just contains how many observations were observed in one day, which is not very relevant to our project and would create unnecessary noise in the data. 

After dropping this column, we searched for missing values and looked at data types. We did find one missing value for each attribute that could be attributed to the fact there was an extra place holder observation for leap years of which 2025 is not. Looking at the data types, everything seems to align and match what we would expect. We also verified integrity using SHA256 once again. To prepare for integration, we had to do some further cleaning. We converted our DOY column to a usable date column using datetime. Additionally, we did the same with our home run data game_date column. After formatting the dates properly in both datasets, we were able to properly integrate. 


<h3>Cleaning with Merging:<h3></h3> Prior to merging our first two datasets together (home runs and batting), we need to do just a bit more cleaning. For the batting dataset, we had to strip the player column to lowercase for merging purposes. Additionally, during the merge process, we dropped unnecessary or duplicate columns (Ex: No need for two columns representing names). To confirm successful integration we searched for missing values and found none. 

<h2>Findings:</h2>
 Ultimately the goal was to identify if there was a significant relationship between wind and batting, quantify this relationship, and suggest if players and managers should adjust their playstyle. 

After properly integrating our datasets, we created a set of visualizations to show the relationship between our weather and baseball data. We created two graphs, to identify the relationship between air temperature and wind direction with hit distance. Ultimately, both of these visuals provided inconclusive evidence to quantify wind having a significant effect on the actual play. 

To confirm the idea that wind does not have a significant effect, we created a correlation heat map to get numerical confirmation of this. Our heatmap returned with largely the same results. There seemed to be little correlation between wind speed, wind direction, and air temperature, with launch speed, launch angle, and hit distance. Our largest correlation came in at a measly 0.24 between wind speed and hit distance. So, perhaps wind speed has a minor impact on the distance balls are hit, but other than this we can not definitively conclude that there is a significant relationship here. Because of this, we can’t truly recommend managers and players make any changes to their style of play. If we see little to no impact on the game, it’s hard to say that anything need be done to combat it.


<h2>Future Work:</h2>

There’s a lot to be gleaned from this project and going forward. First and foremost, we learned a lot about the process that goes into creating a pristine pipeline, from data acquisition to visualization. In lower level courses or simpler projects, most of the work is done on the analysis side, and not much emphasis is given to the actual curation, reproduction, and management of the data. Through each step, we learned the elevated importance of constantly documenting our steps. In the professional world, if someone were to want to reproduce our work to better understand it or build off of it, it is critical that not only outline the steps that we took within our actual analysis, but also that of the prework, such as acquisition, cleaning, and more. 

Without a doubt one the more specific practices that we learned throughout this process came within the acquisition and verification areas. In past projects, we have just opted to download data directly as a CSV file and never thought twice. However, as we have progressed in this course and project, we have realized how detrimental that can be for reproducibility. We learned how to properly acquire data through various methods. In our case for this project, it included scrapping data in a proper manner using a specialized python package. This is far closer to what you would expect to see in industry rather than a direct CSV download. Additionally, we learned the importance of verifying our data, especially for those who are attempting to recreate the process. Using SHA256, we verified that the imported data matches what we expect. Once again, this not only helped on our end, ensuring we imported properly, but it also helps those who attempt to go through our work in ensuring nothing has been corrupted or misread on their end. This is a crucial step of the data management process that we had not been aware of before. 

Lastly, one other key piece that we learned about was creating a proper workflow to automate our steps properly. We are previously used to just doing all of our work in one large Jupyter notebook, however, through this course, we have learned the importance of making the data pipeline more clean to ensure transparency and reproducibility. Because of this, we created individual scripts for steps, such as acquisition, merging, visualization, etc. We also created a Snakemake file that continues to help automate our workflow using those python scripts as outputs. This was a process we had not learned about in previous courses, but now recognize how critical of a role it plays not only in reproducibility, but also the organization of our project as a whole. 

There is also a lot to build off of here. Our analysis did not reveal any significant relationships between batting and wind. Although, intuitively we may still believe that there is still some type of impact here, maybe it can’t be seen with the data we used. Instead, in the future, we may opt to instead analyze the end result of plays. For example, through analysis we may come to the conclusion that there are more fly outs in windier weather, so batters should try to drive balls low rather than going for home runs. We could also look at more specific analysis with the direction of wind. Based on where the wind is blowing, should a batter aim a certain direction for maximum chances of hitting a homerun or landing on base? There really is a lot of analysis that can be done in multiple facets. For our purposes, we didn’t find a significant relationship between wind in the general area and batting, but perhaps a different research question or different dataset would yield different results. 



<h2>Challenges:</h2>

There were a number of challenges throughout this entire process. The largest challenges fell in the earlier stages of the project. Data acquisition proved to be a bit more difficult than expected. In past projects, we would’ve likely just directly downloaded our data as CSV files and went on with analysis. However, knowing what we’ve learned from this course, we opted to go a different route, one that would be better for transparency and reproducibility. We had to grow through a lot of documentation within a python package, pybaseball, that is specifically designed for baseball data. Using this package, we were able to properly retrieve data from our desired sources. After doing this we did still have to go through some data cleaning steps that were complex in some ways. Further, we had some challenges with verifying this data was correct. Meaning, we had to figure out how to use SHA256 to ensure that we properly imported our data. This concept was a bit new to us, so it took a second to wrap our heads around and write code to properly assert this within our scripts. 

One particular dataset also gave us a bit of a challenge. Our weather (wind) dataset came in a very odd format: a .avg file. This itself is not a real file type and is instead just representative of the data presented itself. In reality, the data was provided in a text file. So, when faced with this odd file presentation, we were a bit troubled on how to handle it. Ultimately, we found a way to import the data to a CSV file properly, emitting some rows and using regex to split accurately. The data wrangling process, even though this did not require an extra python package or API key, proved to be challenging with multiple cleaning steps needed. In particular, changing a column that tracked the day of the year (how many days into the year the data was observed on, ex: observed on Jan 15, DOY = 15) into a format that would allow us to integrate with the other datasets required some challenging syntax work with the datetime library. Ultimately, we were able to make it work, and this improved our ability to work with challenging data. 

We also ran into challenges outside of the acquisition process and weather dataset. The cleaning for our two baseball datasets proved to be a bit challenging. One of the more challenging parts was formatting player names. The imported format identifying players would not have worked for data integration. Using an embedded function within pybaseball, some syntax and combination work, and merging (within the same data) allowed us to reach that compatible formatting, but it did prove to cause some challengers early on in our project, especially looking ahead knowing we’d need to integrate with a dataset that had player names in a different format. 

Lastly, one of the biggest challenges was upholding constant documentation. We were not used to having to be clear and transparent about everything throughout the entire project. At times it was difficult to consistently outline everything we had been doing in detail in a presentable well. This also goes along with automating our workflow. This was another challenge we had to do accurately for purposes of transparency. However, using Snakemake we were able to document this well and had it function properly. In general, however, the entire documentation and automation part of the project was something that we had to keep conscious effort of and did not come naturally at first.

<h2>Reproducing:</h2>

In order to fully recreate our data analysis and obtain the same results we did, follow these steps exactly:

1. Clone our github repository onto your local machine. It contains all of our scripts, the raw weather data, and the Snakefile that ties it all together. If you would rather acquire the weather data yourself, it can be found at [this link](https://www.glerl.noaa.gov/metdata/chi/archive/chi2025.04t.avg). It will be checked against the dataset we used for this analysis using checksums.
2. Install the required packages using Python’s typical package installation techniques (and install Python itself if you don’t have it). These might change over time, so for reproducibility’s sake, look into how to do this at [this link](https://packaging.python.org/en/latest/tutorials/installing-packages/) if you don’t know how (or just look it up) The packages required for our scripts are
* pandas v3.0.2
* matplotlib v3.10.8
* seaborn v0.13.2
* pybaseball v2.2.6
* hashlib (but this one is a base Python library, so you don't need to install it separately)
3. Install Snakemake 9.20.0 using instructions found at [this link](https://snakemake.readthedocs.io/en/stable/getting_started/installation.html) (if this link doesn’t work, you can just search something like “Snakemake installation instructions”). This is required so that you can run our Snakefile, which automatically runs all of the scripts in the correct order.
4. Open your favorite IDE’s terminal, navigate to the root directory of our cloned repository, and run the command “snakemake --cores n” where n is the number of cores you would like to use on the process. This is not a resource-intensive workflow, so one or two should be fine.
5. Check output for hash mismatch errors, which indicate that either something about pybaseball has changed since this analysis, or something about the weather data you downloaded has changed (this is only if you downloaded the weather data yourself).
6. Assuming no errors came up, you should have a figures folder containing the exact output visualizations we used for our analysis.

<h2>References:</h2>

Köster, J. et al. (2024). Snakemake (Version 9.20.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.593048

LeDoux, J., & Schorr, M. (2026). pybaseball (Version 2.2.6) [Source code]. https://github.com/jldbc/pybaseball

Matplotlib Development Team. (2025). Matplotlib (Version 3.10.8) [Source code]. https://github.com/matplotlib/matplotlib

McKinney, W. (2010). Data structures for statistical computing in Python. In S. van der Walt & J. Millman (Eds.), Proceedings of the 9th Python in Science Conference (pp. 55–56). https://doi.org/10.25080/Majora-92bf1922-00a

MLB Advanced Media, LP. (2025). MLB Statcast search. Baseball Savant. https://baseballsavant.com

NOAA Great Lakes Environmental Research Laboratory. (2025). Chicago met data archive. https://glerl.noaa.gov/metdata/chi/archive/chi2025.04t.avg

NumPy Developers. (2025). NumPy (Version 2.4.2) [Source code]. https://github.com/numpy/numpy

Python Software Foundation. (2023). Python (Version 3.12.0) [Computer software]. https://www.python.org/

Sports Reference LLC. (2025). 2025 Major League Baseball standard batting. Baseball-Reference.com. https://www.baseball-reference.com/leagues/majors/2025-standard-batting.shtml#all_players_standard_batting

The pandas development team. (2026). pandas-dev/pandas: Pandas (v3.0.2). Zenodo. https://doi.org/10.5281/zenodo.19340003

Waskom, M. L. (2024). Seaborn (Version 0.13.2) [Source code]. https://github.com/mwaskom/seaborn
