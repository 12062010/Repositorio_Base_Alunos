nome = input ("digite seu nome: ")
idade = int(input("digite sua idade: "))
possui_carteira =input("possui carteira de motorista? \n(1-sim/ 2-nao)")

if idade >= 18:
    if possui_carteira == "1":
         print("pode dirigir...MARCHA!!!")
    else:
         print("não pode dirigir !PAIZAO!!!")
else:
     print("menor de idade")