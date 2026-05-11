#Construir una calculadora de IMC 
# por consola: pide peso y altura, calcula el IMC, muestra el 
# resultado con categoría (bajo peso / normal / sobrepeso).

peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu Altura en m: "))

imc = peso / (altura*altura)
print(f"Tu IMC es: {imc:.1f}")
if imc < 18.5:
    print("bajo peso")
elif imc >= 18.5 and imc <= 24.9:
    print("normal")
elif imc >= 25 and imc <= 29.9:
    print("sobrepeso")
elif imc >= 30:
    print("obesidad")
