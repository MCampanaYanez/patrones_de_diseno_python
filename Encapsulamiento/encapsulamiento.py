class encapsulamiento():

    def __init__(self):
        self.__numero = 0 ## el "__" es para encapsular la variable de forma privada, de no tener esto queda público y editable.

    def operacion(self):
        print(self.__numero + 20)

    def resultado(self):
        return self.__numero 
    
ejemplo = encapsulamiento()

ejemplo.numero = 100 ## de esta forma creas una variable llamada número, pero no será la de la clase padre

ejemplo.operacion() ## Verás que el valor de __numero es 0, porque no se ha modificado la variable encapsulada

print(ejemplo.numero) ## Solo puedes llamar esta variable creada, porque la encapsulada es privada

print(ejemplo.resultado()) ## Verás que el valor de __numero es 0, porque no se ha modificado la variable encapsulada