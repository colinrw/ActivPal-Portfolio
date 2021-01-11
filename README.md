# ActivPal Portfolio - Data Science Minor 
By: Colin Werkhoven 

Studentnumber: 17079578

Project group
- Adnan Akbas — [portfolio](https://github.com/klict/activepal-portfolio)
- Ali Safdari — 
- Matthew Turkenberg — 
- Mark Boon — 

# Introduction

Add general introduction about the project.

# Datacamp Courses
Progress in DataCamp can be found [here](Images/datacamp-progress-colin-werkhoven.PNG).

# Reflection and Evaluation

<details><summary>Reflection on own contribution to the project</summary>

##### Situation

##### Task

##### Actions

##### Result

##### Reflection

</details>

---

<details><summary>Reflection on own learning objectives</summary>

##### Situation

This Applied Data Science minor was a very new subject, so my overall knowledge of the subject was minimum. I had some experience with Python programming, but very little. This would mean a lot of new excited things to be learnt!

##### Task

My main focus was aimed on the technical part of the project. This would mean, data preparation, data pre-processing and configuring models. There were times I had to do literature research, but minimum. 

##### Actions

Once we received the data I wanted to immediately start with exploring the data, but literature study had to be done first. After this part was over I did a lot of data exploration and pre-processing for the models. 

After a few weeks of working with the data I thought that I was missing out on the creation of a model. I decided to switch my focus on researching different models and how to pre-process, configure, train and evaluate a model. 

##### Result

Following the Datacamp courses and applying this knowledge in practice improved my Python programming skills a lot! I learned about different Library's which I will use for further projects. 

I've learned a lot about Machine Learning models. I was always fascinated about this technique and never knew how a computer could learn. After this minor I have a very good understanding about the creation of a Machine Learning model. Mainly about Regression models, since this is what I've been working on most of the time during this project.

##### Reflection

The first few weeks of this project was mainly focused on literature research. This was in my opinion the least pleasant part, but if I look back, one of the most important parts to make good progress. I should've focused a bit more on this in the beginning of the project. This would speed up the understanding of the problem domain and Machine Learning models. 

During this minor I learned a lot. The most exciting part is being able to create, configure and understand different Machine Learning models. Besides this, I learned to work with raw data and turn this to useful information. I am able to evaluate and visualize my results. 

If I look back at what I learnt throughout this minor I am happy with my choices. The only thing I wanted to learn more about is different Machine Learning models that were not used in our project and the implication of Neural Networks.   

</details>

---

<details><summary>Evaluation on the group project as a whole</summary>

##### Situation

##### Task

##### Actions

##### Result

##### Reflection

</details>

---

# Research project

<details><summary>Task definition </summary>

This project is a collaboration between The Hague University of Applied Sciences (THUAS) and Centraal Bureau voor de Statistiek (CBS). 

<details><summary>Introduction</summary>

Statistic Netherlands wants to know if it's possible to measure if respondents meet the proposed 150 minutes of moderate intense physical activities within a week. The current method of collecting information from respondents is asking questions with different surveys. This comes with issues, one of them is that respondents don't always know the exact answers and this results in inaccurate results. Therefore, CBS decided to invite 40 random respondents to participate in this experiment. Every respondent received an activPAL device and had it mounted on their upper thigh. This activPAL device measured different types of data which has to be used to answer the following research questions. 

</details>

<details><summary>Research Questions</summary>

*These research questions were created by my colleagues, so I am not taking any credits for them.*

This research contains *3* different research questions. All with different sub-questions. The first 2 questions are necessary to answer before answering the final question.

### Question 1

How can Machine Learning be used to predict the intensity of activities performed in a lab situation by a person, who is being monitored with Vyntus One device and wearing an activPAL accelerometer? 

##### Sub Questions
- What measurement does activPAL use for intensity and why?  
- Is it possible to extract this intensity measurement values from just Vyntus One data, if so, how?  

### Question 2

How can Machine Learning be used to predict the intensity of activities performed by a person wearing only the activPAL accelerometer, based on the data gathered from the Vyntus One device and the ActivPal accelerometer in the lab situation? 

##### Sub Question
- What machine learning model can best be used to measure the intensity for each activity?  

### Question 3

How can Machine Learning be used to determine whether people did their 150 minutes of moderate activity in the activPAL accelerometer data of an entire week? 

##### Sub Question
- How can Machine Learning be used to recognize the activities, performed in the lab situation, in the activPAL accelerometer data?  

</details>

---

</details>

<details><summary>Evaluation</summary>

During this project it was not possible to execute all experiments. Different causes were, not enough knowledge, time or data. This chapter contains different subjects for future research. 

---

<details><summary>Too Little Data</summary>

To make predictions for the MET regression models it is necessary to have enough data so the model could generalize. This was not the case. From the 40 respondents, only 25 were useful for our experiments. The results of this was that our MET predictions models were *overfitting*, which resulted in inaccurate results for the calculation of the 150 minutes moderate intense physical activity.  

##### Recommendation

For future research on this topic I recommend more respondents with different characteristics. One of the main reasons why we were not able to answer the main research question with more certainty was because of too little respondent data for our experiments. 

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

</details>

<details><summary>Conclusions</summary>

In this conclusion chapter I will go over the results and conclude my perspective on the final results. 

<details><summary>MET Prediction Models</summary>

My conclusion after analyzing the MET regression models ([results can be found here](Predictive%20Analysis/evaluating_a_model.md)) is that all Random Forest and XGBoost models seem to overfit. The models gave decent results before applying the test data set, but once the test data set was applied to results worsened. Generalizing during the training of the model was not done accurately due to not having enough respondents in the data set. 

To get back to answering the research question. It *is* possible to predict the intensity, but the predictions are not very reliable since the models are not giving accurate predictions.   

</details>

---

<details><summary>Activity Recognition Models</summary>

*Note: this model has been done by my colleague Adnan Akbas*

*Graphs created by Adnan Akbas were used in this section*

After analysing the results from the Activity Recognition model from Adnan, we can conclude that after applying K-fold Cross Validation most of the activities are predictable with high accuracy, recall and precision.

*Data from Activity Recognition model from Adnan Akbas*

| |K-fold Cross Validation Score|
|------------|---------|
|Accuracy|0.82 (+/- 0.04)|
|Recall|0.84 (+/- 0.04)|
|Precision|0.82 (+/- 0.04)|

Looking at the Confusion Matrix, not all the activities were predictable with high accuracy. The `Cycling Light` and `Cycling Heavy` activity results were a bit worse compared to the other results. Since the movement of cycling is always the same, no matter if it's light or heavy, it is hard for the model to make accurate predictions for these activities. 

*Confusion Matrix from Adnan Akbas*

![](Images/Research%20Project/activity-recognition-confusion-matrix.PNG)


</details>

---

<details><summary>Calculating If Respondents Did Their 150 Minutes of Moderate Intense Activities</summary>

This section concludes the results of the Main Research Question:

*How can Machine Learning be used to determine whether people did their 150 minutes of moderate activity in the activPAL accelerometer data of an entire week?*

The previous conclusions were needed to answer the Main Research Question. With combining the results of the MET prediction models and Activity Recognition models it is possible to calculate if a respondent has done their 150 minutes of moderate intense activities within a week.

Since the results of the MET prediction models are not very reliable, the 150 minutes calculation is also not very reliable. Concluding that the 150 minutes are possible to calculate with the use of Machine Learning, but the trustworthiness is not very high. The Main Research Question could not be answered accurately.   


</details>

---

</details>

<details><summary>Planning</summary>

In this planning chapter I will discuss how we made use of the Scrum Methodology, how our first plannings came to realization and our overall used techniques. 

*Note: the following sections were written by me and are taken from the Research Plan ([find entire research plan here](../Images/Research%20Project/Research%20plan%20-%20Final.pdf))* 

---

<details><summary>Procedure</summary>

For the activPAL project management we have been using the Agile (scrum) method. To follow the scrum method, there will be daily stand-ups. Within our project the daily stand-up time is 9:30 and since day 1, we have been following this method every day. Within the daily stand-up we discuss the progress of the prior day and the plans for today.  

</details>

---

<details><summary>Solving issues </summary>

Besides this, we discuss the issues that you’ve might encountered during your previous working day. If you are stuck or not sure what you should be doing next, we make sure to clear that up and make new working pairs. Usually when this happens there will be Teams calls after the stand-up to discuss or solve this problem with each other. This way the stand-ups won’t take longer than they should be.  

</details>

---

<details><summary>Sprint planning </summary>

Before holding our retrospective, we make sure to create a planning for the next sprint. During every sprint planning we, as a team, look at the current sprint on Jira. We discuss if we managed to complete the set sprint goal, if all the tasks are done, and what still must be done with the leftover tasks to complete them. The leftover tasks will be added to the new sprint. 

Once the current sprint has been completed, we start the new sprint by specifying a goal for the new sprint. We usually look at the roadmap and what we have done the previous sprint to create a new goal. After agreeing as a team with the set goal, we have healthy discussions where everyone gets the chance to add new tickets to our backlog that will help achieve this goal.  

</details>

---

<details><summary>Creation of the first sprint backlog </summary>

The creation of our first sprint backlog was a bit hectic. The project was new for all of us and nobody knew where to start or what the exact planning was going to be. We still managed to create a backlog for the first sprint which was mainly focussed on research.  

Annemieke from CBS provided us with lots of useful papers to research. A task during the first sprint was filtering out useful papers, this way we did not waste time by rereading unusable papers. As a team we all picked different subjects which we thought would be beneficial for our project and created 1 ticket with small subtasks in it. Besides the different papers we also received different CSV files which contained the data we had to work with during the project. We created a ticket to research these CSV files and document as much as possible.  

</details>

---

<details><summary>Retrospectives</summary>

After finishing a 2-week sprint we hold a retrospective to reflect and evaluate the process we’ve made over the past weeks. In these retrospectives we discuss what went well, what didn’t go well, what each team member longed for and the actions we’re going to take for the next sprint. During the retrospective we look back at the actions we wrote down from the previous sprint and see if we have worked on these actions. These retrospectives are a good tool to let every member on the team freely speak on how to feel about certain aspects over the last 2 weeks.  

</details>

---

<details><summary>Project roles </summary>

At the start of the project, we agreed on switching roles every sprint. This would mean a new scrum master, communicator and note taker every sprint. This did not go as planned, we decided to keep the same scrum master for the entire project to make sure the project went smoothly. The communicator role was switched halfway through the project and note taker role was done by the whole team. Every member wrote down what was important for them and after every important meeting we discussed the previous meeting to make sure everyone is on the same level.  

##### *Extra addition*

My role during the first 10 weeks of the project was the communicator. All communication between teachers and project owners was usually done by me. After these 10 weeks I took over the note taker role and wrote down all the information what could be useful for our project.

</details>

---

<details><summary>Planning tool </summary>

The infrastructure/tool we have been using for this is Jira. Jira is a plan, track and manage software that is mostly used for software development. Within the activPAL project Jira is not only used for software development but also for the research development from week 1.  

</details>

---

<details><summary>Research questions </summary>

The main research questions have been divided into smaller tasks called research sub tasks. Every sub research question has a few tasks that help to answer the question and guide us to the right approach to give an answer. By combining Jira with our sub questions, we can put all the sub questions into the Jira Road Map. This gives the whole group a good overview of the questions that still need to be answered and the tasks needed to answer the sub questions.

</details>

---

</details>

# Predictive Analytics

<details><summary>Selecting a Model</summary>

### Introduction
To answer one of the research questions within our project we had to create a model to predict the Metabolic Equivalent of Task (MET) value of given activities. These activities differentiate between `Running`, `Walking`, `Standing`, `Sitting`, `Cycling Light` and `Cycling Heavy`.

Solving this issue would require a regression model since we need to predict an `integer/double` value(MET) and don't need classification in this case. 

### Approach
My approach for solving this problem was looking at different regression models. I started with finding different models and noting their pros and cons and eventually comparing them to pick atleast 2 possible models. I decided to pick 2 possible models and implement them with the same configurations instead of 1 to prevent getting biased results. 

### Different Regression Models
I researched different regression models to find a possible candidate model to answer our question.

##### Random Forest ([source](https://medium.com/swlh/random-forest-and-its-implementation-71824ced454f))
The Random Forest model is a decision tree model which can both be used for Regression and Classification. Besides being a possible regression model, the Random Forest model makes use of `Ensembled Learning`. Ensembled learning means combining multiple results to 1 final result, this method would give more accurate results and minimize getting biased results.

Random Forest is a possible model for our issue since it can be used for regression and the Random Forest decision tree method tries different trees to find the optimal results. 

##### Ridge Regression ([source (1)](https://www.statisticshowto.com/ridge-regression/#:~:text=Ridge%20regression%20is%20a%20way,(correlations%20between%20predictor%20variables)), [source (2)](https://www.quora.com/What-are-the-benefits-of-using-ridge-regression-over-ordinary-linear-regression))
Another Model I've looked into was the Ridge Regression Model. The Ridge Model minimizes the square error of the model, but this Model is based on `Multicollinearity`. This means one value can be predicted with another value. These 2 values have a correlation between each other.  

With the current issue of predicting the MET value with the X, Y and Z data it should not be possible to predict the next value based on the previous value. Therefor the Ridge Regression is not a suitable candidate for our MET recognition model.   

##### K-nearest Neighbour ([source](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761))
Just like the Random Forest Model, the K-nearest Neighbour(KNN) model is also used for Regression and Classification issues. The KNN model is a `supervised machine learning` algorithm, this means the model needs labeled data to produce results. If we look at the `Vyntus (labdata)` we have the `Ground Truth` that needs to be predicted, but this is not the case for `activpal (weekdata)`. This would mean we would only be able to predict on the `labdata` and not the `weekdata`. 

The K-nearest Neighbour model would not be useful to solve our issue, mainly because we don't have the ground truth available all the time. Since K-nearest Neighbour is a supervised machine learning algorithm, apply this on our data would not be sufficient.    

##### XGBoost ([source](https://towardsdatascience.com/https-medium-com-vishalmorde-xgboost-algorithm-long-she-may-rein-edd9f99be63d))
The XGBoost Model is the final regression model I've looked into. This model is very similar to the previously mentioned Random Forest model. Just like Random Forest, XGBoost is an ensembled decision tree algorithm. Besides using ensembled learning, XGBoost makes use of `Gradient Boosting`. This means minimizing errors while trying to find the best possible results. 

XGBoost is a possible model to solve our MET prediction issue. This model uses ensembled learning and Gradient Boosting to prevent low variance and biased results. 

### Final Decision
After analysing the models named above we found 2 candidate models. Firstly the `Random Forest Model` and secondly the `XGBoost Model`. 

The `Ridge Regression Model` is not suitable since it makes use of Multicollinearity. This method would not work on our data since we make predictions based on `X, Y, Z` data. 

The `K-nearest Neighbour Model` would be suitable if we only needed to predict the `labdata` since these MET values could be calculated based on the activity. But in our case we need to predict `labdata` and `weekdata`. The weekdata is unlabelled and therefor not suitable since the KNN model makes use of labelled data.

The final decision will be comparing the `Random Forest Model` with the `XGBoost Model`. Both models make use of decision trees which delivers low variance and less biased results. Finally, to pick a model for our MET predictions, we will be configure both models as identical as possible. More on this can be found in the next chapter.


</details>

<details><summary>Configuring a Model</summary>

### Introduction

In the previous chapter we've picked 2 possible Regression models, Random Forest and XGBoost. I will discuss the configurations for both models here. Both models have almost the same configurations, I will therefor explain the configurations once. Here you can find a list of configurations that were applied by the configuration of both models. 

---

<details> <summary>Random State</summary>
Picking a `random state` is essential for the configurations of your models. Without a `random_state`, the model will always apply a random, new variation of decision trees. To get accurate predictions and results it is important to always have the same decision trees. 

We decided to use `random_state=0` for all our MET prediction models. This way all models would have consistency in the configurations and results could not get manipulated by trying out different random state values. The decision for `random_state=0` is found [here](https://scikit-learn.org/stable/glossary.html#term-random-state). 

</details>

---

<details> <summary>Feature Selection</summary>

After [preparing the MET prediction model dataframe](Data%20Preprocessing/data_preparation.md) with different features I thought it would take a long time to try all possible variations. Therefor, I wanted to use Recursive Feature Selection [(RFE)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html). 
RFE picks a combination with the best scoring features. The chosen features were used in the configuration of the Random Forest or XGBoost model. This automated approach would save us lots of time, since we needed to find features for 6 different activities and 2 different models.   

<details><summary>List of features for Feature Selection</summary>

![](Images/predictive-analysis/list_of_features.PNG)

</details>

<details><summary>Feature Selection Function</summary>

![](Images/predictive-analysis/feature_selection_function.PNG)
</details>

<details><summary>Example results of Feature Selection</summary>

![](Images/predictive-analysis/feature_selection_results.PNG)
</details>

</details>

---

<details> <summary>Picking the best number of trees</summary>

The `n_estimators` parameter is an important configuration for all tree based models. Every number of tree results in a different outcome. I wanted to find the best number of trees, but doing this by hand was gonna take way too long. Therefor I decided to write a function that finds the optimal number of trees between a certain range. 
In our case we picked a range between 1-210. After analyzing the plots, the results were not getting higher with a larger number of trees around 200. 

<details><summary>Finding optimal number of trees function</summary>

The result from this function was used during the configuration of the models for the `n_estimators` parameter.

![](Images/predictive-analysis/n_estimator_function.PNG)

</details>

<details><summary>Profound Explanation of optimal number of trees Approach</summary>

To find the most optimal amount I created a function called `optimal_amount_estimators`. 
This function contains a for loop that creates a new model every loop, trains this model and calculates a R Squared score. All these scores are added to a Dictionary. I picked a dictionary since we need an integer value which will be the optimal estimator. The key from this dictionary will be the optimal estimator. Once the dictionary is filled we simply pick the `max` value from the dictionary and return the associated key value from the max R Squared score. 

Here is an example of how this dictionary looks like. In this case Key 18 gives the highest R Squared score. Therefor we return the key that is associated to the highest score and use this as our `n_estimator`.

![](Images/predictive-analysis/dictionary-example.PNG)

</details>

<details><summary>Results of the optimal number of trees function</summary>

More on the visualisation of this plot can be found in the [visualizing the outcome of a model chapter](Predictive%20Analysis/visualizing_the_outcome_of_a_model.md).

![](Images/predictive-analysis/n_estimators_results_plot.PNG)

</details>

</details>

---

<details> <summary>Hyperparameter Tuning</summary>

Once the optimal amount of features and number of trees were selected it was time to improve the models even more. My colleague Adnan Akbas pointed me towards `Hyperparameter Tuning`.

## What is Hyperparameter Tuning?

Hyperparameter tuning is finding the best combination of parameters for your Machine Learning model. 

Since the Random Forest and XGBoost models have different configurations, I searched which parameters were usually tuned for each model. 

## Hypertuning the Random Forest model 

[Random Forest Hyperparameter Tuning Source](https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74)

<details><summary>Here is a list of parameters and possible values that were tuned for the Random Forest model</summary>

These parameters were applied with all possible combinations on a new `RandomForestRegressor` model. 

![](Images/predictive-analysis/hyperparametertuning_randomforest.PNG)

</details>

<details><summary>Applying the parameters on a new model</summary>

The parameters were applied on a new model with the following function. The function returns a new `RandomForestRegressor` model with the newly found parameters after hyperparameter tuning.

![The function](Images/predictive-analysis/apply_randomforest_hyperparametertuning.PNG)

</details>

## Hypertuning the XGBoost model 

[XGBoost Hyperparameter Tuning Source](https://towardsdatascience.com/doing-xgboost-hyper-parameter-tuning-the-smart-way-part-1-of-2-f6d255a45dde)

<details><summary>Here is a list of parameters and possible values that were tuned for the XGBoost model</summary>

These parameters were applied with all possible combinations on a new `XGBRegressor` model. 

![](Images/predictive-analysis/hyperparametertuning_xgboost.PNG)

</details>

#### GridSearch vs. RandomizedSearch

These parameters were applied on a `XGBRegressor` in combination with `GridSearchCV` and `RandomizedSearchCV`. I decided to try 2 different search methods to see which one performed better. 

<details><summary>GridSearch Function</summary>

![](Images/predictive-analysis/xgboost_gridsearch_function.PNG)

</details>

<details><summary>RandomizedSearch Function</summary>

![](Images/predictive-analysis/xgboost_randomizedsearch_function.PNG)

</details>

The results of the different Search methods were compared to each other to find the best performing method for the XGBoost model. The results of both methods can be found in the [Evaluating a model](evaluating_a_model.md) chapter.

</details>

---

</details>

<details><summary>Training model</summary>

### Introduction

Training is model is an essential part of every Machine Learning model. It is important to find the correct balance to prevent overfitting or underfitting. 

Explanation of Hyperparameter tuning for the Random Forest and XGBoost model can be found [here](Predictive%20Analysis/configuring_a_model.md).

<details><summary>Prevention of Under/Over fitting</summary>

Throughout the implementation of the MET prediction model we've encountered multiple obstacles. Here is a list of actions I took to prevent under/over fitting.

<details><summary>Removing Irrelevent Features</summary>

Removing Irrelevent or high correlating features was also used to prevent overfitting. Take the feature Body Mass Index (BMI) for example. This feature was created from the length and weight of the respondent. After analyzing the feature correlation heatmap I found that weight had a very high correlation with BMI. I decided to pick either length and weight or BMI. The final decision was to remove BMI as a feature.

<details><summary>Feature Correlation Heatmap</summary>

![](Images/predictive-analysis/heatmap-walking-prediction.PNG)

</details> 

</details>

<details><summary>Creating Relevent Features</summary>

After struggling for a while and not getting higher correlations for the MET prediction models I thought about adding new relevant features. The speed of the respondent made sense in our case. Running or walking faster means you use more energy which results in a higher MET production. 
The implementation of the `speed` feature was a good choice, because our models all improved quiet a bit!

</details>

<details><summary>Removing Noise</summary>

The noise for the MET prediction models were usually respondents who weren't able to perform the lab activities according to the rest of the respondents. For example: 70+ year old respondents that could not complete the activities for the given time were excluded from the experiment. This has been agreed in consulation with Annemieke van Leuten and John Bolte from Centraal Bureau of Statistiek (CBS). 

</details>

</details>

---

</details>

<details><summary>Evaluating a model</summary>

### Introduction

As explained in [selecting a model](Predictive%20Analysis/selecting_a_model.md), I decided to pick 2 different regression models to compare the results and select the right one for each activity. 
I used a few different methods to calculate prediction scores and eventually picked the most fitting. 

<details><summary>Cross Validation</summary>

The first method is calculated after applying K-Fold Cross Validation on the Random Forest & XGBoost model. I created a simple function that applies `5 folds` on both models and calculates the `mean` score and the `standard deviation (STD)`. These scores are compared for both model to find the most fitting for each activity.

<details><summary>Cross Validation Function</summary>

![](Images/predictive-analysis/cross-validation-function.PNG)

</details>

</details>

---

<details><summary>Applying Test Dataset</summary>

Once the Cross Validation had decent results we decided to apply the separated test dataset on our model to validate the results. 
The test dataset that was separated contained 3 test users with each containing 5 rows of data for each activity. I created a function to apply the test users on the already trained model to see if our model would over/under fit or give good results on new data.

<details><summary>Applying Test Dataset Function</summary>

![](Images/predictive-analysis/test-set-results.PNG)

</details> 

</details>

---

<details><summary>Evaluation Results</summary>

Picking a fitting model for each activity was the final step once Cross Validation and the Test Dataset were applied. I created a table that displays the:
- `R Squared score after Cross Validation`
- `R^2  score after applying the test data set` 
- `Mean Squared Error (MSE) score after applying the test data set` 

<details><summary>Show Table</summary>

After evaluating the scores for both models we, as a team, picked the best scoring model for each activity. The models we picked are marked in green in the table bellow.

As you can see, `Standing` and `Sitting` are not marked. The reason for this is that we decided to leave the predictions for both out of the experiment since they would not impact the result of the main question. This has been agreed in consulation with Annemieke van Leuten and John Bolte from Centraal Bureau of Statistiek (CBS).

![](Images/predictive-analysis/xgboost_vs_randomforest_results2.PNG)

### Final Results

|Activity|Model|
|------------|---------|
|Walking|Random Forest|
|Running|Random Forest|
|Cycling Light|Random Forest|
|Cycling Heavy|XGBoost|

</details>

</details>

---

</details>

<details><summary>Visualizing the outcome of a model</summary>

### Introduction

Informative and straight to the point visualization of your data is very important to make conclusion about what you're actually seeing. This chapter displays the different visualizations that were applied by the creation of the MET prediction models.

<details><summary>Seaborn — Heatmap</summary>

The Seaborn library was used to create a Heatmap to display correlations between all the features. The use of this heatmap can be found in the [Training a model chapter](Predictive%20Analysis/training_a_model.md).

This heatmap was used to see which features were low or high correlated to the `mean_met` target value. Looking at the correlations we could already see that `sum_mag_acc` and `mean_speed` were high correlating features and are probably good features the predict the `mean_met` value.
![](Images/predictive-analysis/heatmap-walking-met.png)

</details>

---

<details><summary>Finding optimal n_estimators — Line Chart</summary>

The following visualization displays the scores from a certain range, in this case (1-210). I wanted to find the best amount of iterations for this model. In some cases the `n_estimator` value of 2 gave the best results, this would be unlikely so in these cases I decided to start from 10 instead of 1.
At first the amount of iterations was set to 100, but after analysing the results I saw that the scores were going up around the 100 mark. I decided to expand this to 210 to see if it went higher, but it didn't.

![](Images/predictive-analysis/n_estimators_results_plot.PNG)

</details>

---

<details><summary>Ground Truth vs Prediction — Bar Chart</summary>

This Bar Chart shows the differences between the `Ground Truth` and the `Actual Prediction`. The 2 values were set next to eachother to see if there were outliers. Once we could see the outliers we could act upon it. 

![](Images/predictive-analysis/ground_truth_vs_prediction.PNG)

</details>

---

<details><summary>Ground Truth vs Prediction — Scatter Plot</summary>

This Scatter Plot shows the same results as the Bar Chart above this section. The difference is the type of visualization.
Here you can see how the `Ground Truth` and `Prediction` fit the Regression line. With this scatter plot it is easier to spot if there are big outliers or if the data fits the regression line.

![](Images/predictive-analysis/predictions_scatterplot.PNG)


</details>

---

</details>

# Domain knowledge
- [Introduction of the subject field](Domain%20Knowledge/introduction_subject_field.md)
- [Literature research](Domain%20Knowledge/literature_research.md)
- [Explanation of Terminology, jargon and definitions](Domain%20Knowledge/terminology_jargon_definitions.md)

# Data preprocessing
- [Data exploration](Data%20Preprocessing/data_exploration.md)
- [Data cleansing](Data%20Preprocessing/data_cleaning.md)
- [Data preparation](Data%20Preprocessing/data_preparation.md)
- [Data explanation](Data%20Preprocessing/data_explanation.md)
- [Data visualization (exploratory)](Data%20Preprocessing/data_visualization.md)

# Communication
- [Presentations](Communication/presentations.md)
- [Writing paper](Communication/writing_paper.md)
