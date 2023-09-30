#IMPORTING LIBS
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as mlt
#IMPORTING DATA SET
data=pd.read_csv('diamonds.csv')
#PERFORMING BASIC EDA
pd.set_option('display.max_columns',50)
data.head()
data.info()
data.isna().sum()
data1=pd.read_csv('diamonds.csv',na_values=[0])
data1.isna().sum()
columns=['x','y','z']
for column in columns:
    mean=data[column].mean()
    data[column]=data[column].replace(0,mean)
for column in columns:
data.isna().sum()
data.describe()
data.columns
#converting caterigorical to numerical
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
columns=['cut','color','clarity']
for column in columns:
    data[column]=encoder.fit_transform(data[column])
data['cut'].unique()    
data['cut'].value_counts()

data['color'].unique()
data['color'].value_counts()

data['cut'].unique()
data['cut'].value_counts()
data.describe()
#SEGREGATING DATA IN INPUT AND OUTPUT
x=data.drop(['price'],axis=1)
y=data['price']
#FINDING CORR() AND PLOTING GRAPHS
mlt.figure(figsize=(10,8))
sns.pairplot(data)

columns=['Unnamed: 0', 'carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']
    mlt.figure(figsize=(10,8))
    sns.boxplot(x=data['price'],y=data[column])
    
mlt.figure(figsize=(10,8))
sns.heatmap(data.corr(),annot=True)

