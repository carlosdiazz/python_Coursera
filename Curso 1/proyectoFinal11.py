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

def calculate_frequencies(file_contents):
    text=""
    lista=[]
    salida={}
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{;}:'"\,<>./?@#$%^&*_~'''
    
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    for eli in file_contents:
        if eli not in punctuations:
            text=text+eli
    
    text=text.split(" ")

    for borrar in text:
        if borrar not in uninteresting_words:
            lista.append(borrar)


    for palabra in lista:

        if palabra not in salida.keys():
            salida[palabra]=1        
        else:
            salida[palabra]+=1
   
    return salida


texto="hola, me llamo Carlos. Y tu cual es tu nombre"

#dicciona="hola como esta yo estoy bien y tu "
#dicciona=dicciona.split()
#listo=anadir(dicciona)

imagen=calculate_frequencies(texto)
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(imagen)
cloud.to_file("myfilee.jpg")