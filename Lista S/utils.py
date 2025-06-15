
def tamanho_caracteres(tamanho):
    arquivo = open('br-sem-acentos.txt')
    contador_geral = 0
    contador_filtro = 0
    not_contador_filtro = 0
    
    for linha in arquivo:
        palavra = linha.strip()

        if len(palavra) >= tamanho:
            contador_filtro += 1
            print(palavra)

        else:
            not_contador_filtro += 1

        contador_geral +=1

    percent_filtro = (contador_filtro*100)/contador_geral
    not_percent_filtro = (not_contador_filtro*100)/contador_geral

    print(f'Palavras filtradas: {percent_filtro:.2f}% // Palavras não filtradas: {not_percent_filtro:.2f}% // Total: {contador_geral}')


def not_caracter(letra_proibida):
    arquivo = open('br-sem-acentos.txt')
    contador_geral = 0
    contador_filtro = 0
    contador_not_filtro = 0

    for linha in arquivo:
        contador_geral += 1
        palavra = linha.strip()
        palavra = palavra.lower()

        if has_caracter(palavra, letra_proibida):
            contador_not_filtro += 1
        elif not has_caracter(palavra, letra_proibida):
            contador_filtro += 1
            print(palavra)

    percernt_filtro = (contador_filtro * 100)/contador_geral
    percernt_not_filtro = (contador_not_filtro * 100)/contador_geral
    print(f'Palavras filtradas: {percernt_filtro:.2f}% // Palavras não filtradas: {percernt_not_filtro:.2f}% // Total: {contador_geral}')


def has_caracter(palavra, letra):
    for caracter in palavra:
        if caracter == letra:
            return True
        

def caracteres_proibidos(letras_proibidas):
    arquivo = open('br-sem-acentos.txt')
    contador_filtro = 0
    contador_not_filtro = 0
    contador_geral = 0

    for linha in arquivo:
        contador_geral += 1
        palavra = linha.strip()
        palavra = palavra.lower()

        if avoids(palavra, letras_proibidas):
            contador_filtro += 1
            print(palavra)

    contador_not_filtro = contador_geral = contador_filtro
    percent_filtro = (contador_filtro*100)/contador_geral
    percent_not_filtro = (contador_not_filtro*100)/contador_geral
    print(f'Palavras filtradas: {percent_filtro:.2f}% // Palavras não filtradas: {percent_not_filtro:.2f}% // Total: {contador_geral}')


def avoids(palavra, letras_proibidas):
    for letra in palavra:
        if has_caracter(letras_proibidas, letra):
            return False
        
    return True


def apenas_letras_obrigatorias(letras_obrigatorias):
    arquivo = open('br-sem-acentos.txt')
    contador_filtro = 0
    contador_not_filtro = 0
    contador_geral = 0

    for linha in arquivo:
        contador_geral += 1
        palavra = linha.strip()
        palavra = palavra.lower()

        if uses_only(palavra, letras_obrigatorias):
            contador_filtro += 1
            print(palavra)

    contador_not_filtro = contador_geral = contador_filtro
    percent_filtro = (contador_filtro * 100)/contador_geral
    percent_not_filtro = (contador_not_filtro * 100)/contador_geral
    print(f'Palavras filtradas: {percent_filtro:.2f}% // Palavras não filtradas: {percent_not_filtro:.2f}% // Total: {contador_geral}')


def uses_only(palavra, letras_obrigatorias):
    for letra in palavra:
        if has_caracter(letras_obrigatorias, letra):
            return True
        
    return False


def todas_letras_obrigatorias(letras_obrigatorias):
    arquivo = open('br-sem-acentos.txt')
    contador_filtro = 0
    contador_not_filtro = 0
    contador_geral = 0
    
    for linha in arquivo:
        contador_geral += 1
        palavra = linha.strip()
        palavra = palavra.lower()

        if uses_all(palavra, letras_obrigatorias):
            contador_filtro += 1
            print(palavra)

    contador_not_filtro = contador_geral - contador_filtro
    percent_filtro = (contador_filtro*100)/contador_geral
    percent_not_filtro = (contador_not_filtro*100)/contador_geral
    print(f'Palavras filtradas: {percent_filtro:.2f}% // Palavras não filtradas: {percent_not_filtro:.2f}% // Total: {contador_geral}')


def uses_all(palavra, letras_obrigatorias):
    for letra in letras_obrigatorias:
        if has_caracter(palavra, letra):
            return True
        
    return False


def ordem_alfabetica():
    arquivo = open('br-sem-acentos.txt')
    contador_filtro = 0
    contador_not_filtro = 0
    contador_geral = 0

    for linha in arquivo:
        contador_geral += 1
        palavra = linha.strip()
        palavra = palavra.lower()

        if alfabetica(palavra):
            contador_filtro += 1
            print(palavra)

    contador_not_filtro = contador_geral - contador_filtro
    percent_filtro = (contador_filtro*100)/contador_geral
    percent_not_filtro = (contador_not_filtro*100)/contador_geral
    print(f'Palavras filtradas: {percent_filtro:.2f}% // Palavras não filtradas: {percent_not_filtro:.2f}% // Total: {contador_geral}')


def alfabetica(palavra):
    inicial = palavra[0]

    for i in range(1, len(palavra), 1):
        atual = palavra[i]

        if inicial > atual:
            return False
        
        inicial = atual

    return True