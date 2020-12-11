ganadores=['Carlos','Jose','Maria','Jesus']

for index, persona in enumerate(ganadores):
    print("{} - {}".format(index+1,persona))


def skip_elements(elements):
	
    lista=[]
    for index ,elemento in enumerate(elements):
        
        if index in[0,2,4,6,8]:
            lista.append(elemento)

    return lista


    

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']