import pandas as pd 
a = '[[["fruit", "Apple"],["size","Large"],["color","Red"]]]' 
data = pd.DataFrame({key:val for val,key in eval(a)[0]},index=[0]) 
print(data)
