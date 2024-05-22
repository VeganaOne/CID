from Data import Data
from KNN import KNN

def main() -> None:
    ds = Data()
    objeto = KNN(metrica = 'euclileana')

    objeto.fit(ds.get_x(), ds.get_y())

    prueba = [[150, 67], [167, 57], [181, 86], [210, 90], [175, 97]] 
    predicciones = objeto.predict(prueba) 

    print('predicciones')
    for i in range(len(prueba)):
        print("************************************")
        print(f' Prediccion {i + 1}')
        print(f'Altura: {prueba[i][0]} cms')
        print(f'Peso: {prueba[i][1]} kgs')
        print(f'Prediccion Talla Camisa: {predicciones[i]} -> {['Mediana', 'Grande'][predicciones[i]]}')

if __name__ == '__main__':
    main()