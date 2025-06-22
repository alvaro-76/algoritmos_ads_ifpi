import utils

def main():
    qtd_otimo_pessoas = 0
    soma_regular = 0
    soma_otimo_idade = 0
    soma_bom = 0
    soma_geral = 0
    idade = 0

    while True:
        idade = int(input('Informe a idade da pessoa: '))
        if idade == -1:
            break
        opiniao = obter_opiniao('Qual sua opinião sobre o filme(1-ótimo//2-bom//3-regular//4-péssimo)? ')

        if opiniao == 1:
            soma_otimo_idade += idade
            qtd_otimo_pessoas += 1
        elif opiniao == 3:
            soma_regular += 1
        elif opiniao == 2:
            soma_bom += 1

        soma_geral += 1

    percentual_bom = (soma_bom*100)/soma_geral        
    media_idade_otimo = soma_otimo_idade / qtd_otimo_pessoas

    resultado = f'''
    Média de idade das pessoas que respondera "Ótimo": {media_idade_otimo:.1f} anos
    Quantidade de pessoas que respondeu "Regular": {soma_regular}
    Percentual de pessoas que respondeu "Bom": {percentual_bom:.1f}%
'''
    print(resultado)


def obter_opiniao(label):
    opiniao = utils.obter_inteiro_positivo(label)

    if opiniao < 0 or opiniao > 4:
        print('Dado inválido')
        return obter_opiniao(label)
    
    return opiniao

        
main()