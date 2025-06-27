
def main():
    x,y = map(float, input('').split())

    resultado = determinar_quadrante(x,y)
    print(resultado)


def determinar_quadrante(x,y):
    if x == 0 and y == 0:
        resultado = 'Origem'
    elif x == 0 and y != 0:
        resultado = 'Eixo X'
    elif x != 0 and y == 0:
        resultado = 'Eixo Y'
    elif x > 0 and y > 0:
        resultado = 'Q1'
    elif x > 0 and y < 0:
        resultado = 'Q4'
    elif x < 0 and y > 0:
        resultado = 'Q2'
    elif x < 0 and y < 0:
        resultado = 'Q3'

    return resultado


main()