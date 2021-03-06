#!/usr/bin/env python
# coding: utf-8

# ___
# 
# 
# ___
# # Logistic Regression Project For Building an ADs clicking prediction model 
# 
# In this project we will be working with a random advertising data set, indicating whether or not a particular internet user clicked on an Advertisement. We will try to create a model that will predict whether or not they will click on an ad based off the features of that user.
# 
# This data set contains the following features:
# 
# * 'Daily Time Spent on Site': consumer time on site in minutes
# * 'Age': A customer age in years
# * 'Area Income': Avg. Income of geographical area of consumer
# * 'Daily Internet Usage': Avg. minutes a day consumer is on the internet
# * 'Ad Topic Line': Headline of the advertisement
# * 'City': City of consumer
# * 'Male': Whether or not consumer was male
# * 'Country': The Country of consumer
# * 'Timestamp': Time at which consumer clicked on Ad or closed window
# * 'Clicked on Ad': 0 or 1 indicated clicking on Ad
# 
# ## Import Libraries
# 
# **Import a few libraries you think you'll need (Or just import them as you go along!)**

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Get the Data
# **Read in the advertising.csv file and set it to a data frame called ad_data.**

# In[3]:


ad_data = pd.read_csv('advertising.csv')
ad_data.head()


# **Check the head of ad_data to show the first five rows of the data**

# In[ ]:





# ** Use info and describe() on ad_data**

# In[ ]:





# In[5]:


ad_data.info()


# In[ ]:





# In[6]:


ad_data.describe()


# ## Exploratory Data Analysis
# 
# Let's use seaborn to explore the data!
# 
# Try recreating the plots shown below!
# 
# ** Create a histogram of the Age**

# In[7]:


sns.displot(ad_data['Age'])


# **Create a jointplot showing Area Income versus Age.**

# In[ ]:





# In[12]:


sns.jointplot(data=ad_data, x='Age',y="Area Income");


# **Create a jointplot showing the kde distributions of Daily Time spent on site vs. Age.**

# In[22]:


sns.jointplot(x='Daily Time Spent on Site', y='Age', data=ad_data, kind='kde' )


# ** Create a jointplot of 'Daily Time Spent on Site' vs. 'Daily Internet Usage'**

# In[ ]:





# In[24]:


sns.jointplot(x='Daily Time Spent on Site', y= 'Daily Internet Usage', data=ad_data, color='green')


# ** Finally, create a pairplot with the hue defined by the 'Clicked on Ad' column feature.**

# In[ ]:





# In[28]:


sns.pairplot(ad_data, hue='Clicked on Ad', diag_kind='hist'); 


# # Logistic Regression
# 
# Now it's time to do a train test split, and train our model!
# 
# You'll have the freedom here to choose columns that you want to train on!

# ** Split the data into training set and testing set using train_test_split**

# In[29]:


from sklearn.model_selection import train_test_split


# In[35]:


x = ad_data[['Daily Time Spent on Site','Age','Area Income','Daily Internet Usage','Male']]


# In[36]:


X_train, X_test, y_train, y_test = train_test_split(
    x, ad_data['Clicked on Ad'], test_size=0.30, random_state=40)


# In[37]:


x.head()


# ** Train and fit a logistic regression model on the training set.**

# In[38]:


from sklearn.linear_model import LogisticRegression 


# In[40]:


logmodel = LogisticRegression(solver='liblinear')
logmodel.fit(X_train,y_train)


# ## Predictions and Evaluations
# ** Now predict values for the testing data.**

# In[41]:


predict = logmodel.predict(X_test)
predict


# ** Create a classification report for the model.**

# In[42]:


from sklearn.metrics import classification_report, confusion_matrix


# In[44]:


print(f'{confusion_matrix(y_test,predict)}\n')
print(classification_report(y_test, predict))
 

# ## Ciao!
# ## Final submission done 