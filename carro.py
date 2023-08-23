class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
        
    def mostrarInfo(self):
       print(f"Marca:{self.marca}\nModelo:{self.modelo}\nAno:{self.ano}")
    
    def setMarca(self,marca):
       self.marca = marca

    def getMarca(self):
        return self.marca
    
    def setModelo(self,modelo):
       self.modelo = modelo

    def getModelo(self):
        return self.modelo
    
    def setAno(self,ano):
       self.ano = ano

    def getAno(self):
        return self.ano

    def getLigado(self):
        self.ligado = True
        print("Carro está ligado")
        return self.ligado

    def getDesligado(self):
        self.ligado = False
        print("Carro está desligado")
        return self.ligado

def main():

    carro1 = Carro("fiat", "uno", "2012")
    carro1.mostrarInfo()
    print(carro1.getLigado())
    print(carro1.getDesligado())
    carro1.mostrarInfo()

if __name__ == "__main__":
    main()
