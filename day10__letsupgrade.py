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
print(df[['Age','DistanceFromHome','MonthlyIncome','PercentSalaryHike','JobLevel','TotalWorkingYears']].IQR())
#plt.scatter(df['EmployeeID'],df['MonthlyIncome'])
#plt.boxplot(df['MonthlyIncome'])
#plt.boxplot(df['Age'])
plt.hist(df['Age'])

''' My Inference:
Dataset is not normally distributed
As there are no outliers in Age of people in the company, Company in having all set of experienced people in equal proportion
Most of the people are getting higher salary as kurtosis for monthly income is positive'''



  


