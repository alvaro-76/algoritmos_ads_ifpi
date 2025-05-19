#entrada
peso = float(input("Digite o peso em Kg: "))
altura = float(input("Digite a altura em metros: "))

#processamento
imc = peso / altura**2

#saida
print(f'O IMC do indivíduo é {imc:.2f}')