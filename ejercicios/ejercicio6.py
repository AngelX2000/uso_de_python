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
print(lista_1[::-1])   #es lo mismo que la funcion lista_1.reverse()
suma=sum(lista_1)
print("la suma de los numeros es:", suma)
lista_1.sort()
print(lista_1)
lista_1.sort(reverse=True) #la funcion sort ordena la lista en forma ascendente:  junto con la funcion reverse=true la organiza de forma descendente, y reverse=false ascendente.
print(lista_1)



