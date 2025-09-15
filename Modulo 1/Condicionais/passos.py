nome = input("digite seu nome: ")
passos = float(input("difite seu passos "))

if passos > 8000:
    print("ótimo! voce se movimentou bem hoje")

else:
    print("tente se movimentar mais amanhã!")

print(f"o nome do paciente é: {nome}\nE o passo é: {passos}")
