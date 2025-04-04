dia=input("ingrese el dia de la semana: ").lower()
match dia:
    case "sabado" | "domingo":
        print(f"{dia} es un fin de semana")
    case "lunes":
        print(f"{dia} es el dia mas dificil")
    case "martes" | "miercoles" | "jueves":
        print("es un dia normal")
    case _:   # funciona como un else si lo ingresado por el usuario no coincide con el codigo
        print("el texto ingresado no es un dia de la semana") 