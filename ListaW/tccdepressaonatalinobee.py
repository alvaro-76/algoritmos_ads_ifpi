def main():
    e, d = map(int, input().split())
    resultado = verificar(e, d)
    print(resultado)

def verificar(e, d):
    if e > d:
        return 'Eu odeio a professora!'

    diferenca = d - e

    if diferenca > 2:
        return 'Muito bem! Apresenta antes do Natal!'
    else:
        if d + 2 > 24:
            return 'Parece o trabalho do meu filho!\nFail! Entao eh nataaaaal!'
        else:
            return 'Parece o trabalho do meu filho!\nTCC Apresentado!'

main()