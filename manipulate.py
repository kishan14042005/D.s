import pandas as pd
import numpy as np
iris=pd.read_csv(r'C:\Users\kc140\OneDrive\Desktop\d.s\iris.csv')
print(iris['sepal_length'])


print(iris['sepal_length']*2)


print(iris['sepal_length'] == 2)

print(iris['species']=='Iris-setosa')



groups =iris.groupby('species')
groups.get_group('Iris-setosa')
