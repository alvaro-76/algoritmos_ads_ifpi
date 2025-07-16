
def obter_numero(label):
    try:
        num = int(input(label))
    except ValueError:
        print('INVÁLIDO')
        return obter_numero(label)
    
    return num

def obter_numero_positivo(label):
    num = obter_numero(label)

    if num < 0:
        return obter_numero_positivo(label)
    
    return num