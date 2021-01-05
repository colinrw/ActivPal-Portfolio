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

<details><summary>Speed Calculation Formula</summary>

One of the features for our MET models was `speed`. This feature improved the scores of the models tremendously, but we are not 100% sure if the calculations are correctly implemented since none of our group members has a mathematical background. 

##### Recommendation

Let someone with a mathematical background implement the speed calculation correctly and see what this does to the results of the MET models.

</details>

---

<details><summary>More Detailed Cross Validation Approach</summary>

Myself applied Cross Validation on the MET models. If I had more time to work on this I would go for a more detailed approach. 

I started very late with applying Cross Validation and was therefore not able to try and analyse more possible options. 

##### Recommendation

Start applying Cross Validation and K-fold Cross Validation directly after generating the first scores instead of almost at the end of the experiments. 

</details>

---

[< Task Definition](task_definition.md) — [Conclusions >](conclusions.md) 
