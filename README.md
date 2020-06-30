# Tarea-3-de-Modelos
Tarea 3 de Modelos probabilisticos de señales y sistemas. 
Roger Castro
B61725
Grupo: 02

1. Se calculan los valores de fX(x) y fy(Y), para luego graficarlos y observar una distribución simular a la distribución Gaussiana por lo que se crea una función Gaussiana para calcular los paramétros de esta.Esto fue realizado por medio del comando curvefit y se hizo para cada variable aleatoria guardando los parametros en un vector correspondiente a paramX y paramY. Las entradas de este vector son el mu y el sigma para las funciones correspondientes

La media para X tuvo un valor de 9.904843810018251 y la varianza de 3.2994428643069567.
La media para Y tuvo un valor de 15.079460901084733 y la varianza de 6.0269377486808775.

Por esta razón estos valores representan los valores correspondientes a la curva de mejor ajuste para la función de densidad marginal correspondiente a cada variable aleatoria como una función normal 

2. Se puede deducir analíticamente que la condición de independencia de las probabilidades de las variables aleatorias X y Y genera que la función de densidad conjunta de las dos funciones sea la multiplicación de estas. Por lo que la expresión sería:
                                                                  fXY(x,y) = fX(x)* fY(y)

3. Los datos obtenidos serían los siguientes
Rxy = 149.4773100000001 
Cxy = 0.11760503547873213 
p = 0.005914099124709811
La correlación (Rxy) explica el grado en el cual dos o más cantidades están linealmente asociadas, por lo cual se observa que tiene una correlación bastante alta. No obstante es importante entender que correlación no significa casualidad por lo que en este caso se observa como la covarianza(Cxy) tiene un valor bastante cercano a 0 y el valor del coeficiente de correlación(p) también por lo que se deduce que las variables son independientes entre sí. Esta condición de independencia ya se sabía en el Punto 2 y estos parametros obtenidos en este punto demuestra la independencia entre las 2 variables aleatorias

4.En el archivo fX.png y el archivo fY.png muestran las gráficas de las funciones de densidad marginales para las variables aleatorias de X y Y correspondientemente. En estas se pueden observar el comportamiento hacia una tendencia de distribución gaussiana. 
En el archivo 3D.png se guarda la gráfica en 3 dimensiones en donde se observa que los puntos de la función de densidad marginales generan una Campana Gaussiana. Esta función solo confirma la tendencia que anteriormente se había calcado y plasmado.
