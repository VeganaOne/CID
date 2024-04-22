from Datos import Datos
from regresionLineal import regresionLineal

#Arreglo de datos para el Data Set
x = [23,26,30,34,43,48,52,57,58]
y  = [651,762,856,1063,1190,1298,1421,1440,1518]
#Se crea el objeto de Datos con los datos del arreglo
datos = Datos(x,y)
#Creamos nuestra clase de regresionLineal
operacion = regresionLineal(datos.get_x(),datos.get_y())
operacion.imprimir_ecuacion()
print("X = 10, la prediccion de Y es = ", operacion.predecir(10))
print("Coeficiente de Determinacion: ", operacion.get_coeficiente_determinacion())
print("Coeficiente de Correlacion: ", operacion.get_coeficiente_corelacion())
print("---------------------------------------------")
print("Datos a predecir:")
print("Primero X = 15, Y  = ", operacion.predecir(15))
print("Segundo X = 28, Y  = ", operacion.predecir(28))
print("Tercero X = 35, Y  = ", operacion.predecir(35))
print("Cuarto X = 54, Y  = ", operacion.predecir(54))
print("Quinto X = 60, Y  = ", operacion.predecir(60))