#entrada
print("---------------------------------------")
valor = float(input("Digite o preço do produto: R$ "))
porcentagem = float(input("Porcentagem do desconto: "))

#processamento
desconto = (valor/100) *porcentagem
valor_final = valor - desconto

#saida
print("---------------------------------------")
print(f'O valor final do produto é de R${valor_final}')
print("---------------------------------------")

