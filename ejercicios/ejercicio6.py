'''
Problema: Solicitar al usuario 5 números enteros, almacenarlos en una lista y luego mostrar:

    La lista original.

    La lista en orden inverso.

    La suma de los números.
'''
x=int(input("ingresa un numero entero"))
y=int(input("ingresa un numero entero"))
c=int(input("ingresa un numero entero"))
b=int(input("ingresa un numero entero"))
a=int(input("ingresa un numero entero"))

lista_1=[x,y,c,b,a]
print(lista_1)
print(lista_1[::-1])
suma=sum(lista_1)
print("la suma de los numeros es:", suma)


