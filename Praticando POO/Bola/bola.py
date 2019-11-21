class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def __str__(self):
        return self.cor + ' - ' + self.circunferencia + ' - ' + self.material

    def trocacor(self, ncor):
        self.cor = ncor

    def mostracor (self, ncor):
        print(self.cor)

        