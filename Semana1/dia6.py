# un diccionario es clave: valor
persona = {
    "nombre": "Fede",
    "edad": 30,
    "ciudad": "San Martín"
}

# acceder a un valor por su clave
print(persona["nombre"])
print(persona["edad"])

# agregar una clave nueva
persona["profesion"] = "Developer"
print(persona)

# eliminar una clave
del persona["ciudad"]
print(persona)

# cuántas claves tiene
print(len(persona))


# diccionario con lista adentro
persona = {
    "nombre": "Fede",
    "edad": 30,
    "habilidades": ["GeneXus", "Python", "SQL"]
}
print(persona["habilidades"])
print(persona["habilidades"][0])  # primera habilidad

# diccionario adentro de otro diccionario
empresa = {
    "nombre": "Globant",
    "direccion": {
        "ciudad": "Mendoza",
        "pais": "Argentina"
    }
}

print(empresa["direccion"]["ciudad"])


persona["profesion"] = None
print(persona)

# y para verificar si está vacío:
if persona["profesion"] is None:
    print("No tiene profesión")

persona = {
    "nombre": "Fede",
    "edad": 30,
    "ciudad": "San Martín",
    "profesion": "Developer"
}

# recorrer solo las claves
for clave in persona:
    print(clave)

# recorrer clave y valor juntos
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# solo los valores
for valor in persona.values():
    print(valor)

persona = {
    "nombre": "Fede",
    "edad": 30
}

# forma normal - rompe si la clave no existe
print(persona["nombre"])     # funciona
# print(persona["telefono"]) # esto tira error

# con get() - si no existe devuelve None o un valor por defecto
print(persona.get("nombre"))          # Fede
print(persona.get("telefono"))        # None, no rompe
print(persona.get("telefono", "Sin teléfono"))  # valor por defecto