
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu
import seaborn as sns
from matplotlib_venn import venn2
df = pd.read_csv(r'C:\Users\madhuri\Desktop\letsupgrade\Statistics_dinesh\general_data.csv')

'''stats,p = pearsonr(df.Attrition,df.MonthlyIncome)
print(stats,p)
stats,p = pearsonr(df.Attrition,df.MonthlyIncome)
stats,p = pearsonr(df.Attrition,df.MonthlyIncome)
stats,p = pearsonr(df.Attrition,df.MonthlyIncome)
print(df.corr())'''

yes_ds = df[df['Attrition'] == 'Yes']
no_ds = df[df['Attrition'] == 'No']
yes_ds['Attrition'] = yes_ds['Attrition'].replace('Yes',1)
no_ds['Attrition'] = no_ds['Attrition'].replace('No',0)
print(yes_ds)
print(no_ds)
#plt.bar(yes_ds['Department'],yes_ds.groupby('Department').count())
sns.countplot(yes_ds['Department'])
sns.countplot(no_ds['Department'])
sns.countplot(yes_ds['EducationField'])
sns.countplot(no_ds['EducationField'])
s = yes_ds['Department'].value_counts()
s.plot.bar()

venn2(subsets = (yes_ds['Attrition'],yes_ds['DistanceFromHome']))
