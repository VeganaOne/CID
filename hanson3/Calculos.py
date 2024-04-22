class Calculos:
    def __init__(self, valorx, valory):
        self.arreglox = valorx
        self.arregloy = valory
        self.n = len(valorx)
    
    def sum_x(self):
        regreso = 0
        for valor in self.arreglox:
            regreso += valor
        return regreso

    def sum_y(self):
        regreso = 0
        for valor in self.arregloy:
            regreso += valor
        return regreso

    def sum_x_cuadrada(self):
        regreso = 0
        for valor in self.arreglox:
            regreso += valor * valor
        return regreso
    
    def sum_y_cuadrada(self):
        regreso = 0
        for valor in self.arregloy:
            regreso += valor *  valor
        return regreso
    
    def sum_x_cubica(self):
        regreso = 0
        for valor in self.arreglox:
            regreso += valor * valor * valor
        return regreso  
    
    def sum_x_cuarta(self):
        regreso = 0
        for valor in self.arreglox:
            regreso += valor * valor * valor * valor
        return regreso
    
    def sum_x_quinta(self):
        regreso = 0
        for valor in self.arreglox:
            regreso += valor * valor * valor * valor * valor	
        return regreso
    
    def sum_x_sexta(self):
        regreso = 0
        for valor in self.arreglox:
            regreso += valor * valor * valor * valor * valor * valor	
        return regreso
    
    
    def sum_x_sum_x(self):
        return  self.sum_x() * self.sum_x()
    
    def sum_y_sum_y(self):
        return  self.sum_y() * self.sum_y()
    
    def sum_x_sum_y(self):
        regreso = 0
        for iterador in range(self.n):
            regreso += self.arreglox[iterador] * self.arregloy[iterador]
        return regreso
    
    def sum_x_cuadrada_sum_y(self):
        regreso = 0
        for iterador in range(self.n):
            regreso += self.arreglox[iterador] * self.arreglox[iterador] * self.arregloy[iterador]
        return regreso
    
    def sum_x_cubica_sum_y(self):
        regreso = 0
        for iterador in range(self.n):
            regreso += self.arreglox[iterador] * self.arreglox[iterador] * self.arreglox[iterador] * self.arregloy[iterador]
        return regreso
    def promedio_y(self):
        regreso = self.sum_y() / self.n
        return regreso
    


    def get_n(self):
        return self.n