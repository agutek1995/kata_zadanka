
import pandas as pd
import pylab

excel=pd.read_csv("C:\\Users\\Jacek\\git_agata\\kata_zadanka\\excel_pandas\\iris.csv")

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





