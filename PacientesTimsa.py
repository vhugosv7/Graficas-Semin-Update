import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Librerias a utilizar

df = pd.read_excel('pacientes-1-171805.xlsx')#Cargar archivo de pacientes
# 
hombre =df['Sexo'] == "Masculino" #seleccion especifica de columna sexo
hmostar=df[hombre] #mostrar datos masculino

mujer =df['Sexo'] == "Femenino"#seleccion especifica de columna sexo
mmostrar=df[mujer]#mostrar datos femenino

eje=hmostar.shape[0] 
eje2=mmostrar.shape[0]
#Cantidad de datos en el dataFrame

timsap = ['Pacientes Timsa'] #Titulo eje x
hombreg = [eje]
mujeresg = [eje2] 
#Asignamos valores de la cantidad de hombres y mujeres encontrados

#Obtenemos la posicion de cada etiqueta en el eje de X
x = np.arange(len(timsap))
#tamaño de cada barra
width = 0.35

#Dibujamos la grafica
fig, ax = plt.subplots()

#Generamos las barras para el conjunto de hombres
rects1 = ax.bar(x - width/2, hombreg, width, label='Hombres',color="yellow")
#Generamos las barras para el conjunto de mujeres
rects2 = ax.bar(x + width/2, mujeresg, width, label='Mujeres')

#Añadimos las etiquetas de identificacion de valores en el grafico
ax.set_ylabel('Numero de pacientes')
ax.set_title('Pacientes')
ax.set_xticks(x)
ax.set_xticklabels(timsap)

#Añadimos un legend() esto permite mmostrar con colores a que pertence cada valor.
ax.legend()

def autolabel(rects):
    """Funcion para agregar una etiqueta con el valor en cada barra"""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # posicion de la etiqueta de valores
                    textcoords="offset points",
                    ha='center', va='bottom')

#Añadimos las etiquetas para cada barra
autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.savefig('Timsa pacientes.png') #Guardamos el archivo con el metodo savegif
#Mostramos la grafica con el metodo show()
plt.show()

#Funcion para calcular el porcentaje de hombres y mujeres
def percentage(part, whole):
  return round(100 * float(part)/float(whole),2)

#Mostramos los totales
print("Total: ",eje+eje2)
print("Hombres" ,percentage(eje,eje+eje2),"%")
print("Mujeres", percentage(eje2,eje+eje2),"%")