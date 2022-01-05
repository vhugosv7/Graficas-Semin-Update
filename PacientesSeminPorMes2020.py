from openpyxl import load_workbook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel("Paciente-2021-12-07.xlsx")#Cargar archivo Pacientes
arreglo = np.array([])

size= df.shape[0] #Obtenemos el tamaño del archivo
count = 1 #contador para recorrer los elementos 

while (count < size ):
    count = count + 1
    #añadimos las fechas del Excel dentro de un array
    arreglo = np.append(arreglo,[hoja.cell(row=count, column=32).value])


#Guardamos las fechas obtenidas en un documento txt
with open('file2020.txt', 'w') as fecha2020:
    for item in arreglo:
        fecha2020.write("%s\n" % item)

#Abrimos el archivo que contiene las fechas y guardamos las fechas en una lista
with open('file2020.txt','r') as fechas: 
    lineas = [linea.strip() for linea in fechas]


print("Pacientes por mes 2020\n")
#Sumamos todas las veces que se repita la fecha requerida
ene20='2020-01'
ene20=sum(ene20 in string for string in lineas)
print("Enero: ",ene20)

feb20='2020-02'
feb20=sum(feb20 in string for string in lineas)
print("Febrero: ",feb20)

mar20='2020-03'
mar20=sum(mar20 in string for string in lineas)
print("Marzo: ",mar20)

abr20='2020-04'
abr20=sum(abr20 in string for string in lineas)
print("Abril: ",abr20)

may20='2020-05'
may20=sum(may20 in string for string in lineas)
print("Mayo: ",may20)


jun20='2020-06'
jun20=sum(jun20 in string for string in lineas)
print("Junio: ",jun20)

jul20='2020-07'
jul20=sum(jul20 in string for string in lineas)
print("Julio: ",jul20)

ago20='2020-08'
ago20=sum(ago20 in string for string in lineas)
print("Agosto",ago20)

sep20='2020-09'
sep20=sum(sep20 in string for string in lineas)
print("Septiembre",sep20)

oct20='2020-10'
oct20=sum(oct20 in string for string in lineas)
print("Octubre",oct20)

nov20='2020-11'
nov20=sum(nov20 in string for string in lineas)
print("Noviembre",nov20)

dic20 ='2020-12' #lineas son las lineas del file2020.txt que tienen la fecha
dic20=sum(dic20 in string for string in lineas)
print("Diciembre",dic20)

#-------------------------------------------------------------------------


## Declaramos valores para el eje x
eje_x = ['Ene', 'Feb', 'Mar', 'Abr','May', 'Jun', 'Jul', 'Ago','Sep', 'Oct','Nov','Dic']
## Declaramos valores para el eje y
rects1 = [ene20,feb20,mar20,abr20,may20,jun20,jul20,ago20,sep20,oct20,nov20,dic20]

## Creamos Gráfica
plt.bar(eje_x, rects1,color="red")
 
## Titulo para el eje y
plt.ylabel('Cantidad de usuarios')
 
## Titulo para el eje x
plt.xlabel('Meses')
 
## Título de Gráfica
plt.title('Pacientes en Semin por mes 2020')
 
## Mostramos Gráfica
# plt.show()
plt.savefig('Pacientes Semin por mes 2020')


