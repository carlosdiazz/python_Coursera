
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

def anadir(texto):
    salida={}
    
    for palabra in texto:

        if palabra not in salida.keys():
            salida[palabra]=1        
        else:
            salida[palabra]+=1

    return salida


texto='Me llamo Pedro y hoy quiero hablar del parque que hay junto a mi casa. Yo me divierto todos los días en el parque. Allí veo las palomas comiendo y bebiendo agua. También veo pájaros de colores en los árboles. Yo voy al parque a las cinco de la tarde, cuando termino los deberes de la escuela. Allí veo a mi amigo Juan y a mi amigo Luis. Con ellos juego al escondite y a otros juegos muy entretenidos. Luis se va más temprano del parque porque tiene que ir a la escuela de música a aprender a tocar el piano. Mi padre también va al parque a hacer deporte. Él corre durante una hora por el parque después de trabajar. Mi madre solo va los fines de semana porque acaba tarde de trabajar. Ella se sienta siempre en el mismo banco y yo juego mientras con mis amigos. Por la mañana cruzo el parque para ir al colegio, pero no me entretengo para no llegar tarde a clase. De camino al colegio veo al guarda del parque y siempre me da un caramelo de fresa.'


texto=texto.split(" ")

print(texto)

dicciona=anadir(texto)


cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(dicciona)
cloud.to_file("myfile.jpg")