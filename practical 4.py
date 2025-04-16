import pandas as pd 
import numpy as np 
import seaborn as sb 
import matplotlib.pyplot as plt 
import warnings 
from scipy import stats 
 
# Ignore warnings 
warnings.filterwarnings('ignore') 
 
# Load the dataset 
df = sb.load_dataset('mpg') 
print(df.head())




df['horsepower'].describe() 
print(df['horsepower'].describe())


df['model_year'].describe() 
print(df['model_year'].describe())


bins = [0, 75, 150, 240] 
df['horsepower_new'] = pd.cut(df['horsepower'], bins=bins, 
labels=['l', 'm', 'h']) 
print(df['horsepower_new'])


ybins = [69, 72, 74, 84] 
labels = ['t1', 't2', 't3'] 
df['modelyear_new'] = pd.cut(df['model_year'], bins=ybins, 
labels=labels) 
print(df['modelyear_new'])

df_chi = pd.crosstab(df['horsepower_new'], 
df['modelyear_new']) 
print(df_chi)


chi2_stat, p_val, dof, expected = stats.chi2_contingency(df_chi) 
print(f"Chi2 Statistic: {chi2_stat}, P-value: {p_val}, Degrees of Freedom: {dof}") 
print("Expected Frequencies Table:\n", expected)
