

nume=[4,35,12,3,42,34,65,123,5]

#nume.sort()

print(sorted(nume))


nombres=['Carlos','Jose','Jesus','Cecilia','Gisell','Ana','Pedro','Alex','Maria']
print(sorted(nombres,key=len))


tabla=[x*7 for x in range(1,11)]
print(tabla)

z= [x for x in range(0,101) if x % 3 ==0]
print (z)

numeros=[5,9,2,65,124,56,23,453,65]
print(numeros)

#Para odrdenar la lista
numeros.sort()
print(numeros)

#Para invertit los elemntos de la lsita
numeros.reverse()

#Para eliminar elemento de una lista
numeros.clear()


colores=['rojo','azul','amarillo','negro']


#Para agreagr elementos a una lista
colores.append('blanco')

#insertamos un elemento en esta posicion
colores.insert(2,"rosado")

#eliminamos este elemento
colores.remove('rojo')

especifico=colores.pop(1)


print(especifico)
print (colores)