#Librerias necesarias para realizar la grafica
import matplotlib.pyplot as plt

#Ruta de los archivos seleccionados 
#Sistema/Timsa/Pacientes atendidos con estudio/particulares/laboratorios/liquidados

# Pacientes atendidos con estudio particulares laboratorios no liquidados

#Generamos la figura
fig, ax = plt.subplots()
#Lista de datos para el eje x
meses = ['0','Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']

#Diccionario para el eje y
Atendidos = {'LabnoLiqui':[0,3622097.15,1838507.85,3361345.05,2437922.95,2142343.03,1939008.62,2490543.28,2838520.50,2308802.66,1012296.42,1724673.24,1385690.64]}
      
#Generamos la grafica con los datos previamente definidos
ax.plot(meses, Atendidos['LabnoLiqui'], marker = 'o', color = 'tab:blue' ,ms = 10, mec = 'y')

#Tipo de fuente para los textos de la grafica
font1 = {'family':'serif','color':'black','size':12}
font2 = {'family':'serif','color':'black','size':12}
#Etiquetas de texto para los ejes x y
plt.xlabel("Meses ", fontdict = font2)
plt.ylabel("Cantidad", fontdict = font2)
#Cuadricula para la grafica
plt.grid()
#Guardamos la grafica como una imagen
plt.savefig("2Pacientes atendidos con estudio particulares laboratorios no liquidados")
#Mostramos la grafica con la ayuda del metodo show
plt.show()

