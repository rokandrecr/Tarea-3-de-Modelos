import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import norm 
from mpl_toolkits.mplot3d import Axes3D
 

"""Leo el documento y guardo la suma de las filas en un arreglo fX y el de las columnas en fY"""
va=pd.read_csv("xy.csv")
d= va.to_numpy()
matriz = np.array(d).astype("float")

fX = np.sum(matriz, axis=1)
fY = np.sum(matriz, axis=0)


x=[5, 6, 7, 8, 9, 10, 11, 12, 13, 14,15]
y=[5, 6, 7, 8, 9, 10, 11, 12, 13, 14,15,16,17,18,19,20,21,22,23,24,25]




"""Defino la función gaussiana"""
def gaussiana(k,mu,sigma):
  return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp(-(k-mu)**2/(2*sigma**2))
param, _ = curve_fit(gaussiana,x,fX)
print(param)

hx= norm.pdf(x, param[0], param[1] )
parametro, _ = curve_fit(gaussiana,y,fY)
hy= norm.pdf(y, parametro[0], parametro[1] )
print(parametro)
"""Parte 3"""




"""Parte de la grafica en 3D
Leo los datos del xyp"""

xyp=pd.read_csv("xyp.csv")
d2= xyp.to_numpy()
m_xyp = np.array(d2).astype("float")

"""Guardo los datos de cada columna en X,Y yP"""
X= m_xyp[:,0]
Y= m_xyp[:,1]
P= m_xyp[:,2]

"""Calculo la correlación y la covarianza"""
correlacion=0
i=0
for i in range(len(X)):
  if i==0:
    i=i+1
  else:
    promedio=P[i]
    vectorxs=X[i]
    vectorys=Y[i]
    correlacion += promedio*vectorxs*vectorys

print ("la correlacion es",correlacion)
covarianza=0
i=0
for i in range(len(X)):
  if i==0:
    i=i+1
  else:
    promedio=P[i]
    vectorxs=X[i]
    vectorys=Y[i]
    covarianza -= promedio*(vectorxs-param[0])*(vectorys-parametro[0])
print("La covarianza es: ", covarianza)



p= covarianza/(param[1]*parametro[1])
print("El coeficiente de correlación es:", p)



"""Grafico las funciones de Densidad de X y Y(Parte 4)"""
plt.plot(x, fX, 'ro')

plt.savefig("fX.png")
plt.close()

plt.plot(y, fY, 'ro')

plt.savefig("fY.png")
plt.close()


"""Hago la gráfica en 3D"""

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(X, Y, P, zdir='z', s=20, cmap="Greens")
plt.savefig("3D.png")
plt.close()
