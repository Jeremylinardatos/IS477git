<h1>Complete Data Dictionary</h1>

<h2>Dataset 1 | Home Run Data</h2>

* **`game_date`**

    * This is the date that the home run was hit. We can merge our weather dataset to this one using this key.

* **`player_name`**

    * This is the name of the player that hit the home run. We can merge our batting stats dataset to this one using this key, after some wrangling to make sure the name formats match up.

* **`launch_speed`**

    * This is the speed the ball was traveling the moment it left the bat, measured in MPH. It is also frequently referred to as exit velocity.

* **`launch_angle`**

    * This is the angle the ball was moviing the moment it left the bat, as measured in degrees up from the ground.

* **`hit_distance_sc`**

    * This is the horizontal distance in feet that the home run travels before hitting the some "ground". Since we are only dealing with home runs in Wrigley Field, we know this means it hit the seats. Other stadiums require more or less hit distance for a home run to make it.

* **`pitch_type`**

    * This is the type of pitch that was hit. Information about what each abbrevation means can be found [here](https://library.fangraphs.com/pitch-type-abbreviations-classifications/).

<h2>Dataset 2 | Batting Data</h2>

* **`Player`**

    * This is the player whose stats fill out the row. We can merge our home run dataset to this one using this key. You might notice some players have symbols at the end of their names. These represent whether they're a left-handed, right-handed, or switch hitter, but we won't be using this in our analysis.

* **`OBP`**

    * On-Base Percentage measures how often a player is able to get on base.

* **`SLG`**

    * Slugging percentage measures a player's general "slugging" ability, which is how often they are able to hit hard balls. Where something like batting average weighs every hit equally, slugging percentage gives more weight to big hits like home runs. To put it simply, players that have a high SLG are better at hitting home runs, and better at hitting them hard.

These two statistics combined measure each player's general skill with as few variables as possible.

<h2>Dataset 3 | Weather Data</h2>

* **`DOY`**

    * Day of Year; this represents the day of 2025 the data is for. After some formatting, we can use this column to merge our weather dataset with our home run data.

* **`WS`**

    * Wind speed in meters per second.

* **`WD`**

    * The direction from which the wind is blowing; wind blowing north to south would be zero degrees, south to north would be 180.

* **`AT`**

    * Average temperature in degrees Celsius.
