# Selecting a model

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

[<  README](../README.md) — [Configuring a model >](configuring_a_model.md) 