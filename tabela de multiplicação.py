#tabela de multiplacação

print("Tabela de Multiplicação")
num = int(input("Digite um número para ver a tabela de multiplicação: "))
print(f"Tabuada do {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
else:
    print("Fim da tabela de multiplicação.")