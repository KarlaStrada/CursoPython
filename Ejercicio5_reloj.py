#Estrada Crespo Karla Julieta - Ejercicio5 (reloj)
import os
import time

entrada = input("Ingrese la hora:minuto:segundo de esta manera: ")
caracter = ":"

while True:

    if entrada.find(caracter) != -1:
        break
    else:
        print("Error, ese no es el formato de hora indicado")
        entrada = input("Ingrese la hora:minuto:segundo de esta manera: ")

lista = entrada.split(":") #va a separar cada elemento cada que haya ":" y lo va a mandar asi -> ["5", "12", "41"] en forma de lista                   
print(lista)
e_hora = int(lista[0])
e_minuto = int(lista[1])
e_segundo = int(lista[2])

while True: 
    if e_hora < 24 and e_minuto < 60 and e_segundo < 60:
        break
    else:
        print("Error")
        entrada = input("Ingrese la hora:minuto:segundo de esta manera: ")
        lista = entrada.split(":")                
        print(lista)
        e_hora = int(lista[0])
        e_minuto = int(lista[1])
        e_segundo = int(lista[2])
   
        


for hora in range(e_hora, 24):
    for minuto in range(e_minuto, 60):
        for segundo in range(e_segundo, 60):
            os.system("cls")
            print(f"{hora}:{minuto}:{segundo}")
            time.sleep(1)

            if segundo == 59:
                segundo = 0
                e_segundo = 0

        if minuto == 59:
            minuto = 0
            e_minuto = 0

    if hora == 23:
        hora = 0
        e_hora = 0