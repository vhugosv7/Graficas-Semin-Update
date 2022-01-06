import matplotlib.pyplot as plt#Librerias necesarias para generar la grafica


#Ruta de los archivos seleccionados 
#Sistema/Timsa/Pacientes atendidos con estudio/particulares/Imagenologia/liquidados
# Pacientes atendidos con estudio particulares imagenologia liquidados

#Generamos la figura 
fig, ax = plt.subplots()

#Lista de datos para el eje x
meses = ['0','Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']

#Diccionario para el eje y
Atendidos = {'LabLiqui':[0,1965468.52,1816583.25,1765847.96,1508578.79,1503771.37,1404868.43,1655010.39,1812095.03,1454188.08,611107.27,1271001.97,1147530.29]}

#Generamos la grafica con los datos previamente defenidos
ax.plot(meses, Atendidos['LabLiqui'], marker = 'o', color = 'tab:orange' ,ms = 10, mec = 'y')

#Tipo de fuente
font1 = {'family':'serif','color':'black','size':12}
font2 = {'family':'serif','color':'black','size':12}

#Etiquetas para x y
plt.xlabel("Meses ", fontdict = font2)
plt.ylabel("Cantidad", fontdict = font2)
#Cuadricula para la grafica
plt.grid()
#Guardamos la grafica como imagen
plt.savefig("3Pacientes atendidos con estudio particulares imagenologia liquidados")
#Mostramos la gráfica
plt.show()
