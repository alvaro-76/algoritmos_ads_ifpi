
def obter_inteiro_positivo(label):
    try:
        num = int(input(label))
        if num < 0:
            print('Entrada inválida')
            return obter_inteiro_positivo(label)
    except:
        print('Entrada inválida')
        return obter_inteiro_positivo(label)
    
    return num


def obter_inteiro(label):
    try:
        num = int(input(label))
    except:
        print('Entrada inválida')
        return obter_inteiro(label)
    
    return num 


def obter_float_positivo(label):
    try:
        num = float(input(label))
        if num < 0:
            print('Entrada inválida')
            return obter_float_positivo(label)
    except:
        print('Entrada inválida')
        return obter_float_positivo(label)
    
    return num


def obter_string(label):
    try:
        nome = input(label)
        if nome == '':
            print('Entrada inválida')
            return obter_string(label)
    except:
        print('Entrada inválida')
        return obter_string(label)
    
    return nome
        