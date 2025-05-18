#entrada
min = int(input("digite os minutos: "))

#processamento
horas = min//60
min_resto = min%60

#saida
print(f'A conversão de {min} min para horas e minutos fica: {horas}h e {min_resto} min')