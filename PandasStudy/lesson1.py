import pandas as pd

df=pd.DataFrame({'ID':[1,2,3],'Name':['Alice','Bob','Charlie']})
df=df.set_index('ID')
df.to_excel('lesson1.xlsx')

print type(df)