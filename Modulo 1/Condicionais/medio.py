nome = input("digite o nome: ")

Nota1 = float(input("digite a primeira nota: "))
Nota2 = float(input("digite a segunda nota: "))
Nota3 = float(input("digite a terceira nota: "))

media = (Nota1 + Nota2 + Nota3) / 3

if media >= 6:
    print("aprovado")
elif media >= 4:
    print("recuperacao")
elif media <= 3:
     print("reprovado")

print(f"a media do aluno {nome} é {media}")