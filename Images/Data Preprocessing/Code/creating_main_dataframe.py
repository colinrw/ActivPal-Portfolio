#!/usr/bin/env python
# coding: utf-8

# In[237]:


# Imports and Initializations
from helpers import pandas_helper as pdh
from helpers import math_helper as mth
from sensors.activpal import *
from utils import read_functions
from scipy.stats import linregress
from sklearn.model_selection import train_test_split, KFold, cross_val_score, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from pprint import pprint
from sklearn.metrics import mean_squared_error
import math
import matplotlib.pyplot as plt
import datetime
import csv

#By Matt
from xgboost import XGBRegressor
from sklearn.feature_selection import SelectFromModel, RFE, RFECV
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import LabelEncoder

import xgboost as xgb
import pandas as pd
import numpy as np

from sklearn.metrics import f1_score, plot_confusion_matrix, confusion_matrix, accuracy_score, precision_score, recall_score, confusion_matrix, classification_report, r2_score

from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error as MSE 

import scipy.integrate as it

activpal = Activpal()


# In[238]:


def convert_string_to_number(dataframe, column_name):
    return dataframe.replace({
        column_name: {
            "nee": 0,
            "ja": 1
        }
    }, inplace=True)


# In[239]:


def convert_age_to_number(dataframe, age_category):
    age_convertion = {
        age_category: {
            "15-19": 0, "20-24": 1, "25-29": 2, "30-34": 3, 
            "35-39": 4,  "40-44": 5, "45-49": 6, "50-54": 7,  
            "55-59": 8,  "60-64": 9, "65-69": 10,  "70-74": 11, "75-79": 12
        }
    }
    return dataframe.replace(age_convertion, inplace=True)


# In[240]:


def convert_level_to_number(dataframe, estimated_level):
    level_convertion = {
        estimated_level: {
            "niet actief": 0,
            "actief": 1
        }
    }
    return dataframe.replace(level_convertion, inplace=True)


# In[241]:


def convert_gender_to_number(dataframe, gender):
    gender_convertion = {
        gender: {
            "man": 0,
            "vrouw": 1
        }
    }
    return dataframe.replace(gender_convertion, inplace=True)


# In[242]:


def get_vyntus_df(correspondent, start, stop):
    vyntus_df = pdh.read_csv_vyntus(correspondent)
    mask = (vyntus_df.index >= start) & (vyntus_df.index < stop)
    vyntus_df = vyntus_df.loc[mask]
    
    min_index = vyntus_df.index.min()
    max_index = vyntus_df.index.max()
    
    respondents_df = pdh.read_csv_respondents_speed()
    corr_number = int(correspondent.replace('BMR0', '')) 
    weight = respondents_df['gewicht'][corr_number]
    length_m = respondents_df['lengte'][corr_number] / 100
    vyntus_df['vyn_VO2'] = [float(vo2.replace(',', '.')) if type(vo2) == str else vo2 for vo2 in vyntus_df['vyn_VO2']]
    
    vyntus_df['met'] = mth.calculate_met(vyntus_df['vyn_VO2'], weight)
    vyntus_df['weight_kg'] = weight
    vyntus_df['length_cm'] = length_m * 100
    vyntus_df['bmi'] = mth.calculate_bmi(weight, length_m)
    vyntus_df['is_sporting'] = respondents_df['sporter'][corr_number]
    vyntus_df['age_category'] = respondents_df['leeftijdscategorie'][corr_number]
    
    vyntus_df['walking_speed_km'] = respondents_df['loop_snelheid_km'][corr_number]
    vyntus_df['running_speed_km'] = respondents_df['ren_snelheid_km'][corr_number]
    convert_age_to_number(vyntus_df, "age_category")
    
    vyntus_df['meets_balance_guidelines'] = respondents_df['voldoet aan richtlijn balansoefeningen'][corr_number]
    convert_string_to_number(vyntus_df, 'meets_balance_guidelines')
    
    vyntus_df['meets_activity_guidelines'] = respondents_df['voldoet aan beweegrichtlijn 2017'][corr_number]
    convert_string_to_number(vyntus_df, 'meets_activity_guidelines')
    
    vyntus_df['estimated_level'] = respondents_df['ingeschat niveau'][corr_number]
    convert_level_to_number(vyntus_df, 'estimated_level')
    
    vyntus_df['gender'] = respondents_df['geslacht'][corr_number]
    convert_gender_to_number(vyntus_df, "gender")
    
    vyntus_df = vyntus_df.resample('60s').mean()[:-1]
    return (vyntus_df, min_index, max_index)


