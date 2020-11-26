# Selecting a model

### Introduction
To answer one of the research questions within our project we had to create a model to predict the Metabolic Equivalent of Task (MET) value of given activities. These tasks differentiate between `Running`, `Walking` and a combination of `Cycling Light` and `Cycling Heavy`.

Solving this issue would require a regression model since we need to predict an `integer/double` value(MET) and don't need classification in this case. 

### Approach
My approach for solving this problem was looking at different regression models. I started with finding different models and noting their pros and cons and eventually comparing them to pick atleast 2 possible models. I decided to pick 2 possible models and implement them with the same configurations instead of 1 to prevent getting biased results. 

### Different Regression Models
I researched different regression models to find a possible candidate model for our issue.

##### Random Forest ([source](https://medium.com/swlh/random-forest-and-its-implementation-71824ced454f))
The Random Forest model is a decision tree model which can both be used for Regression and Classification. Besides being a possible regression model, the Random Forest model makes use of `Ensembled Learning`. Ensembled learning means combining multiple results to 1 final result, this method would give more accurate results and minimize getting biased results. 

##### Ridge Regression ([source](https://www.statisticshowto.com/ridge-regression/#:~:text=Ridge%20regression%20is%20a%20way,(correlations%20between%20predictor%20variables)))
TODO

##### K-nearest Neighbour ([source](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761))
Just like the Random Forest Model, the K-nearest Neighbour(KNN) model is also used for Regression and Classification issues. The KNN model is a `supervised machine learning` algorithm, this means the model needs labeled data to produce results. If we look at the `Vyntus (labdata)` we have the `Ground Truth` that needs to be predicted, but this is not the case for `activpal (weekdata)`. This would mean we would only be able to predict on the `labdata` and not the `weekdata`. 

The K-nearest Neighbour model would not be useful to solve our issue, mainly because we don't have the ground truth available all the time. Since K-nearest Neighbour is a supervised machine learning algorithm, apply this on our data would not be sufficient.    

##### XGBoost ([source](https://towardsdatascience.com/https-medium-com-vishalmorde-xgboost-algorithm-long-she-may-rein-edd9f99be63d))
TODO

#### Conclusion
TODO

[<  README](../README.md) — [Configuring a model >](configuring_a_model.md) 