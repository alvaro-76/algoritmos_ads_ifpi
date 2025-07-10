import utils, random

def filtrar(lista, criterio):
    nova_lista = []

    for item in lista:
        if criterio(item):
            nova_lista.append(item)

    return nova_lista


def mapear(funcao, lista):
    nova_lista = []

    for item in lista:
        novo_item = funcao(item)
        nova_lista.append(novo_item)

    return nova_lista


def reduzir(lista, funcao, item_inicial):
    reduzido = item_inicial

    for item in lista:
        reduzido = funcao(reduzido, item)

    return reduzido


def somatorio(lista):
    somatorio = 0

    for item in lista:
        somatorio += item

    return somatorio


def media(lista):

    if len(lista) == 0:
        return 0
    
    return somatorio(lista) / len(lista)


def exibir_valores_lista(lista):
    print(lista)


def resetar_vetor():
    return []


def exibir_qtd_itens(lista):
    qtd_itens = 0

    for _ in lista:
        qtd_itens += 1

    return qtd_itens


def maior_menor(lista):
    maior = lista[0]
    menor = lista[0]

    for i in range(len(lista)):
        item = lista[i]

        if item > maior:
            maior = item
        
        if item < menor:
            menor = item

    return maior, menor, lista.index(maior), lista.index(menor)

            
def exibir_positivos(lista):
    vetor_positivo = []
    qtd = 0

    for item in lista:
        if item > 0:
            vetor_positivo.append(item)
            qtd += 1
    
    return qtd, vetor_positivo


def exibir_negativos(lista):
    vetor_negativo = []
    qtd = 0

    for item in lista:
        if item < 0:
            vetor_negativo.append(item)
            qtd += 1

    return qtd, vetor_negativo

def multiplicar_lista(lista, n):
    return mapear(lambda x:x*n, lista)


def potencia_lista(lista, n):
    return mapear(lambda x:x**n, lista)


def substituir_negativos(lista):
    val_min = utils.obter_numero_positivo('Informe o valor mínimo da faixa: ')
    val_max = utils.obter_numero_positivo('Informe o valor máximo da faixa: ')

    for item in range(len(lista)):
        if lista[item] < 0:
            lista[item] = random.randint(val_min, val_max)

    return lista


def embaralhar_lista(lista):
    random.shuffle(lista)
    return lista


def adicionar_itens(vetor, qtd_itens):
    for _ in range(qtd_itens):
        vetor.append(utils.obter_numero())