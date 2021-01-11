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

<details><summary>Task definition</summary>

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

---

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

</details>

- [Task definition](Research%20Project/task_definition.md)
- [Evaluation](Research%20Project/evaluation.md)
- [Conclusions](Research%20Project/conclusions.md)
- [Planning](Research%20Project/planning.md)

# Predictive Analytics

<details><summary></summary>



</details>

- [Selecting a Model](Predictive%20Analysis/selecting_a_model.md)
- [Configuring a Model](Predictive%20Analysis/configuring_a_model.md)
- [Training model](Predictive%20Analysis/training_a_model.md)
- [Evaluating a model](Predictive%20Analysis/evaluating_a_model.md)
- [Visualizing the outcome of a model](Predictive%20Analysis/visualizing_the_outcome_of_a_model.md)

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
