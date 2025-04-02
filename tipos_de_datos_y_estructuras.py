'''
TIPOS DE DATOS
STRINGS: cadenas de texto <class 'str'>
'''
dato="Enca24"
dato_2='Enca24'

#print(type(dato))
#print(type(dato_2))

#concatenacion de strings
texto_1="programa "
texto_2="desarrollador junior"

enunciado=texto_1 + texto_2
#print(enunciado)

#indexacion de strings
#laindexacion se refiere a acceder a un elemento de una cadena en una posicion
nombre="andres felipe"
#print(nombre[0])
'''
Python es un lenguaje indexado en cero
'''
#print(nombre[5])
#print(nombre[-1])  #cuando utilizamos las posiciones en negativo - cuenta de derecha a izquierda

#slicing de cadenas (porcion de la cadena) 
#print(nombre[:]) #trae todo el texto
#print(nombre[0:3]) #esta forma de porcionar no incluye el extremo derecho, osea el 3
#print(nombre[2:4])
#print(nombre[0:-5])

'''
tipos de datos numericos
<class 'int'> : se refieren  numeros enteros
<class 'float'> : se refiere a numeros flotantes que contienen decimales
'''
x=5
#print(type(x))
y=5.0
#print(type(y))
'''
datos boolean
1,0 o falso / verdadero
<class 'bool'>
true
false
'''
asistencia=True
#print(type(asistencia))
#print(not asistencia)

'''
TIPOS DE ESTRUCTURAS
sets: se definen en python con {,,,,}
tuplas: se definen en python con (,,,,)
listas: se definen en python con [,,,,]
diccionarios: {'clave':'valor','clave_2':'valor_2',,,}
'''

#Sets o conjuntos
'''
se utilizan para almacenar informacion cuando no interesa el orden ni la posicion 
no permite valores duplicados
'''
conjunto_1={"a", "b", "c"}
conjunto_2={"d", "e", "f"}

#print(type(conjunto_1))
#print(conjunto_1)

'''

los metodos indican las cosas que podemos hacer con los objetos
'''
#metodos de los conjuntos
conjunto_1.add("h")
#print(conjunto_1)

conjunto_2.remove("f")
#print(conjunto_2)

conjunto_3=conjunto_1.union(conjunto_2)
#print(conjunto_3)

#aplicar un metodo
conjunto_2.update(conjunto_1)
#print(conjunto_2)

conjunto_2.clear()
#print(conjunto_2)

'''
Tuplas
<class 'tuple'>
son estructuras en python mas rigidas,
son inmutables,
se almacenan distintos tipos de datos
'''
tupla_1=(1,1,1,1,1,1,1,1,"b", True)
#print(type(tupla_1))
#print(tupla_1.count("b"))

#print(tupla_1.index("b"))



'''
uso de diccionarios
{clave:valor}
'''

estudiantes={"andres ":25, "jose ":22, "diana ":26}
print(estudiantes.keys())
print(estudiantes.values())
print(estudiantes.pop("diana "))  #pop elimina la clave "diana " y retorna el value correspondiente
print(estudiantes)
