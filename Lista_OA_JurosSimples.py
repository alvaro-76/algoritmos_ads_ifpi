#entrada
capital = float(input("Digite o capital inicial: "))
taxa = float(input("Digite a taxa da aplicação: "))
tempo = int(input("Digite a quatnidade de meses da aplicação: "))

#processamento
juros = capital * taxa * tempo
montante = juros + capital

#saida
print(f'O montate ao final da aplicação será de R${montante}')