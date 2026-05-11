# for: recorre una secuencia
frutas = ["manzana", "naranja", "uva", "pera"]

for fruta in frutas:
    print(fruta)

# range: repite N veces
for i in range(5):
    print(i)

print("--- desde 1 hasta 5 ---")
for i in range(1, 6):
    print(i)

print("--- de 2 en 2 ---")
for i in range(0, 10, 2):
    print(i)

print("--- al revés ---")
for i in range(5, 0, -1):
    print(i)

# while: repite mientras se cumpla una condición
contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

print("Terminó el bucle")