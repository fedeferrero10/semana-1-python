# Mis primeras variables
nombre = "Fede      "
edad = 30
altura = 1.65
programador = True

print(f"Mi nombre es {nombre.strip}")
print(f"Tengo {edad} años")
print(f"Mido {altura} metros")
print(f"{nombre} tiene {edad} años y mide {altura}m")
print(programador)

nombre = "  Fede  "
print(nombre.strip())
print(nombre.strip().upper())
print(nombre.strip().lower())
print(nombre.strip().replace("e", "a"))

# Tipos de datos
print(type(nombre))
print(type(edad))
print(type(altura))
print(type(programador))

# Operaciones básicas
suma = 10 + 5
resta = 10 - 5
multiplicacion = 10 * 5
division = 10 / 5
resto = 10 % 3  # el resto de dividir 10 entre 3

print(suma)
print(resta)
print(multiplicacion)
print(division)
print(resto)