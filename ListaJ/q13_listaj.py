import utils

def main():

    salario = 0
    soma_salarios_antigos = 0
    soma_salarios_novos = 0

    while True:
        salario = utils.obter_float_positivo('Informe o salário ')
        if salario == 0:
            break

        soma_salarios_antigos += salario
        novo_salario = calcular_reajuste(salario)
        print(f'Salário reajustado: R${novo_salario:.2f}')
        soma_salarios_novos += novo_salario

    resultado = f'''
Soma dos salários antes do reajuste: R${soma_salarios_antigos:.2f}
Soma dos salários após o reajuste: R${soma_salarios_novos:.2f}
Diferença entre as folhas salariais: R${(soma_salarios_novos - soma_salarios_antigos):.2f}
'''
    print(resultado)


def calcular_reajuste(salario):
    if salario <= 2999.99:
        salario *= 1.25
    elif salario <= 5999.99:
        salario *= 1.20
    elif salario <= 9999.99:
        salario *= 1.15
    elif salario > 10000.00:
        salario *= 1.10

    return salario



main()