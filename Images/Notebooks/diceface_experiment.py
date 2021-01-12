#!/usr/bin/env python
# coding: utf-8

# ### By Colin Werkhoven
# Data pre-processing for a `diceface` lineair regression experiment

# ### Literature 
# Merge functionality: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html

# ### Goal of this code
# This code is meant to merge the MET values which are calculated with the `vyntus` file to the activ_pal file with 15 seconds intervals. This new dataframe will be used to train a lineair regressionmodel and find possible deviations once a `diceface` changes direction.

# In[1]:


# Imports and Initializations

from helpers import pandas_helper as helper
from helpers import math_helper as mhelper
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

correspondent = 'BMR004'
activpal_df = helper.read_csv_activpal1_15(correspondent)
vyntus_df = helper.read_csv_vyntus(correspondent)


# ### Sorting the `vyntus` file on timestamp
# The vyntus file was not sorted, it was easier to see the minimum and maximum index values once it was sorted on index

# In[2]:


vyntus_df.sort_index(inplace=True)
vyntus_df


# ### Get the start and end date of the vyntus file
# The `start` and `end` timestamps are neccessary to get the correct data from the `activpal_df` file

# In[3]:


start_time = vyntus_df.index.min()
end_time = vyntus_df.index.max()

print('Start time:')
print(start_time)
print('End time:')
print(end_time)


# ### Filtering activpal_15 file with the start and end time from the vyntus file
# To get acccurate results we need to have both dataframes within the same time range

# In[4]:


activpal_resampled = activpal_df.loc[start_time:end_time].copy()
activpal_resampled


# ### Resampled the vyntus file to 15 seconds to match the activ_pal15 file
# To assign the correct MET values to the vyntus file, we need to have both dataframes in the correct interval
# 
# Secondly we removed the first row since this timestamp was not similar to the activ_pal15 timestamp

# In[5]:


resampling = vyntus_df.resample('15S').mean()
vyntus_resampled_15 = resampling[1:].copy()
vyntus_resampled_15


# ### Get the weight of the correspondent
# The weight of the correspondent is neccessary to calculate the MET value of the activities

# In[6]:


respondent_df = helper.read_csv_respondents()
respondent_details = respondent_df.loc[float(correspondent[3:6])]
respondent_details['gewicht']


# ### Calculate the MET values 
# First we need to add the weight of the user to the `vyntus` dataframe to be able to calculate the MET value
# 
# Secondly we can calculate the MET value and add this value to the `vyntus_resampled` dataframe

# In[7]:


vyntus_resampled_15['weight'] = respondent_details['gewicht']
vyntus_resampled_15['MET'] = [mhelper.calculate_met(vo2, weight) for vo2, weight in zip(vyntus_resampled_15['vyn_VO2'], vyntus_resampled_15['weight'])]
vyntus_resampled_15


# ### Add the MET values to the activ_pal15 dataframe
# Merging the `vyntus` MET value to the activ_pal15 dataframe

# In[8]:


activpal_resampled['MET'] = activpal_resampled.merge(vyntus_resampled_15, left_index=True, right_index=True)['MET']


# ### Display the final dataframe
# MET values are added
# 
# This dataframe is now ready for the lineair regression diceface experiment

# In[9]:


activpal_resampled


# ### Added a new `change` row to indicate where the diceface changes it's direction
# With this new column it will be easy to see where a diceface is about to change direction

# In[10]:


activpal_resampled['change'] = activpal_resampled.pal_diceFace != activpal_resampled.pal_diceFace.shift(-1)
activpal_resampled


# ### Linear Regression Experiment

# In[11]:


activpal_resampled['MET'].isnull().values.any()


# ### Prepare the right data for the model
# For this model we needed the `avgAccelVolume`, `MET` and the `change` of the diceface

# In[12]:


activpal_resampled.dropna(how='any', inplace=True)

x = activpal_resampled['pal_avgAccelVolume'].to_numpy().reshape(-1, 1)
y = activpal_resampled['MET']


linear_regression_model = linear_model.LinearRegression()
linear_regression_model.fit(x, y)


# In[13]:


predict_y = linear_regression_model.predict(x)
predict_y


# In[14]:


linear_regression_model.score(x, y)


# ### Plotting the linear regression

# In[15]:


plt.scatter(x, y)
print(activpal_resampled['pal_diceFace'].unique())

try:
    change_filtered = activpal_resampled[activpal_resampled['change'] == True]
    
    change_y = change_filtered['MET']
    change_x = change_filtered['pal_avgAccelVolume']

    plt.scatter(change_x, change_y)
except:
    print('No changes' )


plt.plot(x, predict_y, color='black', linewidth=3)
plt.title('Visualize the change in acceleration on diceface change')
plt.ylabel('MET value')
plt.xlabel('Average Acceleration Volume')
plt.show()


# In[ ]:




