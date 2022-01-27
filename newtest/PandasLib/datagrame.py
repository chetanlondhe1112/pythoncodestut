#dataframe creation
import pandas as pd

data={'animal':['cat','cat','snake','dog','dog','cat','snake','cat','dog','dog'],
      'age':[2.5,3,4,6,5,2,4,6,2,4]
}
labels=['a','b','c','d','e','f','j','k','l','m']
df2=pd.DataFrame(data,index=labels)
print(df2)