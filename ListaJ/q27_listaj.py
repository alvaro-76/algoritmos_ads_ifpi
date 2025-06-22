import utils 

def main():
    soma_idade_mulheres = 0
    qtd_mulheres = 0
    soma_idade_homens = 0
    qtd_homens = 0
    qtd_homens_solteiros = 0
    qtd_mulheres_solteiras = 0
    qtd_mulheres_divorciadas_acima_trinta = 0
    
    qtd_pessoas = utils.obter_inteiro_positivo('Informe a quantidade de pessoas que serão analisadas: ')
    controle = 1

    while controle <= qtd_pessoas:
        sexo = obter_sexo(f'Informe o sexo da {controle}º pessoa(1=masc//2=fem): ')
        idade = utils.obter_inteiro_positivo(f'Informe a idade da {controle}º pessoa: ')
        estado_civil = obter_estado_civil(f'Informe o estado civil da {controle}º pessoa((1=Casado, 2=Solteiro, 3=Divorciado, 4=Viúvo)): ')

        if sexo == 1:
            soma_idade_homens += idade
            qtd_homens += 1
            if estado_civil == 2:
                qtd_homens_solteiros += 1
        elif sexo == 2:
            soma_idade_mulheres += idade
            qtd_mulheres += 1
            if estado_civil == 2:
                qtd_mulheres_solteiras += 1
            if estado_civil == 3 and idade > 30:
                qtd_mulheres_divorciadas_acima_trinta += 1

        controle += 1

    media_idade_mulheres = soma_idade_mulheres / qtd_mulheres if qtd_mulheres > 0 else 0
    media_idade_homens = soma_idade_homens / qtd_homens if qtd_homens > 0 else 0
    
    percentual_homens_solteiros = (qtd_homens_solteiros * 100) / qtd_homens if qtd_homens > 0 else 0
    percentual_mulheres_solteiras = (qtd_mulheres_solteiras * 100) / qtd_mulheres if qtd_mulheres > 0 else 0

    resultado = f'''
Média de idade das mulheres: {media_idade_mulheres:.1f}
Média de idade dos homens: {media_idade_homens:.1f}
Percentual de homens solteiros: {percentual_homens_solteiros:.2f}%
Percentual de mulheres solteiras: {percentual_mulheres_solteiras:.2f}%
Quantidade de mulheres divorciadas acima dos 30 anos: {qtd_mulheres_divorciadas_acima_trinta}
'''
    print(resultado)

def obter_sexo(label):
    sexo = utils.obter_inteiro_positivo(label)
    if sexo not in (1, 2):
        print('Dado inválido')
        return obter_sexo(label)
    return sexo

def obter_estado_civil(label):
    estado_civil = utils.obter_inteiro_positivo(label)
    if estado_civil not in (1, 2, 3, 4):
        print('Dado inválido')
        return obter_estado_civil(label)
    return estado_civil

main()