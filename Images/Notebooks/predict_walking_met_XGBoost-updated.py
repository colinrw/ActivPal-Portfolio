#!/usr/bin/env python
# coding: utf-8

# ### Predicting the `walking` MET using the XGBoost Regression Model
# By Colin Werkhoven (17079578)

# ### Imports and Initializations

# In[154]:


from helpers import pandas_helper as pdh
from helpers import math_helper as mth
from sensors.activpal import *
from utils import read_functions
from scipy.stats import linregress
from sklearn.model_selection import train_test_split, KFold, cross_val_score, RandomizedSearchCV, GridSearchCV
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectFromModel, RFE, RFECV
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error as MSE 
from sklearn.metrics import r2_score
from pprint import pprint
import scipy.integrate as it
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import seaborn as sns
import xgboost as xg

activpal = Activpal()


# ### Get the prepared dataframe

# In[155]:


all_df = pd.read_csv('../../data/all_activities.csv', delimiter=',', index_col=0)


# ### Get the walking activities from the entire dataframe

# In[156]:


walking_df = all_df.loc[all_df['activity'] == 'lopen']
walking_df.head()


# ### Function to create a dataframe based on the added respondents

# In[157]:


def create_respondent_dataframe(respondents):
    new_df = pd.DataFrame(index=pd.to_datetime([]))
    
    for respondent in respondents:
        resp_df = walking_df[(walking_df['respondent_code'] == respondent)]
        new_df = pd.concat([new_df ,resp_df])
        
    return new_df


# ### Train + Validation Respondents

# In[158]:


training_validation_users = ['BMR002', 'BMR004', 'BMR011', 'BMR012', 'BMR014', 'BMR018', 'BMR031', 'BMR032', 'BMR033', 'BMR034', 'BMR036', 'BMR041', 'BMR042', 'BMR043', 'BMR044', 'BMR052', 'BMR053', 'BMR055', 'BMR058', 'BMR064', 'BMR097', 'BMR098']
all_df = create_respondent_dataframe(training_validation_users)


# ### Test Respondents

# In[159]:


test_users = ['BMR008', 'BMR040', 'BMR030'] 
all_df_test = create_respondent_dataframe(test_users)


# ### Seaborn Heatmap
# Created a heatmap to visualize the correlation between the features

# In[160]:


plt.figure(figsize=(12,10))
cor = all_df.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()


# ### List of all features
# A list of all the features in the `all_df` dataframe

# In[219]:


all_features = ['sum_mag_acc', 'weight_kg', 'length_cm', 
                'is_sporter', 'age_category', 'meets_balance_guidelines', 
                'meets_activity_guidelines', 'estimated_level', 
                'gender', 'mean_speed']


# ### Find the best features for our MET prediction model
# This function finds the best features for the model. 
# 
# Returns a list of the chosen features.

# In[220]:


def find_optimal_features(features):
    X = all_df[features]
    y = all_df['mean_met']
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=0)
    
    xgbr = xg.XGBRegressor()
    rfe = RFE(estimator=xgbr, n_features_to_select=7, step=1)
    rfe = rfe.fit(X_train, y_train)
    
    print('Chosen best %s feature by rfe: %s' % (len(X_train.columns[rfe.support_]), X_train.columns[rfe.support_]))
    
    return X_train.columns[rfe.support_]


# ### Model Creation
# Splitting the data with the train_test_split method
# 
# Split ratio: 80%, 20% ratio

# In[221]:


features_by_rfe = find_optimal_features(all_features)
columns_by_rfe = ['sum_mag_acc', 'weight_kg', 'length_cm', 'age_category',
       'meets_balance_guidelines', 'mean_speed']
# X = all_df[['sum_mag_acc', 'weight_kg', 'length_cm', 'meets_balance_guidelines', 'mean_speed']]
X = all_df[columns_by_rfe]
# X = all_df[features_by_rfe]
y = all_df['mean_met']
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=0)
print('X_train Shape:', X_train.shape)
print('X_valid Shape:', X_valid.shape)
print('y_train Shape:', y_train.shape)
print('y_valid Shape:', y_valid.shape)


# In[222]:


X_train.head()


# In[223]:


y_train.head()


# ### Find Optimal Amount of `n_estimators` for our model

# In[224]:


def optimal_amount_estimators(X_train, y_train, X_valid, y_valid):
    # Empty Dictionary to store the best results + the index
    score_list = {}
    for i in range(5, 100):
        highest_score = 0
        xgbregressor = xg.XGBRegressor(n_estimators=i, random_state=0)
        xgbregressor.fit(X_train, y_train)

        predictions = xgbregressor.predict(X_valid)
        valid_score = xgbregressor.score(X_valid, y_valid)
        score_list[i] = valid_score
    
    # Plotting the scores
    x, y = zip(*score_list.items())
    plt.plot(x, y)
    plt.title("Find the best amount of n_estimators based on predicted score")
    plt.xlabel("Amount of iterations")
    plt.ylabel("Predicted score")
    plt.grid()
    plt.show()
    
    # Getting the highest score
    highest_score = max(score_list, key=score_list.get)
    optimal_estimator = highest_score
    print("The most optimal n_estimator is:")
    print("Key: %s, highest score: %s" % (highest_score, score_list[highest_score]))
    
    return optimal_estimator


# ### Creation of the XGBoostRegressor Model
# The optimal amount of estimators is taken from the `optimal_amount_estimators` function 

# In[225]:


# Get the optimal amount of n_estimators
optimal_estimators = optimal_amount_estimators(X_train, y_train, X_valid, y_valid)

xgbr = xg.XGBRegressor(n_estimators=optimal_estimators, objective='reg:squarederror', random_state=0)
xgbr.fit(X_train, y_train)

predictions = xgbr.predict(X_valid)


# ### Cross validation on model

# In[226]:


