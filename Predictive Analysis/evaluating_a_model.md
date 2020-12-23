# Evaluating a model

### Introduction

As explained in [selecting a model](selecting_a_model.md), I decided to pick 2 different regression models to compare the results and select the right one for each activity. 
I used a few different methods to calculate prediction scores and eventually picked the most fitting. 

<details><summary>Cross Validation</summary>

The first method is calculated after applying K-Fold Cross Validation on the Random Forest & XGBoost model. I created a simple function that applies `5 folds` on both models and calculates the `mean` score and the `standard deviation (STD)`. These scores are compared for both model to find the most fitting for each activity.

<details><summary>Cross Validation Function</summary>

![](../Images/predictive-analysis/cross-validation-function.PNG)

</details>

</details>

---

<details><summary>Applying Test Dataset</summary>

Once the Cross Validation had decent results we decided to apply the separated test dataset on our model to validate the results. 
The test dataset that was separated contained 3 test users with each containing 5 rows of data for each activity. I created a function to apply the test users on the already trained model to see if our model would over/under fit or give good results on new data.

<details><summary>Applying Test Dataset Function</summary>

![](../Images/predictive-analysis/test-set-results.PNG)

</details> 

</details>

---

<details><summary>Evaluation Results</summary>

Picking a fitting model for each activity was the final step once Cross Validation and the Test Dataset were applied. I created a table that displays the:
- `R Squared score after Cross Validation`
- `R^2  score after applying the test data set` 
- `Mean Squared Error (MSE) score after applying the test data set` 

Activity|Random Forest|Random Forest Test|XGBoost|XGBoost Test|
        |R Squared Score|Cross Validation|	R^2	|MSE	|R Squared Score| Cross Validation	|R^2	|MSE
        
Walking	0.40 (+/- 0.15)	0.40	0.65	0.32 (+/- 0.12)	0.29	0.70
Running	0.60 (+/- 0.20)	0.58	1.57	0.63 (+/- 0.15)	0.45	1.80
Cycling Light	0.41 (+/- 0.28)	-0.70	1.78	0.41 (+/- 0.23)	-1.03	1.95
Cycling Heavy	-0.39 (+/- 1.18)	0.02	1.67	0.12 (+/- 0.59)	-0.08	1.23
Standing	-0.54 (+/- 0.55)	-0.02	0.38	-0.85 (+/- 0.78)	0.36	0.30
Sitting	-0.23 (+/- 0.41)	-0.05	0.37	-0.17 (+/- 0.42)	-0.24	0.40


</details>

---

[<  Training a model](training_a_model.md) — [Visualizing the outcome of a model >](visualizing_the_outcome_of_a_model.md) 