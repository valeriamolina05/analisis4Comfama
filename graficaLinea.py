#importando libreria

import matplotlib.pyplot as plt 

#1. TENER UNA FUENTE DE DATOS 
barrios=["Calasanz", "Castilla", "Laureles", "Belen", "Robledo", "Boston", "Buenos Aires", "Manrique", "Estadio", "Blanquizal"]
poblacion=[12000, 25000, 40000, 100000,200000, 50000, 60000,250000,10000, 5000]

barrios3=["Calasanz", "Castilla", "Laureles", "Belen", "Robledo", "Boston", "Buenos Aires", "Manrique", "Estadio", "Blanquizal"]
poblacion3=[13000, 26000, 41000, 110000,210000, 6000, 61000,251000,10000, 5000]

barriosBello=["La Cumbre", "Santa Ana ", "Niquia", "Bellavista", "Paris", "Camacol", "Cabañas", "Barrio Obrero", "Navarra", "Pacheli"]
poblacionBello=[30000, 12000, 100000, 50000,25000, 3000, 5500,4850,10000, 5000]

#2. PROCEDO A UTILIZAR EL MATPLOTLIB PARA GENERAR LA GRAFICA
#plt.plot(barrios, poblacion)

#3. MODIFICAMOS LA GRAFICA
plt.plot(barrios, poblacion, marker="o", linestyle="--", color="b")
plt.plot(barrios3, poblacion3, marker="4", linestyle="-.", color="r")

plt.xlabel("Barrios de Medellín")
plt.ylabel("Población")
plt.title("Densidad de población Medellín 2023")

plt.savefig("linea.png")

plt.show()


