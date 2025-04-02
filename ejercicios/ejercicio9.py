'''
Problema: Crear un diccionario con las calificaciones de 3 estudiantes 
y permitir que el usuario consulte la calificación de uno de ellos.
'''

calificaciones={'carlos':3.0, 'juan':2.1, 'marta':4.3}

maestro=str(input("nombre de alumno: "))

calificacion=calificaciones.get(maestro, "no encontrado")  #get nos evita un erroren la app o pagina si lo ingresado no se encuentra en la base de datos
print(calificacion)