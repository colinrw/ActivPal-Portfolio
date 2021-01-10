# Data Exploration

#### Introduction

The data provided by CBS was a lot. Therefore we decided to start by filtering out the data that was labelled with an activity. Each respondent had a corresponding file with the `start` and `stop` time they performed certain activities in the lab.

<details><summary>Here is an example of how this was provided to us</summary>

|Activity|Start|Stop|
|------------|---------|--------|
|springen|2019-09-16 14:29:20|2019-09-16 14:30:18|
traplopen|2019-09-16 14:31:18|2019-09-16 14:32:04|
fietsen licht|2019-09-16 14:41:29|2019-09-16 14:46:29|
fietsen zwaar|2019-09-16 14:46:29|2019-09-16 14:51:29|
lopen|2019-09-16 15:12:00|2019-09-16 15:17:00|
rennen|2019-09-16 15:17:00|2019-09-16 15:22:00|
zitten|2019-09-16 15:31:00|2019-09-16 15:36:00|
staan|2019-09-16 15:45:00|2019-09-16 15:50:00|

With these timestamps it was possible to filter out all the activity data from all respondents and put them all in a new CSV file. This has been done with the following code. 

![](../Images/Data%20Preprocessing/combine_activity_data.PNG)

The entire notebook can be found [here](../Images/Data%20Preprocessing/Code/combine_correspondent_activities.py).

</details>

---

<details><summary>Activity Distribution </summary>

Once the activities were combined I created a distribution with all respondent activities. The results are shown below.

The entire notebook can be found [here](../Images/Data%20Preprocessing/Code/Activity%20Distribution.py).

![](../Images/Data%20Preprocessing/activity-distribution.png)

We can see that `springen` and `traplopen` have very little data points. After some analysing we found out that these activities were only performed for 1 minute instead of 5 for the other activities. This 1 minute of data was not enough for further modelling, we decided to leave `springen` and `traplopen` out of it in consultation with CBS. 

</details>

---

[<  Go Back](../README.md) — [Data Cleaning >](data_cleaning.md) 