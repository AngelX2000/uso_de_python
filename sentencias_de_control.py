x=520
y=60


'''
condicional if elif else
if then else

if <condicion>:
    operacion 1
    operacion 2
    operacion 3
    .
    .

'''
#caso1
if x > y: #condicion
    print(" x es mayor que y") #operacion


#caso2 ---->if else
if x < y:
    print("x es menor que y")
else:
    print("x es mayor que y")


#caso3 ----> uso del if elif else
if x < y:  #condicion
    print("x es menor que y")
elif x==y:  #condicion
    print("x es igual a y")
elif x/y==8:  #condicion
    print("x dividido y es igual a 8")
else:  #de lo contrario a las condiciones
    print("x es mayor que y")


#variante1
if x%2==0 and x>500:   #multiples condiciones a evaluar
    print("x es par y mayor que 500")


#caso de uso del login a una aplicacion

#ejemplo de ingreso comun
usuario=input("por favor ingrese su usuario: ")
#password=input("por favor ingrese su password: ")


#if usuario=="andres" and password=="1234":
   # print("usuario puede ingresar")
#else:
    #print("usuario o contraseña incorrecto")
    

#ejemplo con if anidado
if usuario=="andres":
    password=input("por favor ingresa el password: ")
    if password=="1234":
        print("usuario puede ingresar")
    else:
        print("contraseña incorrecta")
else:
    print("usuario incorrecto")


    



    print("ejecucion terminada")    




