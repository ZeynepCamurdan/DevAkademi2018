import pandas as pd
import numpy as np
import json
import datetime
import matplotlib.pylab as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score


#convert json to xlsx
#pd.read_json("C://Users//MONSTER//Desktop//all_data 3.json", encoding='utf-8').to_excel("C://Users//MONSTER//Desktop//all_data 3.xlsx")
fileName1='C://Users//MONSTER//Desktop//file1.xlsx'  #file1 is train data. (17.10.2018 - 30.09.2018)
fileName2='C://Users//MONSTER//Desktop//file2.xlsx'  #file2 is test data. (01.10.2018-17.10.2018)

#read excel files
df1 = pd.read_excel(fileName1,index_col=0)
df2 = pd.read_excel(fileName2,index_col=0)

numRows = df1.shape[0]
numColumns = df1.shape[1]

numRowstest=df2.shape[0]
numColumnstest=df2.shape[1]

##fill NaN
df1=df1.fillna(0)
df2=df2.fillna(0)

##dateformat
df1['event_date']= pd.to_datetime(df1['event_date'], unit='s')
df2['event_date']= pd.to_datetime(df2['event_date'], unit='s')

df1['year'] = df1['event_date'].dt.year
df1['month'] = df1['event_date'].dt.month
df1['day'] = df1['event_date'].dt.day
df1['hour'] = df1['event_date'].dt.hour

df2['year'] = df2['event_date'].dt.year
df2['month'] = df2['event_date'].dt.month
df2['day'] = df2['event_date'].dt.day
df2['hour'] = df2['event_date'].dt.hour


#Features
df1['viewer_marital_status']= df1['viewer_marital_status'].apply(lambda x: 2 if x == 'Evli' else(1 if x == 'Bekar'  else 0))
df2['viewer_marital_status']= df2['viewer_marital_status'].apply(lambda x: 2 if x == 'Evli' else(1 if x == 'Bekar'  else 0))

df1['viewer_gender']= df1['viewer_gender'].apply(lambda x: 2 if x == 'E' else(1 if x == 'K'  else 0))
df2['viewer_gender']= df2['viewer_gender'].apply(lambda x: 2 if x == 'E' else(1 if x == 'K'  else 0))

df1['event_type']= df1['event_type'].apply(lambda x: 1 if x == 'CLICK' else 0)
df2['event_type']= df2['event_type'].apply(lambda x: 1 if x == 'CLICK' else 0)

df1['viewer_job']= df1['viewer_job'].apply(lambda x: 2 if x == 'Evli' else(1 if x == 'Bekar'  else 0))
df2['viewer_job']= df2['viewer_job'].apply(lambda x: 2 if x == 'Evli' else(1 if x == 'Bekar'  else 0))

def func1(row):
    if row['viewer_job'] == 'Serbest Meslek':
        return 6
    elif row['viewer_job'] =='Özel Sektör':
        return 5
    elif row['viewer_job'] =='Öğrenci':
        return 4
    elif row['viewer_job'] =='Kamu Çalışanı':
        return 3
    elif row['viewer_job'] =='Emekli':
        return 2
    elif row['viewer_job'] =='Çiftçi':
        return 1
    else:
        return 0

df1['viewer_job'] = df1.apply(func1, axis=1)
df2['viewer_job'] = df2.apply(func1, axis=1)

def func2(row):
    if row['viewer_education'] == 'Yüksek Lisans / Doktora':
        return 5
    elif row['viewer_education'] =='Üniversite':
        return 4
    elif row['viewer_education'] =='Lise':
        return 3
    elif row['viewer_education'] =='Ortaokul':
        return 2
    elif row['viewer_education'] =='İlkokul':
        return 1
    else:
        return 0

df1['viewer_education'] = df1.apply(func2, axis=1)
df2['viewer_education'] = df2.apply(func2, axis=1)

def func3(row):
    if row['event_category'] == 'Yedek Parça, Aksesuar, Donanım & Tuning':
        return 4
    elif row['event_category'] =='Emlak':
        return 3
    elif row['event_category'] =='İş Makineleri & Sanayi':
        return 2
    elif row['event_category'] =='İkinci El ve Sıfır Alışveriş':
        return 1
    else:
        return 0

df1['event_category'] = df1.apply(func3, axis=1)
df2['event_category'] = df2.apply(func3, axis=1)


##trainingSetLabels, trainingSet created
trainingSetLabels = df1.ix[:, (df1.shape[1] - 1):]
trainingSet = df1.drop(['ad_daily_budget_kurus'], axis=1) # drop ad_daily_budget_kurus because of prediction
trainingSet = df1.drop(['event_date'], axis=1)


##testSetLabels, testSet is created
testSetLabels = df2.ix[:, (df2.shape[1] - 1):]
testSet = df2.drop(['ad_daily_budget_kurus'], axis=1)
testSet = df2.drop(['event_date'], axis=1)

#numpy array is created for prediction
trainingSetLabels = np.array(trainingSetLabels.values)
testSetLabels = np.array(testSetLabels.values)

#classifier is created using LinearRegression
classifier = linear_model.LinearRegression()
predictionModel = classifier.fit(trainingSet, trainingSetLabels)


eval = mean_squared_error(testSetLabels, predictionModel.predict(testSet))
print(classifier)
print('prediction model (test on training set):\n',predictionModel)
print('evaluation - test on training set- mean squared error:\n',eval)


