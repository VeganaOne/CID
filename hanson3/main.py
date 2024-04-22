from Datos import Datos
from RegresionLineal import RegresionLineal
from RegresionCuadratica import RegresionCuadratica
from RegresionCubica import RegresionCubica
from Calculos import Calculos
#Arreglo de datos para el Data Set
x = [108,115,106,97,95,91,97,83,83,78,54,67,56,53,61,115,81,78,30,45,99,32,25,28,90,89]
y  = [95,96,95,97,93,94,95,93,92,86,73,80,65,69,77,96,87,89,60,63,95,61,55,56,94,93]
#Ejemplo cuadratica
#x = [0,1,2,3]
#y = [1,3,2,0]
#Ejemplo de cubica
#x = [-2,-1,0,1,2]
#y = [3,0,2,4,4]
#Se RegresionCubicaea el objeto de Datos con los datos del arreglo
datos = Datos(x,y)
#RegresionCubicaeamos nuestra clase de RegresionLineal
lineal = RegresionLineal(datos.get_x(),datos.get_y())
cuadratica = RegresionCuadratica(x,y)
cubica = RegresionCubica(x,y)
cuadratica.imprimir_ecuacion()
cubica.imprimir_ecuacion()
print("Regresion Lineal")
lineal.imprimir_ecuacion()
print("3 datos conocidos: ")
print("#1 x = 108 y = ", lineal.predecir(108))
print("#2 x = 115 y = ", lineal.predecir(115))
print("#3 x = 106 y = ", lineal.predecir(106))
print("Predicciones de 3 datos:")
print("#1 X = 92, Y  = ", lineal.predecir(92))
print("#2 X = 40, Y  = ", lineal.predecir(40))
print("#3 X = 100, Y  = ", lineal.predecir(100))
print("Coeficiente de Correlacion: ", lineal.get_coeficiente_corelacion())
print("Coeficiente de Determinacion: ", lineal.get_coeficiente_determinacion())
print("**********************")
print("Regresion Cuadratica")
cuadratica.imprimir_ecuacion()
print("3 datos conocidos: ")
print("#1 x = 108 y = ", cuadratica.predecir(108))
print("#2 x = 115 y = ", cuadratica.predecir(115))
print("#3 x = 106 y = ", cuadratica.predecir(106))
print("Predicciones de 3 datos:")
print("#1 X = 92, Y  = ", cuadratica.predecir(92))
print("#2 X = 40, Y  = ", cuadratica.predecir(40))
print("#3 X = 100, Y  = ", cuadratica.predecir(100))
print("Coeficiente de Correlacion: ", cuadratica.get_coeficiente_corelacion())
print("Coeficiente de Determinacion: ", cuadratica.get_coeficiente_determinacion())
print("----------------------------------------------------------")
print("Regresion  Cubica")
cubica.imprimir_ecuacion()
print("3 datos conocidos: ")
print("#1 x = 108 y = ", cubica.predecir(108))
print("#2 x = 115 y = ", cubica.predecir(115))
print("#3 x = 106 y = ", cubica.predecir(106))
print("Predicciones de 3 datos:")
print("#1 X = 92, Y  = ", cubica.predecir(92))
print("#2 X = 40, Y  = ", cubica.predecir(40))
print("#3 X = 100, Y  = ", cuadratica.predecir(100))
print("Coeficiente de Correlacion: ", cubica.get_coeficiente_corelacion())
print("Coeficiente de Determinacion: ", cubica.get_coeficiente_determinacion())