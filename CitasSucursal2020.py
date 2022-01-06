import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("CitaSucursal-2021-12-07.xlsx")#Cargar archivo de Citas
#Definicion de Arreglos
arreglo = np.array([])
estudios = np.array([])


size= df.shape[0] #Tamaño del DataFrame
count = 1


#Bucle para recorrer las filas de la columna fecha 
while (count < size ):
    count = count + 1
    #Guardando fechas dentro  del array
    arreglo = np.append(arreglo,[hoja.cell(row=count, column=2).value])

#Agregar citas dentro de un archivo txt
with open('fileCitas20.txt', 'w') as citasv:
    for item in arreglo:
        citasv.write("%s\n" % item)

#Guardamos las fechas dentro de una lista
with open('fileCitas20.txt','r') as stop_words: 
    lineas = [linea.strip() for linea in stop_words]


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
print("Junio",jun20)

jul20='2020-07'
jul20=sum(jul20 in string for string in lineas)
print("Julio: ",jul20)

ago20='2020-08'
ago20=sum(ago20 in string for string in lineas)
print("Agosto: ",ago20)

sep20='2020-09'
sep20=sum(sep20 in string for string in lineas)
print("Septiembre: ",sep20)

oct20='2020-10'
oct20=sum(oct20 in string for string in lineas)
print("Octubre: ",oct20)

nov20='2020-11'
nov20=sum(nov20 in string for string in lineas)
print("Noviembre: ",nov20)


dic20='2020-12'
dic20=sum(dic20 in string for string in lineas)
print("Diciembre: ",dic20)


## Declaramos valores para el eje x
eje_x = ['Ene', 'Feb', 'Mar', 'Abr','May', 'Jun', 'Jul', 'Ago','Sep', 'Oct','Nov','Dic']

## Declaramos valores para el eje y

rects1 = [ene20,feb20,mar20,abr20,may20,jun20,jul20,ago20,sep20,oct20,nov20,dic20]

## Creamos Gráfica
plt.bar(eje_x, rects1, color="orange")
 
## Etiqueta en el eje y
plt.ylabel('Cantidad de citas 2020')
 
## Etiqueta en el eje x
plt.xlabel('Meses')
 
## Título de Gráfica
plt.title('Citas en sucursal 2020')
 
## Mostramos Gráfica
plt.show()

#Guardamos la grafica
plt.savefig("Citas en sucursal 2020.png", bbox_inches='tight')



