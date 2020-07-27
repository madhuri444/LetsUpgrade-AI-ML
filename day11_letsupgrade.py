import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew

df = pd.read_csv(r'C:\Users\madhuri\Desktop\letsupgrade\Dinesh_sir\general_data.csv')
print(df.head())
df.duplicated()
df.drop_duplicates(inplace = True)
df.dropna(inplace = True)
print(df[['Age','DistanceFromHome','MonthlyIncome','PercentSalaryHike','JobLevel','TotalWorkingYears']].mean())
print(df[['Age','DistanceFromHome','MonthlyIncome','PercentSalaryHike','JobLevel','TotalWorkingYears']].median())
print(df[['Age','DistanceFromHome','MonthlyIncome','PercentSalaryHike','JobLevel','TotalWorkingYears']].mode())
print(df[['Age','DistanceFromHome','MonthlyIncome','PercentSalaryHike','JobLevel','TotalWorkingYears']].skew())
print(df[['Age','DistanceFromHome','MonthlyIncome','PercentSalaryHike','JobLevel','TotalWorkingYears']].kurt())
print(df[['Age','DistanceFromHome','MonthlyIncome','PercentSalaryHike','JobLevel','TotalWorkingYears']].var())
print(df[['Age','DistanceFromHome','MonthlyIncome','PercentSalaryHike','JobLevel','TotalWorkingYears']].std())

df['Attrition'] = df['Attrition'].replace('Yes',1)
df['Attrition'] = df['Attrition'].replace('No',0)
#plt.scatter(df['EmployeeID'],df['MonthlyIncome'])
#plt.boxplot(df['MonthlyIncome'])
df_new = df[df['Attrition'] == 'Yes']
print(df_new)
#plt.boxplot(df_new['TotalWorkingYears'])
#print(df_new['TotalWorkingYears'].mode())
plt.bar(df_new['JobRole'])

''' My Inference:
Dataset is not normally distributed
As there are no outliers in Age of people in the company, Company in having all set of experienced people in equal proportion
Top most positioned people are getting higher salary as kurtosis for monthly income is positive
People having 20- 40 years majorly left the company '''

