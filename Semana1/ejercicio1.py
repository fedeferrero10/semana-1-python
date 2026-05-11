# Lista de personas (lista de diccionarios)
personas = [
    {"nombre": "Fede", "edad": 30, "profesion": "Developer"},
    {"nombre": "Juan", "edad": 25, "profesion": "Diseñador"},
    {"nombre": "María", "edad": 35, "profesion": "Analista"},
    {"nombre": "Carlos", "edad": 28, "profesion": None}
]

# 1. Imprimir el nombre de todas las personas

for persona in personas:
    print(persona["nombre"])

# 2. Imprimir solo las que tienen profesión definida
print("******")
for persona in personas:
    if persona["profesion"] is not None:
        print(persona["nombre"])

# 3. Imprimir cuántas personas hay en total
print(f"hay {len(personas)} personas")

numeros = [1, 2, 2, 3, 2, 4]
print(numeros.count(2))  # devuelve 3