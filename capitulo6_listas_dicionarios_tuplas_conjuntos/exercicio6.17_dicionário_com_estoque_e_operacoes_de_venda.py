# Exercício 6.17 - Dicionário com estoque e operações de venda.
estoque = {"tomate": [1000, 2.30],
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijão": [100, 1.50]}
total = 0
while True:
    produto = input("Informe o produto (parar para sair): ")
    
    if produto == "parar":
        break
    if produto in estoque:
        quantidade = int(input("Informe a quantidade desse produto "))
        if quantidade <= estoque[produto][0]:
            preco = estoque[produto][1]
            custo = preco * quantidade
            print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
            preco = estoque[produto][1]
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print("quantidade solicitada não disponível")
    else:
        print("Nome do produto inválido")
print(f"Custo total: {total:.2}\n")
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")
    
    