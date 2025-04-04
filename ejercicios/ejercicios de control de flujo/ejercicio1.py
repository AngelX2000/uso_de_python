'''
crear una lista de palabras predefinida y pedir al usuario
una palabra. Indicar si esta en el listado o no

'''
lista=["tren", "auto", "moto"]
consulta=input("ingrese un metodo de movilidad: ")

if consulta in lista:
    print("vehiculo encontrado")

if lista.count(consulta)>0:
    print("el vehiculo se encuentra disponible")
