import utils

def main():
    soma_A = 0
    soma_B = 0
    numero_prova = None
    qtd_nadadores = None

    while True:
        numero_prova = utils.obter_inteiro_positivo('Informe o número da prova: ')
        print(f'Prova {numero_prova}:')
        qtd_nadadores = utils.obter_inteiro_positivo('Informe a quantidade de nadadores: ')
        if numero_prova == 0 and qtd_nadadores == 0:
            break
        while qtd_nadadores > 0:
        
            nome = utils.obter_string('Informe o nome do nadador: ')
            colocacao = obter_colocacao(f'-->Informe a classificação de {nome}: ')
            tempo = utils.obter_float_positivo(f'Informe o tempo de {nome}(s): ')
            clube = obter_clube(f'Informe o clube de {nome}(a//b): ').lower()

            if clube == 'a':
                pontos = calcular_pontos(colocacao)
                soma_A += pontos
            elif clube == 'b':
                pontos = calcular_pontos(colocacao)
                soma_B += pontos

            qtd_nadadores -= 1

    if soma_A > soma_B:
        vencedor = 'Clube A'
    elif soma_A < soma_B:
        vencedor = 'Clube B'
    elif soma_A == soma_B:
        vencedor = 'Empate'

    resultado = f'''
            RESULTADO
    Pontuação Clube A: {soma_A} pontos
    Pontuação Clube B: {soma_B} pontos
    Vencedor = {vencedor}
'''
    print(resultado)


def calcular_pontos(colocacao):
    if colocacao == 1:
        pontos = 9
    elif colocacao == 2:
        pontos = 6
    elif colocacao == 3:
        pontos = 4
    elif colocacao == 4:
        pontos = 3

    return pontos


def obter_clube(label):
    clube = input(label).lower()

    if clube != 'a' and clube != 'b':
        print('Entrada inválida')
        return obter_clube(label)
    
    return clube


def obter_colocacao(label):
    colocacao = int(input(label))

    if colocacao < 0 or colocacao > 4:
        print('A colocação tem que ser do 1º até o 4º')
        return obter_colocacao(label)
    
    return colocacao


main()