
def filtrar(colecao, criterio):
    nova_colecao = []

    for item in colecao:
        if criterio(item):
            nova_colecao.append(item)

    return nova_colecao


def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        novo_item = funcao_transformadora(item)
        nova_colecao.append(novo_item)

    return nova_colecao


def reduzir(colecao, redutora, inicial): 
    acumulado = inicial # o termo "inicial" se refere ao 1º termo da variável acumulado

    for item in colecao:
        acumulado = redutora(acumulado, item) # acumulado é o montante atual e item é o item que será acumulado

    return acumulado


def palavra_alfabetica(palavra):
    anterior = palavra[0]

    for i in range(1, len(palavra)):
        atual = palavra[i]

        if atual < anterior:
            return False
        
        anterior = atual

    return True


def obter_entrada_menu(label):
    try:
        option = int(input(label))
        if option < 0 or option > 6:
            return obter_entrada_menu(label='Insira uma entrada válida: ')
    except:
        return obter_entrada_menu(label='Insira uma entrada válida: ')
    
    return option


def obter_inteiro_positivo(label):
    try:
        n = int(input(label))
        if n < 1:
            return obter_inteiro_positivo(label='Insira uma entrada válida')
    except:
        return obter_inteiro_positivo(label='Insira uma entrada válida')
    
    return n


def char_proibido(palavra, proibido):
    for char in palavra:
        if char == proibido:
            return False
        
    return True


def abcdarian(palavra):
    anterior = palavra[0]

    for i in range(1, len(palavra)):
        atual = palavra[i]
        if anterior > atual:
            return False
        
        anterior = atual

    return True


def palavras_obrigatorias(palavra, obrigatorias):
    for letra in obrigatorias:
        if letra not in palavra:
            return False

    return True


def palavras_sem_letras(palavra, proibidas):
    for letra in palavra:
        if letra in proibidas:
            return False
        
    return True


def exibir_palavras(palavras):
    for palavra in palavras:
        print(palavra)