class Carro:
    def __init__(self, marca, modelo):
        self.__marca=marca
        self.__modelo=modelo
    
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca= marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo=modelo

carro1=Carro('Mitsubishi', 'Lancer')

print(carro1.marca)
print(carro1.modelo)

carro1.marca='Nissan'
carro1.modelo='Silvia.S15'
print(f'\n{carro1.marca}')
print(carro1.modelo)