import pandas as pd

excel=pd.read_excel("C:\\Users\\Jacek\\Documents\\orkiestry.xlsx")
# print (excel)
#
# print (excel.columns)
#
# print (excel["cena"])
# print (excel.loc[2, "cena"])
# print (excel.iloc[2, 1])
#
# print (excel.loc[2, :])
# print (excel.iloc[2, :])
#
# wiersz = excel.iloc[2, :]
# print(wiersz.tolist())
#
# print (excel[["cena", "czy_chcemy"]])

print (excel.columns)
print (excel.iloc[:2])

print (excel.iloc[2:4])

print (excel.iloc[:,:2])

print (excel.loc[:,['cena','komentarz']])
