import random
import time
from playsound import playsound
import speech_recognition as sr

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

diccionario = {1:"cocodrilo",
               2: "tigre",
               3: "leon",
               4: "elefante",
               5: "jirafa",
               6: "delfin",
               7: "otorongo",
               8: "pelicano",
               9: "atun",
               10: "gato"}
print("Aqui")
nivel = 3
lista = [0,0,0,0,0,0,0,0,0,0]
orden = ""
time.sleep(1)
for i in range(nivel):
    num = random.randint(1,10)
    while(lista[num-1] != 0):
        num = random.randint(1,10)
    lista[num-1] = 1
    orden+=diccionario.get(num)+" "
    aux = diccionario.get(num) +".mp3"
    print(orden)
    playsound(aux)
    time.sleep(1.2)

r = sr.Recognizer() 
with sr.Microphone() as source:
    print('Habla: ')
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="es-ES")
        print('Digiste: '+ text)
        text = normalize(text).lower()+" "
        if(text == orden):
            print("Bien")        
            playsound("excelente.mp3")
        else:
            print("Mal")
            playsound("Prueba de nuevo.mp3")
    except:
        print('Ocurrio un error')


    

     