# In[243]:


def get_speed(x_acc, y_acc, z_acc):

    activpal_time = 0.05
        
    x_vel = np.array([sum(x_acc[:i]) * activpal_time for i in range(len(x_acc))])
    y_vel = np.array([sum(y_acc[:i]) * activpal_time for i in range(len(y_acc))])
    z_vel = np.array([sum(z_acc[:i]) * activpal_time for i in range(len(z_acc))])
        
        
    return np.sqrt(x_vel ** 2 + y_vel **2 + z_vel ** 2)


# In[244]:


def get_raw_df(correspondent, start, stop):
    df = activpal.read_data(correspondent, start, stop)
    mask = (df.index >= start) & (df.index < stop)
    df = df.loc[mask]
    
    df = df[['pal_accX', 'pal_accY', 'pal_accZ']].apply(mth.convert_value_to_g)
    df['pal_accX'] = abs(df['pal_accX'])
    df['pal_accY'] = abs(df['pal_accY'])
    df['pal_accZ'] = abs(df['pal_accZ'])
    df['mag_acc'] = mth.to_mag_acceleration(df['pal_accX'], df['pal_accY'], df['pal_accZ'])
    df['speed'] = get_speed(df['pal_accX'], df['pal_accY'], df['pal_accZ'])
    
    df = df.resample('60s').sum()[:-1]

    return df


# In[245]:


def get_timestamps(correspondent, activity='rennen'):
    activities_df = read_functions.read_activities(correspondent)
    
    # Enable for cycling
    start = activities_df.loc[activity].start
    stop = activities_df.loc[activity].stop
    
    return (start, stop)


# In[246]:


def get_regression_df(correspondent, addHeader):
    activities = ['lopen','rennen','staan','zitten','fietsen licht','fietsen zwaar']
    for activity in activities:
        
        start, stop = get_timestamps(correspondent, activity)

        vyntus_df, min_index, max_index = get_vyntus_df(correspondent, start, stop)
        raw_df = get_raw_df(correspondent, min_index, max_index)

        new_df = pd.DataFrame(index=raw_df.index)
        new_df['respondent_code'] = correspondent
        new_df['activity'] = activity
        new_df['mean_met'] = vyntus_df['met']
        new_df['sum_mag_acc'] = raw_df['mag_acc']
        new_df['mean_speed'] = raw_df['speed']
        new_df['weight_kg'] = vyntus_df['weight_kg']
        new_df['length_cm'] = vyntus_df['length_cm']
        new_df['bmi'] = vyntus_df['bmi']
        new_df['is_sporter'] = vyntus_df['is_sporting']
        new_df['age_category'] = vyntus_df['age_category']
        new_df['meets_balance_guidelines'] = vyntus_df['meets_balance_guidelines']
        new_df['estimated_level'] = vyntus_df['estimated_level']
        new_df['walking_speed_km'] = vyntus_df['walking_speed_km']
        new_df['running_speed_km'] = vyntus_df['running_speed_km']
        new_df['gender'] = vyntus_df['gender']
        new_df['meets_activity_guidelines'] = vyntus_df['meets_activity_guidelines']
        
        addHeader = True if addHeader == True else False
        new_df.to_csv('../../data/all_activities.csv', mode='a', header=addHeader)
        addHeader = False
    
    return new_df


# In[247]:


correspondents = ['BMR004', 'BMR008', 'BMR011', 'BMR012', 'BMR034', 'BMR036', 'BMR043', 'BMR052', 'BMR053', 'BMR055', 'BMR058', 'BMR064', 'BMR098',  'BMR041', 'BMR044',  'BMR097', 'BMR031', 'BMR032', 'BMR040', 'BMR042', 'BMR002', 'BMR014', 'BMR018', 'BMR030', 'BMR033']
addHeader = True

for corr in correspondents:
    test_dataframe = get_regression_df(corr, addHeader)
    addHeader = False


# In[ ]:




