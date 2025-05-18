#entrada
area = int(input("Informe a dimensão da área a ser pintada: "))
area_lata = int(input("Digite a área que uma lata de tinta consegue pintar: "))

#processamento
numeroLatas = area/area_lata

#saida
print(f'Serão necessárias {numeroLatas} latas de tinta para pintas essa área')