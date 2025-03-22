'''
operadores aritmeticos
20-marzo-2025

'''


#para realizar comentarios se utilizan los operadores de comillas triples y/o el # (''' y #)

#operador suma
#print(2+6)

#operador multiplicacion
#print(2*8)

#operador resta
#print(8-4)

#podemos guardar un valor en una variable poniendo el nombre de la variable seguido de el simbolo = y despues el valor
x=4
y=6
#print(x*y)

#operador division
z=12/4
#print(z)
#print(type(z)) #el resultado de la division siempre es flotante

#print(10/3)
#print(10//3)
#print(14.5//3)

#la division con doble barra (//) siempre devuelve el entero mas proximo

#print(20/3)
#print(20%3)

#el "%" se utiliza como modulo, que es el residuo en una operacion

#print(8//-3)
#print(8/-3)

#para expresar unapotencia utiliza dos veces (**)
#print(5**2)

'''
operadores de igualdad (==) y desigualdad (!=)

este tipo de operadores los usamos cuando deseamos comparar
expresiones o variables. python evalua si se cumple la 
comparacion y nos devuelve (retorna) un valor True o False

'''

#print(8==8)

#print(3==3.01)

#print(3!=1)

'''
operadores de asignacion
'''
#asignacion de igualdad o definicion
w=5

#incremento: con += podemos incrementar el valor actaul de una variable indicando seguidamente en cuantas unidades queremos afectarla 
#saldo=100
#saldo=saldo+1   #esto es igual a la expresion (saldo+=1)
#print(saldo)

#decrecimiento: este operador se utiliza para hacer decrecer el valor actual de una variable, el simbolo utilizado es -= y debe ser acompañado de un valor que ejercerá el efecto de disminucion
credito=8
credito=credito-2 #esto es lo mismo que expresar la instruccion (credito-=2)
print(credito)



'''
operadores logicos
and: comprueban si todas las condiciones se cumplen, true, flase de lo contrario
or: comprueba si alguna de las condiciones se cumple , true, false de lo contrario
not: negar el estado de una variable
'''
print(x==4 and y==6)
print(x==4 or y==8)
print(x==5 or y==8)

usuario_logeado=True
click_logout=True
print(not usuario_logeado)










