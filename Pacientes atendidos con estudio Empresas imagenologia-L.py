import matplotlib.pyplot as plt
#libreria a utilizar

#Figura para generar la grafica
fig, ax = plt.subplots()

print("Particulares Imagenologia liquidados ")
#Lista para el eje x
meses = ['0','Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']

#Diccionario de datos para el eje y
Atendidos = {'EImaLiqui':[0,9480.00,15545.60,12025.00,13090.00,15180.00,20479.00,24472.00,13627.00,27578.66,6380.00,17706.00,9872.00]}

font1 = {'family':'serif','color':'black','size':12}
font2 = {'family':'serif','color':'black','size':12}

#Etiquetas para eje x y
plt.xlabel("Meses ", fontdict = font2)
plt.ylabel("Cantidad", fontdict = font2)
#Generamos la grafica con color morado
ax.plot(meses, Atendidos['EImaLiqui'], marker = 'o', color = 'tab:purple')
#Cuadricula para la grafica
plt.grid()
#Guardamos la grafica como imagen
plt.savefig("6Pacientes atendidos con estudio empresas imagenologia liquidados")
#Mostramos en pantalla la grafica
plt.show()
