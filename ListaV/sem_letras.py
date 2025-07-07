
def main():
    arquivo = mapear(lambda x:x.strip(), open('br-sem-acentos.txt'))
    contador_geral = 0
    contador_filtro = 0

    letras_proibidas = input('Informe as letras proibidas: ').strip()

    '''
    USANDO UMA FUNÇÃO ESPECÍFICA PARA VERIFICAR SE HÁ LETRAS PROIBIDAS NA PALAVRA
    for palavra in arquivo:
        if not tem_letras_proibidas(palavra, letras_proibidas):
            print(palavra)
            contador_filtro += 1

        contador_geral += 1'''
    
    #USANDO FUNÇÃO GENÉRICA QUE VERIFICA SE HÁ LETRAS ESPECÍFICAS NA PALAVRA
    for palavra in arquivo:
        palavra = palavra.lower() #DEIXA TODAS AS PALAVRAS COM LETRA MINÚSCULA PARA GENERALIZAR
        if not tem_letras(palavra, letras_proibidas):
            print(palavra)
            contador_filtro += 1

        contador_geral += 1

    print(f'{contador_filtro} de {contador_geral}')


'''-> FUNÇÃO ESPECÍFICA PARA VERIFICAR SE HÁ LETRAS PROIBIDAS NA PALAVRA:
def tem_letras_proibidas(palavra, letras_proibidas): 
    for c in palavra:
        if c in letras_proibidas:
            return True
        
    return False'''

#-> FUNÇÃO GENÉRICA:
def tem_letras(palavra, letras):
    for letra in palavra:
        if letra in letras:
            return True
        
    return False


def mapear(funcao, lista):
    nova_lista = []

    for item in lista:
        novo_item = funcao(item)
        nova_lista.append(novo_item)

    return nova_lista


main()