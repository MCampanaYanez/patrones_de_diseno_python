from abc import ABC, abstractmethod

## Clase Base: Animales
class Animal(ABC):
    @abstractmethod
    def habla(self):
        pass

## Subclase: Perro, Gato, Pájaro

class perro(Animal):
    def habla(self):
        return("Guau guau")

class gato(Animal):
    def habla(self):
        return("Miau")

class pajaro(Animal):
    def habla(self):
        return("Pio pio")

## Clase Factory: CreadorDeAnimales
class CreadorDeAnimales(ABC):
    def creaAnimal(self, tipo):
        if tipo == "perro":
            return perro()
        elif tipo == "gato":
            return gato()
        elif tipo == "pajaro":
            return pajaro()
        else:
            raise ValueError("Animal desconocido")
            

animal1 = CreadorDeAnimales().creaAnimal("perro")
print(animal1.habla())
animal2 = CreadorDeAnimales().creaAnimal("gato")
print(animal2.habla())
animal3 = CreadorDeAnimales().creaAnimal("pajaro")
print(animal3.habla())
