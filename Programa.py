
import random


class Cuestionador:

    def __init__(self):

        self.questions=[
            "¿Qué es el ALMICANTARA?",
            "¿Dónde se encuentra el zenit?",
            "¿Cuántos ordenes existen en la taxonomía de suelos?"

        ]

        self.answers=[
            "Circulo imaginario en la esfera celeste",
            "90 grados respecto al horizonte",
            12
        ]

    def jugar(self):
        #Generar un número aleatorio entre 0 y n-1 siendo n el tamaño de la lista de preguntas 
        n=len(self.questions)
        number=random.randint(0, n-1)     
        print(self.questions[number])         

        #Solicitar la respuesta 
        respuesta=input("¿Cual es tu respuesta, mi pex?")        

        #Verificar si la respuesta es correcta
        if respuesta== self.answers[number]:
            print("Eres genial, mi perrito!!!")  
        else:
            print("Deje de pensar que sus papás lo van a mantener")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   