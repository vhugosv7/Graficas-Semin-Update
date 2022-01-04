import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Librerias que se van a utilizar 


df = pd.read_excel("SeminPaciente-2021-12-07.xlsx")#Cargamos el archivo de pacientes


hombre =df['sexo'] == "masculino" #DataFrame de la columna sexo seleccionando solo masculino
hmostar=df[hombre] #mostrar datos de DataFrame masculino

mujer =df['sexo'] == "femenino" #DataFrame de la columna sexo seleccionando solo femenino
mmostrar=df[mujer]#mostrar datos de DataFrame femenino


eje=hmostar.shape[0] #Forma del dataFrame masculino
eje2=mmostrar.shape[0]#Forma del dataFrame femenino

seminp = ['Pacientes Semin digital'] #titulo
hombreg = [eje]
mujeresg = [eje2]

#Obtenemos la posicion de cada etiqueta en el eje de X
x = np.arange(len(seminp))
#tamaño de cada barra
width = 0.35

fig, ax = plt.subplots()

#Generamos las barras para el conjunto de hombres
rects1 = ax.bar(x - width/2, hombreg, width, label='Hombres')
#Generamos las barras para el conjunto de mujeres
rects2 = ax.bar(x + width/2, mujeresg, width, label='Mujeres')

#Añadimos las etiquetas de identificacion de valores en el grafico
ax.set_ylabel('Numero de pacientes')
ax.set_title('Pacientes')
ax.set_xticks(x)
ax.set_xticklabels(seminp)

#Añadimos un legen(),esto permite mmostrar con colores a que pertence cada valor.
ax.legend()

def autolabel(rects):
    """Funcion para agregar una etiqueta con el valor en cada barra"""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom')#Posicion de las etiquetas de las barras

#Añadimos las etiquetas para cada barra
autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
#Guardamos la grafica con el metodo savegif
plt.savefig('doble_barra.png')
#Mostramos la grafica con el metodo show()
plt.show()

#Mostramos el porcentaje de los pacientes
def percentage(part, whole):
  return round(100 * float(part)/float(whole),2)

print("Total: ",eje+eje2) #Total de pacientes
print("Hombres" ,percentage(eje,eje+eje2),"%") #Total de hombres
print("Mujeres", percentage(eje2,eje+eje2),"%") #Total de mujeres