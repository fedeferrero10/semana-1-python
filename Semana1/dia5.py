# crear una lista
frutas = ["manzana", "naranja", "uva", "pera"]

# acceder por índice (arranca en 0)
print(frutas[0])  # manzana
print(frutas[2])  # uva
print(frutas[-1]) # el último: pera

# agregar un elemento
frutas.append("banana")
print(frutas)

# eliminar un elemento
frutas.remove("naranja")
print(frutas)

# cuántos elementos tiene
print(len(frutas))


# recorrer con índice y valor a la vez
for i, fruta in enumerate(frutas):
    print(f"{i} - {fruta}")

# lista de números y operaciones útiles
numeros = [3, 7, 1, 9, 4, 6, 2]

print(min(numeros))   # el menor
print(max(numeros))   # el mayor
print(sum(numeros))   # la suma de todos
print(sorted(numeros)) # ordenada de menor a mayor

print(sorted(numeros, reverse=True))