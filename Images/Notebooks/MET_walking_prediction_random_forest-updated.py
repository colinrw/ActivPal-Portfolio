#!/usr/bin/env python
# coding: utf-8

# ### Practicing the Random Forest Algorithm
# By Colin Werkhoven

# ### The Issue
# We need to predict the MET value with the X, Y and Z data from a respondent

# ### Additional Comments
# Why we picked `random_state = 0`: the sklearn docs gives `0` and `42` as the popular values.
# 
# Found here: https://scikit-learn.org/stable/glossary.html#term-random-state

# In[2]:


# Imports and Initializations
from helpers import pandas_helper as pdh
from helpers import math_helper as mth
from sensors.activpal import *
from utils import read_functions
from scipy.stats import linregress
from sklearn.model_selection import train_test_split, KFold, cross_val_score, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectFromModel, RFE, RFECV
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error as MSE 
from sklearn.metrics import r2_score
from pprint import pprint
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import seaborn as sns

activpal = Activpal()


# ### Get the prepared dataframe

# In[3]:


all_df = pd.read_csv('../../data/all_activities.csv', delimiter=',', index_col=0)


# ### Get the walking activities from the entire dataframe

# In[4]:


walking_df = all_df.loc[all_df['activity'] == 'lopen']
walking_df.head()


# ### Function to create a dataframe based on the added respondents

# In[5]:


def create_respondent_dataframe(respondents):
    new_df = pd.DataFrame(index=pd.to_datetime([]))
    
    for respondent in respondents:
        resp_df = walking_df[(walking_df['respondent_code'] == respondent)]
        new_df = pd.concat([new_df ,resp_df])
        
    return new_df


# ### Train + Validation Respondents

# In[6]:


training_validation_users = ['BMR002', 'BMR004', 'BMR011', 'BMR012', 'BMR014', 'BMR018', 'BMR031', 'BMR032', 'BMR033', 'BMR034', 'BMR036', 'BMR041', 'BMR042', 'BMR043', 'BMR044', 'BMR052', 'BMR053', 'BMR055', 'BMR058', 'BMR064', 'BMR097', 'BMR098']
all_df = create_respondent_dataframe(training_validation_users)


# ### Test Respondents

# In[7]:


test_users = ['BMR008', 'BMR040', 'BMR030'] 
all_df_test = create_respondent_dataframe(test_users)


# ### Seaborn Heatmap
# Created a heatmap to visualize the correlation between the features

# In[8]:


plt.figure(figsize=(12,10))
cor = all_df.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()


# ### List of all features
# A list of all the features in the `all_df` dataframe

# In[9]:


all_features = ['sum_mag_acc', 'weight_kg', 'length_cm',  
                'is_sporter', 'age_category', 'meets_balance_guidelines', 
                'meets_activity_guidelines', 'estimated_level', 
                'gender', 'mean_speed']


# ### Find the best features for our MET prediction model
# Parameter: list of all features
# 
# This function finds the best features for the model. 
# 
# Returns a list of the chosen features.

# In[10]:


def find_optimal_features(features):
    
    #splitting the data
    X = all_df[features]
    y = all_df['mean_met']
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=0)
    
    # Creation of the model
    rfm = RandomForestRegressor()
    rfe = RFE(estimator=rfm, n_features_to_select=6, step=1)
    
    # Fitting the model + printing the results
    rfe = rfe.fit(X_train, y_train)
    print('Chosen best %s feature by rfe: %s' % (len(X_train.columns[rfe.support_]), X_train.columns[rfe.support_]))
    
    return X_train.columns[rfe.support_]


# ### Optimal combination of features
# 
# Output from the feature selection function is a list of the best features

# In[11]:


columns_by_rfe = find_optimal_features(all_features)


# ### Model Creation
# Splitting the data with the train_test_split method
# 
# Split ratio: `80% Train`, `20% Valid`

# In[12]:


X = all_df[columns_by_rfe]
y = all_df['mean_met']
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=0)
print('X_train Shape:', X_train.shape)
print('X_valid Shape:', X_valid.shape)
print('y_train Shape:', y_train.shape)
print('y_valid Shape:', y_valid.shape)


# In[13]:


X_train.head()


# In[14]:


y_train.head()


# ### Getting the optimal amount of trees
# Here we try different `n_estimators` and find the highest score for our model
# 
# This function tries a different number of trees in a for loop and eventually finds the best score number of trees,
# 
# The fuction returns a number which represents the highest scoring `n_estimators`.

# In[15]:


def optimal_amount_estimators(X_train, y_train, X_valid, y_valid):
    # Empty Dictionary to store the best results + the index
    score_list = {}
    
    # The range of the possible best number of trees
    for i in range(1,210):
        highest_score = 0
        randomForest = RandomForestRegressor(n_estimators=i, random_state=0)
        randomForest.fit(X_train, y_train)
        
        # Adding all scores to the dictionary
        score = randomForest.score(X_valid, y_valid)
        score_list[i] = score
    
    # Plotting the number of trees with the associated score
    x, y = zip(*score_list.items())
    plt.plot(x, y)
    plt.title("Find the best amount of n_estimators based on predicted score")
    plt.xlabel("Amount of iterations")
    plt.ylabel("Predicted score")
    plt.show()
    
    # Finding the highest score in the dictionary
    highest_score = max(score_list, key=score_list.get)
    optimal_estimator = highest_score
    print("The most optimal n_estimator is:")
    print("Key: %s, highest score: %s" % (highest_score, score_list[highest_score]))
    
    return optimal_estimator