def apply_cross_validation(model, X, y):
    print('\nCross Validation Results')
    scores = cross_val_score(model, X, y, cv=5)
    print("R^2 of the predictions: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()))


# ### Plotting the `Ground Truth` VS `Predictions`

# In[227]:


def plot_ground_truth_vs_prediction(y, pred, title='Predictions on validation dataset'):
    bar_width = 0.35

    pred_index = np.arange(len(pred))
    y_index = np.arange(len(y)) + bar_width

    plt.bar(pred_index, pred, bar_width, label='Prediction')
    plt.bar(y_index, y, bar_width, label='Ground Truth')


    plt.xlabel('Prediction Number')
    plt.ylabel("MET")
    plt.title(title)
    plt.xticks(pred_index + 0.15, pred_index)

    plt.legend()
    plt.grid()
    plt.show()


# ### Display useful results from the XGBoost Model
# This function displays the `R Squared` and the `Mean Absolute Error` of the XGBoost model. 

# In[228]:


def display_results(y_valid, predictions):
    score = np.sqrt(MSE(y_valid, predictions))
    rsquared_score = r2_score(y_valid, predictions)
    print("Results before cross validation")
    print('R2 Score: %s' % rsquared_score)
    print('Mean Squared Error: %s' % score)


# ### Display Scatter plot of results

# In[229]:


def plot_results_as_scatter(y_valid, predictions):
    plt.scatter(y_valid, predictions, marker='.', c='r')
    plt.plot(y_valid, y_valid)
    
    plt.grid()
    
    plt.title('MET prediction - scatterplot')
    plt.xlabel('MET Ground Truth')
    plt.ylabel('MET Prediction')
    
    plt.show()


# # Displaying Results of the XGBoost Model

# In[230]:


plot_ground_truth_vs_prediction(y_valid, predictions)
plot_results_as_scatter(y_valid, predictions)
display_results(y_valid, predictions)
apply_cross_validation(xgbr, X, y)


# ### HyperParameter Tuning
# Trying to find the optimal parameters for our `XGBRegressor` model

# In[231]:


print('Parameters currently in use:\n')
pprint(xgbr.get_params())


# ### Creation of the possible best parameter values

# In[232]:


random_grid = {
    "learning_rate": [0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ] ,
     "max_depth": [ 3, 4, 5, 6, 8, 10, 12, 15],
     "min_child_weight": [ 1, 3, 5, 7 ],
     "gamma": [ 0.0, 0.1, 0.2 , 0.3, 0.4 ],
     "colsample_bytree": [ 0.3, 0.4, 0.5 , 0.7 ] 
}
pprint(random_grid)


# ### Functions to apply Hyperparameter Tuning to a new model
# Theese functions apply hyperparameter tuning to a new model and returns a model with the best results
# 
# src: https://towardsdatascience.com/doing-xgboost-hyper-parameter-tuning-the-smart-way-part-1-of-2-f6d255a45dde
# 
# src #2: https://www.youtube.com/watch?v=9HomdnM12o4&ab_channel=KrishNaik

# ### Validating the models with the test users
# This function applies the test dataset on the model that is added as parameter

# In[233]:


def apply_test_dataset(model, test_df, columns_by_rfe):
    test_X = test_df[columns_by_rfe]
    test_Y = test_df['mean_met']
    
    test_prediction = model.predict(test_X)
    plot_ground_truth_vs_prediction(test_Y, test_prediction)
    display_results(test_Y, test_prediction)


# ### Hyperparameter Tuning function that applies GridSearch
# 
# Parameter: a list of possible parameter values
# 
# The function applies `Grid Search` to a new XGB Regressor model and displays the results of the Hyperparameter Tuning

# In[ ]:


def apply_grid_search_hyperparameter_tuning(grid):
    # Create the XGBoost Regression model
    xgb_model = xg.XGBRegressor()
    
    # Apply the XGBRegressor + other parameters on GridSearch
    xgbr_randomized = GridSearchCV(estimator=xgb_model, param_grid=grid, 
                                        cv=5, verbose=3, n_jobs=-1)
    
    # Training and fitting the new model
    xgb_model.fit(X_train, y_train)
    xgb_predictions = xgb_model.predict(X_valid)
    
    print('Train Validation Dataset Results')
    plot_ground_truth_vs_prediction(y_valid, xgb_predictions)
    display_results(y_valid, xgb_predictions)
    
    print('Test Dataset Results')
    apply_test_dataset(xgb_model, all_df_test, columns_by_rfe)


# ### Hyperparameter Tuning function that applies RandomizedSearch
# 
# Parameter: a list of possible parameter values
# 
# The function applies `Randomized Search` to a new XGB Regressor model and displays the results of the Hyperparameter Tuning

# In[235]:


def apply_randomized_search_hyperparameter_tuning(grid):
    # Create the XGBoost Regression model
    xgb_model = xg.XGBRegressor()
    
    # Apply the XGBRegressor + other parameters on RandomizedSearch
    xgbr_randomized = RandomizedSearchCV(estimator=xgb_model, param_distributions=grid, n_iter=5,
                                         n_jobs=-1, cv=5, verbose=3)
    
    # Training and fitting the new model
    xgb_model.fit(X_train, y_train)
    xgb_predictions = xgb_model.predict(X_valid)
    
    print('Train Validation Dataset Results')
    plot_ground_truth_vs_prediction(y_valid, xgb_predictions)
    display_results(y_valid, xgb_predictions)
    
    print('Test Dataset Results')
    apply_test_dataset(xgb_model, all_df_test, columns_by_rfe)


# ### Displaying the results from hyperparameter tuning for `Randomized Search`

# In[236]:


apply_randomized_search_hyperparameter_tuning(random_grid)


# ### Displaying the results from hyperparameter tuning for `Grid Search`

# In[237]:


apply_grid_search_hyperparameter_tuning(random_grid)


# ### Conclusion
# After applying `Grid Search` and `Randomized Search` the R Squared score and Mean Squared Error(MSE) `didn't` improve compared to the previous model.
# 
# Hyperparameter tuning is not improving the model for the `walking` activity.

# In[238]:


# from joblib import dump

# dump(xgbr, 'walking.dat')

