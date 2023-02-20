import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt #Esta libreria crea graficos 2D y 3D
import scipy.stats as stats #libreria para implementar distribucion normal
import numpy as np
import os


#df = pd.read_excel("perros.xlsx") # leer el excel
#print(df) # toda la tabla
#print(df.loc[0, "raza"]) #chihuaha primera posicion de raza


#file = 'perros.xlsx'

flag = True

while flag:
    file = input("Ingrese el nombre del archivo: ")

    if not os.path.exists(file):
        print(f"El archivo {file} no existe.")
    else:
        if not file.endswith('.xlsx'):
            print("El archivo debe ser de tipo .xlsx")
        else:
            print("El archivo es válido.")
            flag = False


df = pd.read_excel(file)
print(df) # toda la tabla



edad = df['edad']; #Escoger sola la columna edad

#calcular media y desviacion estandar
mu = edad.mean()
sigma = edad.std() #raiz cuadrada de la varianza

min_value = edad.min()
max_value = edad.max()

print("min", min_value)
print("max", max_value)

x = np.linspace(min_value, max_value, 100) # crear grafica con suficiente resolución.
#Y ya para calcular la probabilidad de que la variable aleatoria caiga en los valores de x
y = stats.norm.pdf(x, mu, sigma) #pdf funcion de densidad  (valor variable aleatoria, media, y desviacion estandar)

plt.plot(x, y) #plot crea graficos de linea
#plt.hist(x, y)
plt.title('Distribucion normal de edades')
plt.xlabel('Edades X')
plt.ylabel('Probabilidad Y')
plt.show()

window = tk.Tk() #instancia de Tk, que representa la venta principal
window.title("Dogs")
window.geometry("600x500")
window.resizable(False, False) # No se puede hacer resizable

button = tk.Button(window, text="Button")
button.pack() #Mostrar boton en la ventana


window.mainloop() #Mostrar ventana y que el usuario interactue

