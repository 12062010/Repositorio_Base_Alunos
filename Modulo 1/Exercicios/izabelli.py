nome = input("digite seu nome: ")
altura = float(input("digite sua altura: "))
peso = float(input("digite seu peso: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("abaixo do peso")
elif imc < 24.9:
    print("peso normal")
elif imc < 29.9:
    print("sobrepeso")
elif imc < 34.9:
    print("obesidade grau I")
elif imc < 39.9:
    print("obesidade grau II")
else: 
    print("obesidade grau III (morbida)")

print(f"o nome do paciente é: {nome}\nE o imc é: {imc}")