'''
Problema: Escribe un programa que verifique si una palabra ingresada por el usuario está 
en la siguiente frase:
"Python es un lenguaje de programación poderoso".
'''
usuario=str(input("ingresa una palabra"))

frase=str("python es un lenguaje de programacion poderoso")

print("si la palabra que ingresaste coincide con alguna de la frase te arrojará true, de lo contrario te arrojará false:", usuario in frase)
