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



</details>

[<  Data Cleaning](data_cleaning.md) — [Data Explanation >](data_explanation.md)