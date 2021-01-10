# Data Preparation

This chapter is mainly about the data preparation for the MET regression models. The preparation has partly been done by Ali Safdari and me.

<details><summary>Convert to Numerical for Machine Learning</summary>

Machine Learning models can't work with non-integer values, therefore we need to convert these values to  integer values. Here are a few examples of respondent characteristics that were converted to numerical values. 

|Description|Function|
|------|------|
|Convert `ja/nee` string to number| ![](../Images/Data%20Preprocessing/convert_string_to_number.PNG) |
|Convert `age` to categorical number| ![](../Images/Data%20Preprocessing/convert_age_category.PNG) |

The remaining functions can be found at the top of [this](../Images/Data%20Preprocessing/Code/creating_main_dataframe.py) notebook. 

</details>

---

<details><summary>Feature Creation</summary>

To have a useful data set for the MET regression model we needed to create a data set with all the possible features. At first Ali and I created a simple data set with the following features:

|Feature|Function|
|---|------|
|Sum of Magnitude of Acceleration (calculate from X, Y and Z - by ?)| ![](../Images/Data%20Preprocessing/sum_mag_function.PNG) |
|MET value (calculated from vo2 + weight in kg) - by ?| ![](../Images/Data%20Preprocessing/MET_function.PNG) |
|Body Mass Index (BMI; calculate from weight and height) - by Ali and Me| ![](../Images/Data%20Preprocessing/BMI_function.PNG) |

All mathematical functions can be found in [this](../Images/Data%20Preprocessing/Code/math_helper.py) notebook. 

</details>

---

<details><summary>Putting it all together</summary>

Eventually this was the final function that actually created the data set that was used for the MET regression models. The function took all the created features in the notebook and added it together. 

![](../Images/Data%20Preprocessing/adding_together_function.PNG)

The entire MET regression data preparation can be found in [this](../Images/Data%20Preprocessing/Code/creating_main_dataframe.py) notebook (same as the above mentioned notebook). 


</details>

---

[<  Data Cleaning](data_cleaning.md) — [Data Explanation >](data_explanation.md)