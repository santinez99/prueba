import math
"""
v1 = int(input("V1: "))
v2 = int(input("V2: "))
dif = int(input("D: "))
d=v1-v2
result=dif/d
print(result)
"""
class Fabrica:
    def __init__(self,tiempo,nombre,ruedas):
        self.tiempo = tiempo
        self.nombre = nombre
        self.ruedas = ruedas
        print("Se creo el auto",self.nombre)
    
    def __str__(self):
        return """
        
        {}({})""".format(self.nombre,self.tiempo)

class Listado:
    autos = []

    def __init__(self,autos):
        print(autos)
        pass

    def fabricar(self,x):
        self.autos.append(x)

    def visualizar(self):
        for x in self.autos:
            print(x)


a = Fabrica(10,"Chevrolet",4)
b = Fabrica(20,"Renault",3)
l = Listado(a)
l.fabricar(a)
l.fabricar(b)
l.visualizar()
print("*********+")
b = [a,a]
for x in b:
    print(x,"\n")