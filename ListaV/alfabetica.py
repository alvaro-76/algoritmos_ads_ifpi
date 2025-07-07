
def main():
    arquivo = mapear(lambda x:x.strip(), open('br-sem-acentos.txt'))

    contador_fitlro = 0
    contador_geral = 0

    for palavra in arquivo:
        palavra = palavra.lower()

        if palavra_alfabetica(palavra):
            print(palavra)
            contador_fitlro += 1

        contador_geral += 1

    print(f'{contador_fitlro} de {contador_geral}')


def palavra_alfabetica(palavra):
    anterior = palavra[0]

    for letra in palavra:
        if anterior > letra:
            return False
        
        anterior = letra

    return True


def mapear(funcao, lista):
    nova_lista = []

    for item in lista:
        new_item = funcao(item)
        nova_lista.append(new_item)

    return nova_lista


main()