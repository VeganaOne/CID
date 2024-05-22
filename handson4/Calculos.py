class Calculos:
    def __init__(self) -> None:
        pass

    def standardize(self, data: list[float]) -> list[float]:
        altura: list[float] = [data[i][0] for i in range(len(data))]
        peso: list[float] = [data[i][1] for i in range(len(data))]

        std_altura: list[float] = []
        std_peso: list[float] = []

        for i in range(len(data)):
            std_altura.append((altura[i] - min(altura)) / (max(altura) - min(altura)))
            std_peso.append((peso[i] - min(peso)) / (max(peso) - min(peso)))

        return [[std_altura[i], std_peso[i]] for i in range(len(data))]

    def euclileana_distancia(self, x1: list[float], x2: list[float]) -> float:
        distancia = 0

        for i in range(len(x1)):
            distancia += (x1[i] - x2[i]) ** 2

        return distancia ** 0.5

    def manhattan_distancia(self, x1: list[float], x2: list[float]) -> float:
        distancia = 0

        for i in range(len(x1)):
            distancia += abs(x1[i] - x2[i])

        return distancia