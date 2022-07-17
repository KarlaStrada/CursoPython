#Estrada Crespo Karla Julieta -> ejercicio4 (calculadora)
#funcion de las operaciones

def operaciones(x, y):
    if operacion == 1 :
        return x + y
    elif operacion == 2 :
        return x - y
    elif operacion == 3 :
        return x * y
    elif operacion == 4 :
        return x / y
    elif operacion == 5 :
        historial(n1, n2, result)
    else:
        print("Este numero de opcion no se encuentra disponible")



#funcion del diccionario
diccionario = {"Sumas": [], "Restas": [], "Multiplicaciones": [], "Divisiones": []}
def historial(x, y, resultado):
    if operacion == 1 :
        id = "Sumas"
        diccionario[id].append(str(x)+"+"+str(y)+"="+str(resultado))
    elif operacion == 2 :
        id = "Restas"
        diccionario[id].append(str(x)+"-"+str(y)+"="+str(resultado))
    elif operacion == 3 :
        id = "Multiplicaciones"
        diccionario[id].append(str(x)+"*"+str(y)+"="+str(resultado))
    elif operacion == 4 :
        id = "Divisiones"
        diccionario[id].append(str(x)+"/"+str(y)+"="+str(resultado))
    return diccionario
                        
            

while True:
    entrada = input("Desea realizar alguna operacion (Y/n): ").lower()

    if entrada == "n":
        break
    else:
        print("Menu: ")
        print("1- Suma")
        print("2- Resta")
        print("3- Multiplicacion")
        print("4- Division")
        print("5- Historial")

    operacion = int(input("Elija el numero de la operacion que desea realizar: "))
    if operacion == 5 :
        if len(diccionario["Sumas"])==0 and len(diccionario["Restas"])==0 and len(diccionario["Multiplicaciones"])==0 and len(diccionario["Divisiones"]) == 0: 
            print("No hay historial")
            continue
        else:
            print(resultadoDicc)
            borrar = input("Desea borrar el historial Y/n: ").lower()
            if borrar == "y":
                diccionario["Sumas"].clear()
                diccionario["Restas"].clear()
                diccionario["Multiplicaciones"].clear()
                diccionario["Divisiones"].clear()
                continue
            else:
                continue
            

    
    n1 = int(input("Ingrese el primer numero de su operacion: "))
    n2 = int(input("Ingrese el segundo numero de su operacion: "))

    result = operaciones(n1, n2)
    print(f"El resultado de su operacion es: {result: .2f}")

    resultadoDicc = historial(n1, n2, result)
    
   

    
       

    

    

        



        

        
     








