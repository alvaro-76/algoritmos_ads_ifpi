
def main():
    arquivo = mapear(lambda x:x.strip(), open('br-sem-acentos.txt'))
    contador_geral = 0
    contador_filtro = 0

    letras_obrigatorias = input('Informe as letras obrigatórias: ')

    for palavra in arquivo:
        palavra = palavra.lower()

        if tem_letras_obrigatorias(palavra, letras_obrigatorias):
            print(palavra)
            contador_filtro += 1

        contador_geral += 1

    print(f'{contador_filtro} de {contador_geral}')


def tem_letras_obrigatorias(palavra, obrigatorias):
    for letra in obrigatorias:
        if letra not in palavra:
            return False
        
    return True


def mapear(funcao, lista):
    nova_lista = []

    for item in lista:
        new_item = funcao(item)
        nova_lista.append(new_item)

    return nova_lista


main()