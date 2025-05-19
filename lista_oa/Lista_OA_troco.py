#entrada
valor = int(input("Digite o valor a ser trocado: "))

#processamento
notas50 = valor//50
new_valor = valor - notas50*50
notas10 = new_valor//10

#saida
print(f'O valor de R${valor} pode ser trocado em {notas50} nota(s) de 50 e {notas10} nota(s) de 10')