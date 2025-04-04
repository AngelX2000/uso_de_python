'''
Problema: Escribe un programa que solicite un número al usuario y lo incremente en 5 unidades y 
luego lo decremente en 3.
'''

usuario=float(input("ingresa un numero entero"))

print("numero ingresado: ", usuario)
usuario=usuario + 5 #numero+=5
print(usuario)

usuario-=3
print(usuario)
