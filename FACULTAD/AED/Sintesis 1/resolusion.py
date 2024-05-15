

limitLower=int(input('Ingrese un número: '))
limitTop=int(input('Ingrese un segundo número: '))

while limitTop <= limitLower:
    limitTop=int(input('Recuerde que el segundo número no puede ser igual al primero y debe ser mayor que el primer número ingresado, vuelva a ingresa un segundo número '))


result = []


for number in range(limitLower, limitTop):
        result.append(number)       
result.append(limitTop)

print("*****")
print("****")
print("***") 

print("***")
print("****")
print("*****")  

print(f"Los números comprendidos entres los limistes son: {result}")

print("*****")
print("****")
print("***")

print("***")
print("****")
print("*****")

sumaTotal= sum(result)

print(f"A)_ la suma de todos los números son: {sumaTotal}")

print("*****")
print("****")
print("***")

print("***")
print("****")
print("*****")

numerosPares=[]
numerosImpares=[]

for numbers in result:
    if numbers % 2 == 0:
        numerosPares.append(numbers)

for numbers in result:
    if numbers % 2 != 0:
        numerosImpares.append(numbers)

print(f"B)_ Los números pares son: {numerosPares}")

print("*****")
print("****")
print("***")

print("***")
print("****")
print("*****")

print(f"B)_ Los números impares son: {numerosImpares}")

print("*****")
print("****")
print("***")

print("***")
print("****")
print("*****")


numeroDivisiblesporCinco=[]

for numbers in result:
    if numbers % 5 == 0:
        numeroDivisiblesporCinco.append(numbers)

print("*****")
print("****")
print("***") 

print("***")
print("****")
print("*****")        

print(f"C)_ Los números divisibles por 5 son : {numeroDivisiblesporCinco}")

print("*****")
print("****")
print("***")
        
print("***")
print("****")
print("*****")    

for numbers in result:
    if numbers == 0:
        print('D)_ Se ha ingresado un número 0') 
        


numerosDivisibles=[]
for numbers in result:
    if numbers % 1 == 0 and numbers % 3==0:
        numerosDivisibles.append(numbers)
        

print("*****")
print("****")
print("***")
        
print("***")
print("****")
print("*****")  
print(f'Los números que son divisibles por 1 y por 3 son {numerosDivisibles}')

print(f'La cantidad de valores en la coleccion dada por los limites que ha ingresado son: {len(result)}')