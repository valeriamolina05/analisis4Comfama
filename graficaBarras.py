
import matplotlib.pyplot as plt

años=[2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
consumidores=[4000,10000,8000,4500, 4000, 5000,4800, 12000, 14000,10000]
colores=["#DE76BD", "#C076DE", "#7C76DE", "#76D3DE", "#76DE8C", "#DE7676", "#DFEB27", "#C427EB", "#252125", "#1E4AA9"]

plt.bar(años, consumidores, color=colores)
plt.xlabel("Años")
plt.ylabel("Consumidores")
plt.title("Consumo de drogas Medellín")
plt.show()