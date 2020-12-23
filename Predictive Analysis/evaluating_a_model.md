# Evaluating a model

### Introduction

As explained in [selecting a model](selecting_a_model.md), I decided to pick 2 different regression models to compare the results and select the right one for each activity. 
I used a few different methods to calculate prediction scores and eventually picked the most fitting. 

<details><summary>Cross Validation</summary>

The first comparison is made after applying K-Fold Cross Validation on the Random Forest & XGBoost model. I created a simple function that applies `5 folds` on both models and calculates the `mean` score and the `standard deviation (STD)`. These scores are compared for both model to find the most fitting for each activity.

<details><summary>Cross Validation Function</summary>

![](../Images/predictive-analysis/cross-validation-function.PNG)

</details>



</details>

---

<details><summary>Applying Test Dataset</summary>

</details>

---

[<  Training a model](training_a_model.md) — [Visualizing the outcome of a model >](visualizing_the_outcome_of_a_model.md) 