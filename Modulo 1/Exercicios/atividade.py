numero = int(input("Digite o numero para a tabuada: "))
i = int(input("Digite onde a tabuada vai começar: "))
fim = int(input("Digite até qual multiplicador vai: "))


while i <= fim:
    print(f"{i} x {numero} = {i * numero}")
    i += 1