#Estrada Crespo Karla Julieta - Ejercicio3 (Diccionarios)

verduras = [
    {"verdura": "brocoli", "precio": 8.55 },
    {"verdura": "pepino", "precio": 6.87 },
    {"verdura": "calabaza", "precio": 11.55},
    {"verdura": "chayote", "precio": 14.33},
]

#print(verduras)

print("Binevenido a la verduleria Karla\n")
print("Menu de verduras: ")
print(verduras[0]["verdura"])
print(verduras[1]["verdura"])
print(verduras[2]["verdura"])
print(verduras[3]["verdura"])
#print(type(verduras[3]["precio"]))
entrada = input("Por favor ingrese la verdura que desea adquirir: ").lower()
entrada2 = float(input("Ingrese cuantos kilos desea: "))

resultado = 1
if entrada == verduras[0]["verdura"]:
    resultado = verduras[0]["precio"] * entrada2
elif entrada == verduras[1]["verdura"]:
    resultado = verduras[1]["precio"] * entrada2
elif entrada == verduras[2]["verdura"]:
     resultado = verduras[2]["precio"] * entrada2
elif entrada == verduras[3]["verdura"]:
     resultado = verduras[3]["precio"] * entrada2
else:
    print("Esa verdura no se encuentra disponible")
   
print(f"Total a pagar: {resultado: .2f}")
   

