#entrada
num = int(input("Digite um número de 3 digitos: "))

#processamento
centena = num//100
dezena = (num%100)//10
unidade = (num%100)%10

#saida
print(f'O {num} invertido é {unidade}{dezena}{centena}')