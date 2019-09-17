
import pandas as pd
import pylab

excel=pd.read_csv("C:\\Users\\Jacek\\git_agata\\kata_zadanka\\excel_pandas\\iris.csv")
print (excel.head())

print (excel)


x=excel.iloc[2,:-1].tolist()
print (x)



y=excel.columns[:-1].tolist()
print (y)




pylab.bar(y,x)
pylab.show()