# ### Applying the optimal estimator to the RandomForest
# We apply the most optimal estimator from the function above for our final model

# In[16]:


# Get the optimal amount of n_estimators
optimal_estimators = optimal_amount_estimators(X_train, y_train, X_valid, y_valid)

randomForest = RandomForestRegressor(n_estimators=optimal_estimators, random_state=0, oob_score=True)
randomForest.fit(X_train, y_train)

predictions = randomForest.predict(X_valid)


# ### Cross Validation On Model
# 
# Cross Validation uses the `train` and `valid` dataset combined
# 
# Parameters:
# - model: the Random Forest or XGBoost model
# - X: the entire dataframe without the test data
# - y: all mean_met values without the test data
# 
# This function displays the `mean` and `standard devitation` after Cross Validation

# In[17]:


def apply_cross_validation(model, X, y):
    scores = cross_val_score(model, X, y, cv=5)
    print('\nCross Validation Results')
    print("R^2 of the predictions: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()))


# ### Plot the `ground truth` VS  `prediction`
# This function plots the ground truth and the prediction

# In[18]:


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


# ### Display useful results from the Random Forest Model
# This function displays the `R Squared` and the `Mean Absolute Error` of the Random Forest model. 

# In[19]:


def display_results(y_valid, predictions):
    score = np.sqrt(MSE(y_valid, predictions))
    rsquared_score = r2_score(y_valid, predictions)
    print("Results before cross validation")
    print('R2 Score: %s' % rsquared_score)
    print('Mean Squared Error: %s' % score)


# ### Display Scatter plot of results

# In[20]:


def plot_results_as_scatter(y_valid, predictions):
    plt.scatter(y_valid, predictions, marker='.', c='r')
    plt.plot(y_valid, y_valid)
    
    plt.grid()
    
    plt.title('MET prediction - scatterplot')
    plt.xlabel('MET Ground Truth')
    plt.ylabel('MET Prediction')
    
    plt.show()


# ### Displaying Results of the Random Forest Model

# In[21]:


plot_ground_truth_vs_prediction(y_valid, predictions)
plot_results_as_scatter(y_valid, predictions)
display_results(y_valid, predictions)
apply_cross_validation(randomForest, X, y)


# ### Hyperparameter Tuning
# Applying Hyperparameter Tuning to see if we can improve the results of our model

# In[22]:


print('Parameters currently in use:\n')
pprint(randomForest.get_params())


# ### Creation of all the possible features parameters 
# Here we create different inputs for Hyperparameter Tuning
# 
# Hyperparameter Tuning features found here: https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74 

# In[23]:


n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
max_features = ['auto', 'sqrt']
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)
min_samples_split = [2, 5, 10]
min_samples_leaf = [1, 2, 4]
bootstrap = [True, False]


# ### Add all the features in a random_grid object
# The `random_grid` now contains all the features with different inputs. This will be used for hypertuning. 

# In[24]:


random_grid = {
   'n_estimators': n_estimators,
   'max_features': max_features,
   'max_depth': max_depth,
   'min_samples_split': min_samples_split,
   'min_samples_leaf': min_samples_leaf,
   'bootstrap': bootstrap
}
pprint(random_grid)


# ### Function to apply Hyperparameter Tuning to a new model
# 
# Parameter: a list of possible parameter values
# 
# This function applies hyperparameter tuning to a new model and returns a model with the best results

# In[25]:


def apply_hyperparameter_tuning(grid):
    randomForestTuning = RandomForestRegressor()
    rf_random = RandomizedSearchCV(estimator=randomForestTuning, param_distributions=grid, 
                                   n_iter=100, cv=3, verbose=2, random_state=0, n_jobs=-1)

    rf_random.fit(X_train, y_train)
    
    return rf_random


# ### Display the best values for the parameters

# In[26]:


hyperparameter_model = apply_hyperparameter_tuning(random_grid)
hyperparameter_model_prediction = hyperparameter_model.predict(X_valid)
plot_ground_truth_vs_prediction(y_valid, hyperparameter_model_prediction)
display_results(y_valid, hyperparameter_model_prediction)


# In[27]:


hyperparameter_model.best_params_


# ### Validating the models with the test users
# 
# Parameters:
# - model: the Random Forest or XGBoost model
# - test_df: the separated test data set
# - columns_by_rfe: the columns selected by the Recursive Feature Selection function
# 
# This function applies the test dataset on the already trained model and displays the results

# In[28]:


def apply_test_dataset(model, test_df, columns_by_rfe):
    
    # Splitting the test data
    test_X = test_df[columns_by_rfe]
    test_Y = test_df['mean_met']
    
    # Get all predictions
    test_prediction = model.predict(test_X)
    
    # Display functions
    plot_ground_truth_vs_prediction(test_Y, test_prediction)
    display_results(test_Y, test_prediction)
    
    plot_results_as_scatter(test_Y, test_prediction)


# ### Apply test set on randomForest model

# In[29]:


apply_test_dataset(randomForest, all_df_test, columns_by_rfe)


# ### Apply test set on hyperparameterized model

# In[30]:


apply_test_dataset(hyperparameter_model, all_df_test, columns_by_rfe)


# In[31]:


from joblib import dump

dump(hyperparameter_model, 'walking.dat')


# In[ ]:




