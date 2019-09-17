
import pandas as pd
import pylab

excel=pd.read_csv("C:\\Users\\Jacek\\git_agata\\kata_zadanka\\excel_pandas\\iris.csv")

# excel = excel.head(53).tail(5)

# print(excel["Species"])
# true_false = excel["Species"] == "setosa"
# print(true_false)
# print(excel.loc[49:51, :])
# print(excel.loc[true_false, :])

excel=excel.loc[excel["Species"] == "setosa", ]
def wylicz_srednia(lista):
    suma=0
    for i in lista:
        suma=suma+i
    srednia=suma/(len(lista))
    return srednia
print(wylicz_srednia(excel['Sepal.Length'].tolist()))
lista_columns=[]
lista_srednich=[]
for i in excel.columns[:-1]:
    srednia=wylicz_srednia(excel[i])
    lista_columns.append(i)
    lista_srednich.append(srednia)
print (lista_srednich)
print (lista_columns)

pylab.bar(lista_columns,lista_srednich)
pylab.show()

print(excel.loc[excel["Species"] == "setosa", ])