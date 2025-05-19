#entrada
dist = int(input("Digite a distância da vaigem(em metros): "))
vel = int(input("Digite a velocidade média da viagem(m/s): "))

#processamento
tempo = dist/vel

#saida
print(f'A duração da viagem foi de cerca de {tempo:.1f} segundos')
