
def main():
    a, b, c = map(float, input('').split())

    resultado = calcular_baskhara(a,b,c)
    print(resultado)


def calcular_baskhara(a,b,c):
    delta = (b**2)-4*a*c
    if a == 0 or delta == 0:
        resultado = 'Impossivel calcular'
    else:
        raiz_delta = delta**0.5
        r1 = ((-1*b)+raiz_delta)/(2*a)
        r2 = ((-1*b)-raiz_delta)/(2*a)
        resultado = f'R1 = {r1:.5f}\nR2 = {r2:.5f}'

    return resultado


main()