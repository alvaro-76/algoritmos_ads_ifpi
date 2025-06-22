
def main():
    qtd_canditadas = obter_candidatas('Informe o número de candidatas: ')

    maior_peso = None
    menor_peso = None
    

    nome_maior = None
    altura_maior = None
    nome_menor = None
    altura_menor = None

    nome_gorda = None
    nome_magra = None
    

    nome = ''
    altura = 0.00
    peso = 0

    while qtd_canditadas > 0:
        nome = obter_nome('-->  Informe o nome da candidata: ')
        altura = obter_altura('Informe a altura da candidata: ')
        peso = obter_peso('Informe o peso da candidata: ')

        if altura_maior == None or altura > altura_maior:
            altura_maior = altura
            nome_maior = nome

        if altura_menor == None or altura < altura_menor:
            altura_menor = altura
            nome_menor = nome

        if maior_peso == None or peso > maior_peso:
            maior_peso = peso
            nome_gorda = nome

        if menor_peso == None or peso < menor_peso:
            menor_peso = peso
            nome_magra = nome

        qtd_canditadas -= 1

    resultado = f'''
                RESULTADO:
Candidata mais alta: {nome_maior}, {altura_maior}m
Candidata mais baixa: {nome_menor}, {altura_menor}m
Candidata mais magra: {nome_magra}, {menor_peso}kg
Candidata mais gorda: {nome_gorda}, {maior_peso}kg
'''
    print(resultado)

def obter_candidatas(label):

    try:
        num = int(input(label))
        if num < 0:
            print('Entrada inválida')
            return obter_candidatas(label)
    except:
        print('Entrada inválida')
        return obter_candidatas(label)
    
    return num


def obter_nome(label):

    try:
        nome = input(label)
        return nome
    except:
        print('Entrada inválida')
        return obter_nome(label)


def obter_altura(label):

    try:
        altura = float(input(label))
        if altura < 0:
            print('Entrada inválda')
            return obter_altura(label)
    except:
        print('Entrada inválida')
        return obter_altura(label)
    
    return altura


def obter_peso(label):

    try:
        peso = float(input(label))
        if peso < 0:
            print('Entrada inválida')
            return obter_peso
    except:
        print('Entrada inválida')
        return obter_peso(label)
    
    return peso


main()