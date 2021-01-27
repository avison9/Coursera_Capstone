# This notebook is to carry out the Captsone projects (Battle of Neigbourhoods) from the IBM Data Science Specialist course, via Coursera!!!

import pandas as pd
import numpy as np

print('Hello Capstone Project Course!')
a =13
b = 11
c = 12
d = 15
e = 16
f = 99
g = 24
h = 3
i = 9
lis = {
	'Jaccard':[a,b,c,d],
	'fi score':['16','33','NA','77'],
	'plu':['11','244','54','NA']
}
index = ['knn','DT','SVM','Poly']
df =pd.DataFrame(lis, index= index)
print(df)