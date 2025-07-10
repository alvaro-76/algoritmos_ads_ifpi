import utils, random, vetor_utils

def inicializar_vetor_numerico():
    menu = '''
    >Construir vetor
1 - Vetor automático
2 - Informe os valores do vetor
3 - Carregar arquivo
0 - Sair

Opção -> '''

    option = utils.obter_numero_positivo(menu)

    while option != 0:
        
        if option == 1:
            return gerar_vetor_automatico()
        elif option == 2:
            return gerar_vetor_manual()
        elif option == 3:
            return gerar_vetor_arquivo()
        

def gerar_vetor_automatico():
    vetor = []

    tam = utils.obter_numero_positivo('Informe o tamanho do vetor: ')

    val_max = utils.obter_numero('Informe o valor máximo do vetor: ')
    val_min = utils.obter_numero('Informe o valor mínimo do vetor: ')

    for _ in range(tam):
        vetor.append(random.randint(val_min, val_max))

    return vetor


def gerar_vetor_manual():
    vetor = []

    tam = utils.obter_numero_positivo('Informe o tamanho do vetor: ')

    val_max = utils.obter_numero('Informe o valor máximo do vetor: ')
    val_min = utils.obter_numero('Informe o valor mínimo do vetor: ')

    for i in range(tam):
        print(f'Item nº {i+1}')
        valor = utils.obter_num_faixa('Informe o valor a ser adicionado ao vetor: ', val_max, val_min)
        vetor.append(valor)

    return vetor


def gerar_vetor_arquivo():
    vetor = []

    nome_arquivo = input('Informe o nome do arquivo da forma correta: ')

    try:
        with open(nome_arquivo) as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    numeros = linha.split()
                    for n in numeros:
                        vetor.append(int(n))

    except FileNotFoundError:
        print('Arquivo não encontrado')

    except ValueError:
        print('Dados inválidos no arquivo')

    return vetor


def atualizar_vetor(vetor):

    menu = '''
    >Atualizar vetor
1 - Multiplicar por um valor
2 - Elevar a um valor
3 - Reduzir a uma fração
4 - Substituir valores negativos por um número aleatório de uma faixa
5 - Inverter valores
6 - Embaralhar valores
0 - Sair

Opção -> '''

    option = utils.obter_numero_positivo(menu)

    if option == 1:
        num = utils.obter_numero('Informe o valor a ser multiplicado: ')
        return vetor_utils.multiplicar_lista(vetor, num)
    
    elif option == 2:
        num = utils.obter_numero('Informe o valor da potência: ')
        return vetor_utils.potencia_lista(vetor, num)
    
    elif option == 3:
        numerador, denominador = map(int, input('Informe a fração: ').split('/'))
        fator = numerador/denominador
        return vetor_utils.multiplicar_lista(vetor, fator)
    
    elif option == 4:
        return vetor_utils.substituir_negativos(vetor)
    
    elif option == 5:
        escolhas = '''
        >Escolhas como ordenar a lista
    1 - Ordenar normalmente
    2 - Ordenar de forma inversa

    - > '''
        escolha = utils.obter_numero_positivo(escolhas)

        if escolha == 1:
            vetor.sort()
            return vetor
        
        elif escolha == 2:
            vetor.sort(reverse= True)
            return vetor
    
    elif option == 6:
        return vetor_utils.embaralhar_lista(vetor)
    
    elif option == 0:
        return vetor
    

def adicionar_itens(vetor):
    qtd_itens = utils.obter_numero_positivo('Informe quantos itens deseja adicionar: ')

    for _ in range(qtd_itens):
        vetor.append(utils.obter_numero('Informe o valor a ser adicionado: '))

    return vetor


def remover_itens_exatos(vetor):
    qtd_itens = utils.obter_numero_positivo('Informe quantos itens deseja remover: ')

    for _ in range(qtd_itens):
        valor = utils.obter_numero('Informe o valor a ser removido: ')
        if valor in vetor:
            vetor.remove(valor)

    return vetor


def remover_itens_posicao(vetor):
    qtd_itens = utils.obter_numero_positivo('Informe quantos itens deseja remover: ')

    for _ in range(qtd_itens):
        indice = utils.obter_numero('Informe o índice do número a ser removido(1º termo = índice[0]): ')
        try:
            vetor.pop(indice)
        except IndexError:
            print('Não há este índice')

    return vetor


def editar_valor_posicao(vetor):
    qtd_itens = utils.obter_numero_positivo('Informe quantos itens deseja editar: ')

    for i in range(qtd_itens):
        indice = utils.obter_numero('Informe o índice que deseja editar: ')

        try:
            print(f'{i+1}º item')
            novo_valor = utils.obter_numero(f'Informe o novo valor para o índice [{indice}]: ')
            vetor[indice] = novo_valor
        except IndexError:
            print('Não há este índice')

    return vetor


def salvar_valores_arquivo(vetor):
    nome_arquivo = input('Informe o nome do arquivo(coloque ".txt" no final): ')

    with open(nome_arquivo, 'w') as arquivo:
        for valor in vetor:
            arquivo.write(str(valor) + '\n')

    print('Arquivo salvo com sucesso!')