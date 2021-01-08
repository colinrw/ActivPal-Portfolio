# Evaluation

During this project it was not possible to execute all experiments. Different causes were, not enough knowledge, time or data. This chapter contains different subjects for future research. 

---

<details><summary>Too Little Data</summary>

To make predictions for the MET regression models it is necessary to have enough data so the model could generalize. This was not the case. From the 40 respondents, only 25 were useful for our experiments. The results of this was that our MET predictions models were *overfitting*, which resulted in inaccurate results for the calculation of the 150 minutes moderate intense physical activity.  

##### Recommendation

For future research on this topic I recommend more data. One of the main reasons why we were not able to answer the main research question with more certainty was because of too little data for our experiments. 

</details>

---

<details><summary>Removing Low Variance Features</summary>

While creating the features for the MET prediction models we picked the most logical features from the `respondenten.csv` file (this file contains different characteristics of all participating respondents) that was provided by CBS, but the most logical is not always the most optimal.

##### Recommendation

My recommendation for the MET models is to remove low variance Features. The cause of the overfitting MET models could be having low variance features. The models could improve (or worsen) once the low variance features are removed from the models.  

</details>

---

<details><summary>A More In Depth Hyperparameter Tuning Approach</summary>

During the implementation of both regression models I briefly researched the implementation and use of Hyperparameters. I applied a set of parameters from different websites, but going deeper and finding my own set of parameters would probably improve the models. 

##### Recommendation 

More in depth research on parameters that are not predefined from different websites. 


</details>

---

[< Task Definition](task_definition.md) — [Conclusions >](conclusions.md) 
