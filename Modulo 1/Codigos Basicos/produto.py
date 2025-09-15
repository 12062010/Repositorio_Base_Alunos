nome_produto = input("digite  o nome do produto:")
preco = float(input("digite o preço do produto: R$"))
desconto = float(input("digite o percentual de descdonto %: "))
                        
valor_desconto = preco * desconto / 100

preco_final = preco - valor_desconto
print("------------------")
print(f"produto: {nome_produto}\n preço final: {preco_final}")
print("------------------")