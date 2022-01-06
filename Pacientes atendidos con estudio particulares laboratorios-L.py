#Librerias necesarias
import matplotlib.pyplot as plt

#Ruta de los archivos seleccionados 
#Sistema/Timsa/Pacientes atendidos con estudio/particulares/laboratorios/liquidados

# Pacientes atendidos con estudio particulares laboratorios liquidados

#Generamos la figura
fig, ax = plt.subplots()
#Datos para el eje x
meses = ['0','Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']

#Datos para el eje y dentro de un diccionario
Atendidos = {'LabLiqui':[0,3267753.77,3427479.87,3294230.13,2468707.51,2009193.04,1820915.67,2437373.67,2918931.00,2272233.22,988740.99,1687725.26,1361148.82]}

#Dibujamos la grafica
ax.plot(meses, Atendidos['LabLiqui'], marker = 'o', color = 'tab:green' ,ms = 10, mec = 'y')
#Variables para cambiar el tipo de fuente de las grafica
font1 = {'family':'serif','color':'black','size':12}
font2 = {'family':'serif','color':'black','size':12}

#Asiganmos etiquetas para los ejes x y
plt.xlabel("Meses ", fontdict = font2)
plt.ylabel("Cantidad", fontdict = font2)
#Dibujamos una cuadricula para la grafica
plt.grid()
#Guardamos la grafica como un archivo de imagen
plt.savefig("1Pacientes atendidos con estudio particulares laboratorios liquidados")