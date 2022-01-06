import matplotlib.pyplot as plt
#Librerias a utilizar

#Figura para crear la grafica 
fig, ax = plt.subplots()

print("Empresas Imagenologia NO liquidados ")

#Lista de datod para el eje x
meses = ['0','Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']

#Diccionario de datos para el eje y
Atendidos = {'EImanoLiqui':[0,35704.40,50760.80,57370.29,106036.36,54758.83,270350.56,207549.98,440836.16,464067.79,126712.61,572827.00,446301.53]}

font1 = {'family':'serif','color':'black','size':12}
font2 = {'family':'serif','color':'black','size':12}

#Etiquetas para la grafica en ejes x y
plt.xlabel("Meses ", fontdict = font2)
plt.ylabel("Cantidad", fontdict = font2)
#Generamos la grafica
ax.plot(meses, Atendidos['EImanoLiqui'], marker = 'o', color = 'tab:red')
#Cuadricula para la grafica
plt.grid()
#Guardamos la grafica como imagen
plt.savefig("7Pacientes atendidos con estudio empresas imagenologia NO liquidados")
#Mostramos la grafica generada
plt.show()