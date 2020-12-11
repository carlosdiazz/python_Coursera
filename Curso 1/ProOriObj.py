class Animal:
    name = ""
    category = ""
    
    def __init__(self, name):
        self.name = name
    
    def set_category(self, category):
        self.category = category

class Turtle(Animal):
    category="reptile"

print(Turtle.category)

print("----------------------------------------------")
#-----------------------------------------------------
class Fruta:
    color=""
    sabor=""

    def contar(self):
        print("Hola su color es: {}".format(self.color))

manzana1=Fruta()
manzana1.color="rojo"

print(manzana1.color)
manzana1.contar()



class Vehiculo:

    #Con ese metodo podemos crear variales predeterminada de inicio
    def __init__(self, color, marca):
        self.color=color
        self.marca=marca

    #Este método nos permite definir cómo se imprimirá una instancia de un objeto cuando se pase a la función print ()
    #Con este metodo podemos imprimir cuando mandemos  imprimir la funcion
    def __str__(self):
        return "El colo del vehiculo es: {} y la marca es: {}".format(self.color,self.marca)

vehiculo1=Vehiculo("Azul","Honda")

print(vehiculo1.color)
print(vehiculo1)