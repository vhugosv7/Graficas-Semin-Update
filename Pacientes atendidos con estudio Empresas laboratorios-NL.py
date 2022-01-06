import matplotlib.pyplot as plt
#Libreria a utilizar

#Figura para la grafica
fig, ax = plt.subplots()
print("Empresas laboratorios NO liquidados ")

#Lista de datos para el eje x
meses = ['0','Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']

#Diccionario de datos para el eje y
Atendidos = {'EImaLiqui':[0,426791.99,351991.95,202977.96,201318.95,225953.89,746844.53,710605.71,602217.41,451783.25,177390.82,418589.12,532702.14]}

font1 = {'family':'serif','color':'black','size':12}
font2 = {'family':'serif','color':'black','size':12}

#Etiquetas para los ejes x y
plt.xlabel("Meses ", fontdict = font2)
plt.ylabel("Cantidad", fontdict = font2)

#Generamos la grafica con los datos previamente establecidos
ax.plot(meses, Atendidos['EImaLiqui'], marker = 'o', color = 'tab:green')
#Cuadricula para grafica
plt.grid()
#Guardamos la grafica como imagen
plt.savefig("9Pacientes atendidos con estudio empresas laboratorios NO liquidados")
#Mostramos la grafica 
plt.show()