
def obter_numero(label):
    try:
        num = int(input(label))
    except:
        print('INVÁLIDO')
        return obter_numero(label)
    
    return num


def obter_numero_positivo(label):
    num = obter_numero(label)

    if num < 0:
        print('INVÀLIDO')
        return obter_numero_positivo(label)
    
    return num


def obter_numero_negativo(label):
    num = obter_numero(label)

    if num > 0:
        print('INVÀLIDO')
        return obter_numero_positivo(label)
    
    return num


def obter_num_faixa(label, max, min):
    num = obter_numero(label)

    if num > max or num < min:
        print('INVÀLIDO')
        return obter_num_faixa(label, max, min)
    
    return num
