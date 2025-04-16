import pandas as pd 
iris = pd.read_csv(r'C:\Users\kc140\OneDrive\Desktop\d.s\iris.csv') 
iris.head()


from sklearn.preprocessing import LabelEncoder 
le =LabelEncoder() 
iris['Code']=le.fit_transform(iris.species) 
iris.head()

iris.tail() 
