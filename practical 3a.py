import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
df = pd.read_csv(r'C:\Users\kc140\OneDrive\Desktop\d.s\wine.csv',header=None,skiprows=1, usecols= [0, 
1,2]) 
df.columns=['Class label', 'Alcohol','Malic Acid'] 
print(df)


from sklearn.preprocessing import MinMaxScaler 
scaling=MinMaxScaler() 
scaling.fit_transform(df[['Alcohol', 'Malic Acid']])

from sklearn.preprocessing import StandardScaler 
scaling.fit_transform(df[['Alcohol' , 'Malic Acid']]) 
