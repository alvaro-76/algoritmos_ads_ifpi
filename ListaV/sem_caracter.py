
def main():
    arquivo = mapear(lambda x:x.strip(), open('br-sem-acentos.txt'))

    caracter_proibido = input('Informe o carater proibido: ')

    for palavra in arquivo:
        if not tem_caracter(palavra, caracter_proibido):
            print(palavra)


def tem_caracter(palavra, caracter):
    for c in palavra:
        if c == caracter:
            return True
        
    return False


def mapear(funcao, lista):
    new_list = []

    for item in lista:
        new_item = funcao(item)
        new_list.append(new_item)

    return new_list


main()