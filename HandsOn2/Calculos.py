class Calculos: #resivimos dos valores x y y
    def __init__(self, valorx, valory):
        self.arreglox = valorx
        self.arregloy = valory
        self.n = len(valorx)
    
    def sum_x(self): #sumatoria de x
        regreso = 0
        for valor in self.arreglox: #suma la iteracion del tamaño de x
            regreso += valor
        return regreso

    def sum_y(self):
        regreso = 0
        for valor in self.arregloy: #suma la iteracion del valor de y
            regreso += valor
        return regreso

    def sum_x_cuadrada(self):
        regreso = 0
        for valor in self.arreglox: # eleva el valor de x al cuadrado y lo suma
            regreso += valor * valor
        return regreso
    
    def sum_y_cuadrada(self):
        regreso = 0
        for valor in self.arregloy: #eleva el valor de y al cuadrado y lo suma
            regreso += valor * valor
        return regreso
    
    def sum_x_sum_x(self):
        return  self.sum_x() * self.sum_x() # eleva al cuadrado la sumatoria de x
    
    def sum_y_sum_y(self):
        return  self.sum_y() * self.sum_y() #eleva al cuadrado la sumatoria de y
    
    def sum_x_sum_y(self):
        regreso = 0
        for iterador in range(self.n):
            regreso += self.arreglox[iterador] * self.arregloy[iterador] #el valor de xsubcero lo mutiplica por el valor de ysubcero
        return regreso
    
    def get_n(self):
        return self.n #retorno del numero de elementos