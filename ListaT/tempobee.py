
def main():
    hora_inicial, min_inicial, hora_final, min_final = map(int, input('').split())

    resultado_horas, resultado_minutos = calcular_hora(hora_inicial, min_inicial, hora_final, min_final)

    print(f'O JOGO DUROU {resultado_horas} HORA(S) E {resultado_minutos} MINUTO(S)')


def calcular_hora(hora_inicial, min_inicial, hora_final, min_final):
    inicio = hora_inicial * 60 + min_inicial
    fim = hora_final * 60 + min_final

    duracao = fim - inicio

    if duracao <= 0:
        duracao += 24 * 60

    horas = duracao //60
    minutos = duracao % 60

    return horas, minutos

main()