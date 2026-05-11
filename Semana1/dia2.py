edad = 15

if  edad >= 18:
    print("Sos mayor de edad")
else:
    print("Sos menor de edad")

nota = 60
if nota >= 90:
    print("Sobresaliente")
elif nota >= 75:
    print("Muy bueno")
elif nota >= 60:
    print ("Regular")
else:
    print ("Desaprobado")

#Do case
dia = "viernes"

match dia:
    case "lunes":
        print("Inicio de semana")
    case "viernes":
        print("Por fin viernes")
    case "sabado" | "domingo":
        print("Fin de semana")
    case _:
        print("Día normal")