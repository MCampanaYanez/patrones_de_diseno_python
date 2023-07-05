#Herencia y polimorfismo

class padre:
    def __init__(self, numero):
        self.numero = numero

    def mensaje1(self):
        print("Hola buenos días")

    def mensaje2(self):
        print("Hola buenas tardes")

    def mensaje3(self):
        print("Hola buenas noches")


class hijo(padre):
    def __init__(self, numero):
        super().__init__(numero)


    def mensaje4(self):
        print("Cómo has estado¡")
        print(self.numero + 10)
    def mensaje5(self):
        print("Cómo va la vida?")
    def mensaje6(self):
        print("Hasta otra oportunidad")


objeto = hijo(10)
objeto.mensaje1()
objeto.mensaje2()
objeto.mensaje3()
objeto.mensaje4()
objeto.mensaje5()
objeto.mensaje6()
