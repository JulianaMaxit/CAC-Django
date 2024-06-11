#variables

contador = 0
print(contador)

contador += 1
contador += 1

print(contador)

contador = "Hola"

print(contador)

# estructuras de control
condicion = True # False (tiene que ser con mayúscula) None

if condicion:
    print ("Es verdadera")

else:
    print ("Es falsa") 

#bucle for clásico

for i in range (0,10):
    print(i)

lista = ["Hola", "Sí", "Adiós"]

for palabra in lista:
    print(palabra)

condicion = True

contador = 0
while condicion:
    contador +=1
    print(contador)

    if contador > 12:
        break
print("Adios")