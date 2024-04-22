from Calculos import Calculos
import numpy as np
class RegresionCubica:
    def __init__(self,x,y):
        calculos = Calculos(x,y)
        self.matrizA = np.array([[calculos.sum_x_cubica(),calculos.sum_x_cuadrada(),calculos.sum_x(),calculos.get_n()],[calculos.sum_x_cuarta(),calculos.sum_x_cubica(),calculos.sum_x_cuadrada(),calculos.sum_x()],[calculos.sum_x_quinta(),calculos.sum_x_cuarta(),calculos.sum_x_cubica(),calculos.sum_x_cuadrada()],[calculos.sum_x_sexta(),calculos.sum_x_quinta(),calculos.sum_x_cuarta(),calculos.sum_x_cubica()]])

        self.matrizB = np.array([calculos.sum_y(),calculos.sum_x_sum_y(),calculos.sum_x_cuadrada_sum_y(),calculos.sum_x_cubica_sum_y()])
        self.resultado = np.dot(np.linalg.inv(self.matrizA),self.matrizB)
        self.a = round(self.resultado[0],6)
        self.b = round(self.resultado[1],6)
        self.c = round(self.resultado[2],6)
        self.d = round(self.resultado[3],6)

        sum_ypredicida_ypromedio = 0
        sum_y_ypromedio = 0
        for iterador in range(calculos.get_n()):
            sum_ypredicida_ypromedio += (self.predecir(x[iterador]) - calculos.promedio_y()) * (self.predecir(x[iterador]) - calculos.promedio_y())
            sum_y_ypromedio += (y[iterador] - calculos.promedio_y()) * (y[iterador] - calculos.promedio_y()) 
        
        self.coeficiente_determinacion = round(sum_ypredicida_ypromedio / sum_y_ypromedio,4)
        self.coeficiente_corelacion = round(((calculos.get_n() * calculos.sum_x_sum_y()) - (calculos.sum_x() * calculos.sum_y())) / (((calculos.get_n() * calculos.sum_x_cuadrada() - calculos.sum_x_sum_x()) * (calculos.get_n() * calculos.sum_y_cuadrada() - calculos.sum_y_sum_y())) ** 0.5),2)



    def imprimir_ecuacion(self):
        print("Y = ", self.a, "x cubica + ", self.b, "x cuadrada + ", self.c, "x + ", self.d)

    def predecir(self, x):
        return round(self.a * x * x * x + self.b * x * x + self.c * x + self.d,4)
    
    def get_coeficiente_corelacion(self):
        return self.coeficiente_corelacion

    def get_coeficiente_determinacion(self):
        return self.coeficiente_determinacion
    


