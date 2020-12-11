personas={  "Carlos":14,
            "Jose":78,
            "Maria":54,
            "Juan":21,
            "Marcos":34

}

for nombre,edad in personas.items():
    print(" El que tiene {} se llama {}".format(edad,nombre))

#saber cuanto elementos hay en un diccionario
print(len(personas))

#borrar un elemnto especifico
del personas["Marcos"]


#Para imprimir las claves
print(personas.keys())

#Para impirmir los valores
print(personas.values())

#Devolver el elemento de esta clave
print(personas.get("Carlos"))

#Eliminar el diccioanrio entero
personas.clear()