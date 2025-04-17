import pandas as pd
d = pd.read_csv(r'C:\Users\kc140\OneDrive\Desktop\d.s\Titanic.csv')
df = pd.DataFrame(d)
print(df)


df.loc[df['Age']<20]


df.loc[(df['Age']<20)&(df['SibSp']==0)]


