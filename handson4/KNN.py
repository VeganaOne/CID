from Calculos import Calculos

class KNN:
    def __init__(self, k = 5, metrica = 'euclileana') -> None:
        self.k: int = k
        self.metrica: str = metrica

    def fit(self, X_train, y_train) -> None:
        self.X_train: list[float] = X_train
        self.y_train: list[float] = y_train
        self.dm: Calculos = Calculos()

        self.x_train_std: list[float] = self.dm.standardize(X_train)

    def predict(self, prueba) -> list[int]:
        prueba_std: list[float] = self.dm.standardize(prueba)

        distancias: list[float] = self._compute_distancias(prueba_std)
        vecinoMasCernano: list[float] = self._get_vecinoMasCernano(distancias)
        predicciones: list[int] = self._mayoriaVotos(vecinoMasCernano)

        return predicciones

    def _compute_distancias(self, prueba: list[float]) -> list[float]:
        distancias: list[float] = []

        for prueba in prueba:
            distanciasi: list[float] = []

            for x_train in self.x_train_std:
                distancia: float = self._calcularDistancia(prueba, x_train)
                distanciasi.append(distancia)

            distancias.append(distanciasi)

        return distancias

    def _calcularDistancia(self, x1: list[float], x2: list[float]) -> float:
        if self.metrica == 'euclileana':
            return self.dm.euclileana_distancia(x1, x2)

        elif self.metrica == 'manhattan':
            return self.dm.manhattan_distancia(x1, x2)

        else:
            raise ValueError('Metrica Invalida')

    def _get_vecinoMasCernano(self, distancias: list[float]) -> list[float]:
        vecinoMasCernano: list[float] = []

        for distanciasi in distancias:
            indexes: list[float] = []

            for i in range(len(distanciasi)):
                distanciaMinima: float = distanciasi[0]
                min_index: int = 0

                for j in range(1, len(distanciasi)):
                    if distanciasi[j] < distanciaMinima:
                        distanciaMinima = distanciasi[j]
                        min_index = j

                indexes.append(min_index)

            if len(indexes) > self.k:
                indexes = indexes[:self.k]

            vecinoMasCercanoi: list[int] = []

            for i in indexes:
                vecinoMasCercanoi.append(self.y_train[i])

            vecinoMasCernano.append(vecinoMasCercanoi)

        return vecinoMasCernano

    def _mayoriaVotos(self, vecinoMasCernano: list[float]) -> list[int]:
        predicciones: list[int] = []

        for vecinoMasCercanoi in vecinoMasCernano:
            cuentaVotos = {}

            for etiqueta in vecinoMasCercanoi:
                if etiqueta not in cuentaVotos:
                    cuentaVotos[etiqueta] = 0

                cuentaVotos[etiqueta] += 1

            votosMaximo: int = 0
            maximo_etiqueta: int = None

            for etiqueta, votes in cuentaVotos.items():
                if votes > votosMaximo:
                    votosMaximo = votes
                    maximo_etiqueta = etiqueta

            predicciones.append(maximo_etiqueta)

        return predicciones