
def main():
    arquivo = mapear(lambda x:x.strip(), open('br-sem-acentos.txt'))
    contador_geral = 0
    contador_filtro = 0

    letras_permitidas = input('Informe as letras permitidas: ').strip()

    for palavra in arquivo:
        if tem_letras_permitidas(palavra, letras_permitidas):
            print(palavra)
            contador_filtro += 1

        contador_geral += 1

    print(f'{contador_filtro} de {contador_geral}')


def tem_letras_permitidas(palavra, permitidas):
    for letra in palavra:
        if letra not in permitidas:
            return False
        
    return True


def mapear(funcao, lista):
    nova_lista = []

    for item in lista:
        novo_item = funcao(item)
        nova_lista.append(novo_item)

    return nova_lista


main()