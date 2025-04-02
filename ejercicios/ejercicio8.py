'''Problema: Solicitar al usuario dos conjuntos de números y luego mostrar:

    La unión de ambos conjuntos.

    La intersección de ambos conjuntos'''
    
    #en casa

#conjunto_1=set(map(float, input("ingresa el primer conjunto de numeros: ").split()))
#conjunto_2=set(map(float, input("ingresa el segundo conjunto de numeros: ").split()))

#conjunto_3=conjunto_1.union(conjunto_2)
#print(conjunto_3)

#en clase

conjunto1=set(map(int, input("ingrese los numeros del primer conjunto: ").split()))
conjunto2=set(map(int, input("ingrese los numeros del segundo conjunto: ").split()))
union=conjunto1 | conjunto2   #metodo union
interseccion=conjunto1 & conjunto2 #metodo interseccion
print(conjunto1, conjunto2, union, interseccion)



