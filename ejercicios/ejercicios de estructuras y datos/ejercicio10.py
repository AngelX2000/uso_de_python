'''
Problema: Crear un diccionario con algunos productos 
y permitir que el usuario agregue un nuevo producto con su precio.
'''
#en casa

productos={'manzana':4000, 
           'yogurt':5500, 
           'leche':2800, 
           'cafe':6700, 
           'chocolate':6000}
precios=str(input("inserta nombre del producto: "))
precio=productos.get(precios, "no encontrado")
print(f"${precio}")

nuevoProducto=input("ingresa el nuevo producto: ")
nuevoPrecio=float(input("ingresa el precio: "))
productos[nuevoProducto]=nuevoPrecio

print("Lista actualizada de productos:")
for producto, precio in productos.items():
 print(f"{producto}: ${precio}")   #La f antes de las cadenas de texto indica que es una f-string (cadena formateada). Permite incrustar variables dentro de una cadena utilizando llaves {}


 #en clase

 