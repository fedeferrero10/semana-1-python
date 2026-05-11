# definir una función

def saludar(nombre):
    print (f"Hola, {nombre}!")

#llamar la funcion
saludar("Fede")
saludar("Juan")
saludar("María")

def sumar(a ,b):
    resultado = a + b
    return resultado
# guardar el resultado en una variable

total = sumar(10, 5)
print(f"La suma es: {total}")

# o usarlo directamente
print(f"La suma es: {sumar(20, 30)}")

def calcular(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    return suma, resta, multiplicacion

# opción 1: recibir todo junto
resultados = calcular(10, 5)
print(resultados)  # devuelve una tupla: (15, 5, 50)

# opción 2: desempaquetar en variables separadas
s, r, m = calcular(10, 5)
print(f"Suma: {s}, Resta: {r}, Multiplicación: {m}")

def saludar(nombre, idioma="español"):
    if idioma == "español":
        print(f"Hola, {nombre}!")
    elif idioma == "inglés":
        print(f"Hello, {nombre}!")
    elif idioma == "portugués":
        print(f"Olá, {nombre}!")

# sin pasar idioma, usa el por defecto
saludar("Fede")

# pasando idioma explícito
saludar("Fede", "inglés")
saludar("Fede", "portugués")