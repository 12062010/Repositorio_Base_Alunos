cadastro = []

def cadastrar(cadastro):
    nome = input("digite o nome: ")
    cadastro.append(nome)
    print(f"usuario{nome} cadastrado !")

def listar(cadastro):
    for i, nome in enumerate(cadastro, start=1):
        print (f"{i}. {nome} ")
def excluir(cadastro):
    nome = input("digite o nome: ")
    cadastro.remove(nome)
    print(f"usuario {nome} excluido !")

while True:
    print("1 - cadastrar usuario")
    print("2 - listar usuario")
    print("3 - remover usuario")
    print("0 - sair")
    opção = input("digite a opção: ")

    if opção == "1":
        cadastrar(cadastro)

    elif opção == "2":
        listar(cadastro)

    elif opção == "3":
        excluir(cadastro)
    elif opção == "0":
        break

    

    
