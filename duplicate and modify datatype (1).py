#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Load the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data =pd.read_csv("data_clean.csv")
data


# In[3]:


#Data Structure
print(type)


# In[4]:


data1=data.drop(['Unnamed: 0',"Temp C"],axis=1)
data1


# In[5]:


data.info()


# In[6]:


#Convert the month column datatype to integer data type
data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1


# In[7]:


data1.info()


# In[8]:


#Checkinng the duplicate values in table
#Print the duplicate rows
data1[data1.duplicated()]


# In[9]:


#Print all duplicated rows
data1[data1.duplicated(keep=False)]


# In[10]:


#Change column names(Rename the columns)
data1.rename({'Solar.R': 'Solar','Temp':'Temperature'},axis=1,inplace=True)
data1


# In[11]:


data1.info()


# In[12]:


#Display data1 missing values count in each column isnull().swm()
data.isnull().sum()


# In[13]:


#Visulize data1 missing values using a chart or grap
cols =data1.columns
colours=['black','yellow']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colours),cbar=True)


# In[14]:


#Find the mean and median values of ech numeric column
#Imputation of missing value with median
median_ozone=data1["Ozone"].median()
mean_ozone=data1["Ozone"].mean()
print("Median of Ozone :",median_ozone)
print("Mean of Ozone :",mean_ozone)


# In[15]:


#Replace the Ozone missing values with median
data1['Ozone']=data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[16]:


data1['Solar']=data1['Solar'].fillna(median_ozone)
data1.isnull().sum()


# In[17]:


data1.info()


# In[18]:


#Find the mode values of categorical column(weather)
print(data1["Weather"].value_counts())
mode_weather=data1["Weather"].mode()[0]
print(mode_weather)


# In[19]:


#Impiute missing values(Replace NaN with mode etc.) of "weather" using fillna()
data1["Weather"]=data1["Weather"].fillna(mode_weather)
data1.isnull().sum()


# In[20]:


data1


# In[21]:


#mode of month
print(data1["Month"].value_counts())
mode_month=data1["Month"].mode()[0]
print(mode_month)


# In[22]:


#filling NaN value with mode values
data1["Month"]=data1["Month"].fillna(mode_month)
data1.isnull().sum()


# In[23]:


data1.tail()


# In[24]:


#Reset the index colums
data1.reset_index(drop=True)


# In[25]:


#Create a figure with two subplots ,stacked vertically
fig, axes=plt.subplots(2, 1, figsize=(8, 6), gridspec_kw={'height_ratios':[1, 3]})
#Plot the boxplot in the first (top) subplot
sns.boxplot(data=data1["Ozone"], ax=axes[0],color='skyblue',width=0.5, orient='h')
axes[0].set_title("Boxplot")
axes[0].set_xlabel("Ozone Levels")

#Plot the histogram with KDE Curve in the second (bottom) subplot
sns.histplot(data1["Ozone"], kde=True, ax=axes[1],color='purple',bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("Ozone Levels")
axes[1].set_ylabel("Frequency")
 
#Adjust layout for better spacing
plt.tight_layout()

#Show the plot
plt.show()


# ### Observations
# 
#     The ozone column has extreme values beyond 81 as seen from box plot
#     The same is confirmed from the below right-skewed histogram
# 

# In[26]:


#Create a figure with two subplots ,stacked vertically
fig, axes=plt.subplots(2, 1, figsize=(8, 6), gridspec_kw={'height_ratios':[1, 3]})
#Plot the boxplot in the first (top) subplot
sns.boxplot(data=data1["Solar"], ax=axes[0],color='skyblue',width=0.5, orient='h')
axes[0].set_title("Boxplot")
axes[0].set_xlabel("Solar Levels")

#Plot the histogram with KDE Curve in the second (bottom) subplot
sns.histplot(data1["Solar"], kde=True, ax=axes[1],color='purple',bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("solar Levels")
axes[1].set_ylabel("Frequency")
 
#Adjust layout for better spacing
plt.tight_layout()

#Show the plot
plt.show()


# ## Observations
#     The solar column has no extreme values as we seen from the boxplot
#     the same is confirmed from the below slightly left-skewed histogram
#     

# In[27]:


#Display boxplot for ozone
plt.figure(figsize=(6,2))
plt.boxplot(data1["Ozone"],vert=False)


# In[28]:


#Extract outliers from boxplot for ozone column
plt.figure(figsize=(6,2))
boxplot_data=plt.boxplot(data1["Ozone"],vert=False)
[item.get_xdata() for item in boxplot_data['fliers']]


# In[29]:


data["Ozone"].describe()


# In[30]:


mu=data1["Ozone"].describe()[1]
sigma=data1["Ozone"].describe()[2]
for x in data1["Ozone"]:
    if ((x<(mu - 3*sigma)) or (x>(mu +3*sigma))):
        print(x)


# ## Observations
#     It is observed that only two outliers are identified using std method
#     In box plot method more no of oytliers are identified
#     This is because the assumption of normality is not satified in this colums
#     

# In[31]:


# Quantile-Quantile plot for detection of outliers
import scipy.stats as stats
#Create Q-Q plot
plt.figure(figsize=(8, 6))
stats.probplot(data1["Ozone"], dist='norm', plot=plt)
plt.title("Q-Q plot for outliers detection", fontsize=14)
plt.xlabel("Theoretical Quantiles", fontsize=12)


# ## Observations from Q-Q plot
#     The data does not follow normal distribution as the data points are deviated
#     The data shows  right-skweed distribution and possible outliers

# In[32]:


#Plot Q-Q plot for solar column
# Quantile-Quantile plot for detection of outliers
import scipy.stats as stats
#Create Q-Q plot
plt.figure(figsize=(8, 6))
stats.probplot(data1["Solar"], dist='norm', plot=plt)
plt.title("Q-Q plot for outliers detection", fontsize=14)
plt.xlabel("Theoretical Quantiles", fontsize=12)

