# función que recibe un diccionario
def mostrar_persona(persona):
    nombre = persona.get("nombre", "Sin nombre")
    edad = persona.get("edad", "Sin edad")
    profesion = persona.get("profesion", "Sin profesión")
    print(f"{nombre} - {edad} años - {profesion}")

# función que filtra una lista de diccionarios
def filtrar_con_profesion(personas):
    resultado = []
    for persona in personas:
        if persona["profesion"] is not None:
            resultado.append(persona)
    return resultado

# datos
personas = [
    {"nombre": "Fede", "edad": 30, "profesion": "Developer"},
    {"nombre": "Juan", "edad": 25, "profesion": "Diseñador"},
    {"nombre": "María", "edad": 35, "profesion": "Analista"},
    {"nombre": "Carlos", "edad": 28, "profesion": None}
]

# usar las funciones
print("--- Todas ---")
for persona in personas:
    mostrar_persona(persona)

print("--- Con profesión ---")
con_profesion = filtrar_con_profesion(personas)
for persona in con_profesion:
    mostrar_persona(persona)


# forma larga (la que ya conocés)
con_profesion = []
for persona in personas:
    if persona["profesion"] is not None:
        con_profesion.append(persona)

# forma corta con list comprehension
con_profesion = [persona for persona in personas if persona["profesion"] is not None]

print(con_profesion)