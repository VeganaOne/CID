from Calculos import Calculos
class RegresionLineal:
    def __init__(self,x,y):
        self.calculos = Calculos(x,y)
        self.b0 = round(((self.calculos.sum_y() * self.calculos.sum_x_cuadrada()) - (self.calculos.sum_x() * self.calculos.sum_x_sum_y())) / ((self.calculos.get_n() * self.calculos.sum_x_cuadrada()) - self.calculos.sum_x_sum_x()),2)

        self.b1 = round(((self.calculos.get_n() * self.calculos.sum_x_sum_y()) - (self.calculos.sum_x() * self.calculos.sum_y())) / ((self.calculos.get_n() * self.calculos.sum_x_cuadrada() - self.calculos.sum_x_sum_x())),2)

        self.coeficiente_corelacion = round(((self.calculos.get_n() * self.calculos.sum_x_sum_y()) - (self.calculos.sum_x() * self.calculos.sum_y())) / (((self.calculos.get_n() * self.calculos.sum_x_cuadrada() - self.calculos.sum_x_sum_x()) * (self.calculos.get_n() * self.calculos.sum_y_cuadrada() - self.calculos.sum_y_sum_y())) ** 0.5),2)

        self.coeficiente_determinacion = round(self.coeficiente_corelacion * self.coeficiente_corelacion,2)

    def imprimir_ecuacion(self):
        print("Y = ", self.b0, "+", self.b1, "X")
    def predecir(self, x):
        return round(self.b0 + self.b1 *x,2)

    def get_coeficiente_corelacion(self):
        return self.coeficiente_corelacion
    
    def get_coeficiente_determinacion(self):
        return self.coeficiente_determinacion