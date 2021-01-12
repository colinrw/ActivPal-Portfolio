#!/usr/bin/env python
# coding: utf-8

# ### By Colin Werkhoven

# In[9]:


# Note: before running the program, make sure to change the name 
# of the CSV file you add data to, to prevent overwriting any data


# In[10]:


from helpers import pandas_helper


# In[11]:


# A list of correspondents with synchronized timestamps and activities
correspondents = ['BMR002', 'BMR004', 'BMR008', 'BMR011', 'BMR012', 'BMR014', 'BMR015', 'BMR018', 'BMR025', 'BMR030', 'BMR031', 'BMR032', 'BMR033', 'BMR034','BMR036', 'BMR040', 'BMR041', 'BMR042', 'BMR043', 'BMR044', 'BMR052', 'BMR053', 'BMR055', 'BMR058', 'BMR060', 'BMR064', 'BMR097', 'BMR098', 'BMR099']
# correspondents = ['BMR002']


# @desc Convert the activity name to an integer. Machine Learning algorithms work better with integers than Strings
# 
# @param dataset - the entire dataframe
# 
# @param mask - the data from the dataframe that fits between the activity timestamps
# 
# @return masked data with integers instead of strings

# In[12]:


def convert_activity_name_to_integer(dataset, mask):
    activity_name = dataset.loc[mask,  'activity_name']
    return activity_name.replace({
        "zitten": 0, "staan": 1,
        "lopen": 2, "traplopen": 3,
        "springen": 4, "rennen": 5,
        "fietsen licht": 6, "fietsen zwaar": 7
    })


# @desc Add the activity to the corresponding timestamp
# 
# @param data - the entire dataframe
# 
# @param activity_values - the start & stop data from the activity
# 
# @param activity_name - the name of the activity

# In[13]:


def add_activity_to_timestamp(data, activity_values, activity_name):
    mask = (data.index >= activity_values['start']) & (data.index <= activity_values['stop'])
    data.loc[mask, 'activity_name'] = activity_name
    data.loc[mask, 'pal_activity'] = convert_activity_name_to_integer(data, mask)


# In[14]:


# The header for the CSV file only needs to be added once
# After adding to the CSV file once, the header will turn to False
addHeader = True

for correspondent in correspondents:
    # Initialization of used data
    activpal_data = pandas_helper.read_csv_activpal20(correspondent)
    activpal_activities = pandas_helper.read_csv_activiteiten(correspondent)
    activpal_data.insert(0, 'participant_code', str(correspondent))
    activpal_data['pal_activity'] = ''
    
    # Loop through the activities of the correspondent
    for activity_index, activity_values in activpal_activities.iterrows():
        add_activity_to_timestamp(activpal_data, activity_values, activity_index)
        
    # Get only the labelled data
    labelled_data = activpal_data[activpal_data['pal_activity'] != '']
    
    # Only in the first iterarion a header needs to be added
    addHeader = True if addHeader == True else False
    
    # Add the labelled data to a CSV file
    labelled_data.to_csv('../../data/combined_correspondent_activities.csv', mode='a', header=addHeader)
    addHeader = False
    print('Successfully added data of: ' + correspondent)
    


# In[ ]:




