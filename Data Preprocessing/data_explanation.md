# Data Explanation

The data that will be explained is coming from the previous [data preparation](data_preparation.md) chapter. Most of these `column names` are features that are used for the MET regression models. 

The following table is an example of 1 row of data that is used for the MET regression models. Every row is resampled to 1 minute (60 seconds) since MET is calculated in minutes.

|Column name|DataType|Example|Explanation|
|------|------|------|------|
|pal_time|timestamp|2019-10-10 15:36:00|Since we need to predict the MET value, and MET is calculated in 60 seconds, the `pal_time` column name is the time the MET value is calculated on.  
|respondent_code|string|BMR004|The unique number that corresponds to a respondent.
|activity|string|lopen|The performed activity from that minute.
|mean_met|double|1.2920676857268667|The mean MET value from the measured minute. 
|sum_mag_acc|double|1116.7722891103585|The summation of the X, Y and Z values to the power of 2 within the measured minute.
|mean_speed|double|23533.170460441113|The mean speed within the measured minute. 
|weight_kg|double|75.7|The weight of the respondent in kilograms.
|length_cm|double|166.79999999999998|The length of the respondent in centimeters.
|bmi|double|27.20844906808366|The Body Mass Index, which is calculated with the weight and length of the respondent.
|is_sporter|boolean|1.0 (true)|If the respondent is a sporter or not. 
|age_category|boolean|4.0|The age category from the respondent. `4.0` means the age of the respondent is between 40-44.
|meets_balance_guidelines|boolean|0.0 (false)|The balance of the respondent was measured during the lab sessions. The respondent adheres to the balance guidelines or he/she does not.
|estimated_level|boolean|0.0 (false)|CBS looked at the characteristics of the respondents and decided based on these if the respondent adheres to the estimated level from their perspective. 
|walking_speed_km|double|5.0|The speed in kilometers the walking activity was performed in the lab.
|running_speed_km|double|10.0|The speed in kilometers the running activity was performed in the lab.
|gender|boolean|1.0 (true)|The gender of the respondent. Male or Female.
|meets_activity_guidelines|boolean|0.0 (false)|During the lab sessions characteristics and the daily activities from the respondents were noted and concluded if the respondent adheres to the activity guidelines or not. 

[<  Data Preparation](data_preparation.md) — [Data Visualization >](data_visualization.md)