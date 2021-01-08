# Conclusions

In this conclusion chapter I will go over the results and conclude my perspective on the final results. 

<details><summary>MET Prediction Models</summary>

My conclusion after analyzing the MET regression models ([results can be found here](../Predictive%20Analysis/evaluating_a_model.md)) is that all Random Forest and XGBoost models seem to overfit. The models gave decent results before applying the test data set, but once the test data set was applied to results worsened. Generalizing during the training of the model was not done accurately due to not having enough respondents in the data set. 

To get back to answering the research question. It *is* possible to predict the intensity, but the predictions are not very reliable since the models are not giving accurate predictions.   

</details>

---

<details><summary>Activity Recognition Models</summary>

*Note: this model has been done by my colleague Adnan Akbas*
*Graphs created by Adnan Akbas were used in this section*

After analysing the results from the Activity Recognition model from Adnan, we can conclude that most of the activities are predictable with high accuracy, recall and precision after applying K-fold Cross Validation.

*Data from Activity Recognition model from Adnan Akbas*

| |K-fold Cross Validation Score|
|------------|---------|
|Accuracy|0.82 (+/- 0.04)|
|Recall|0.84 (+/- 0.04)|
|Precision|0.82 (+/- 0.04)|

Looking at the Confusion Matrix, not all the activities were predictable with high accuracy. The `Cycling Light` and `Cycling Heavy` activity results were a bit worse compared to the other results. Since the movement of cycling is always the same, no matter if it's light or heavy, it is hard for the model to make accurate predictions for these activities. 

*Confusion Matrix from Adnan Akbas*

![](../Images/Research%20Project/activity-recognition-confusion-matrix.PNG)


</details>

---

<details><summary>Calculating If Respondents Did Their 150 Minutes of Moderate Intense Activities</summary>

</details>

---

[< Evaluation](evaluation.md) — [Planning >](planning.md) 