
def main():
    salario = float(input('Informe o salário(R$): '))
    
    taxa = 0
    if salario <= 280:
        taxa = 20
    elif salario <= 700:
        taxa = 15
    elif salario <= 1500:
        taxa = 10
    elif salario > 1500:
        taxa = 5

    salario_reajustado = reajuste(salario)
    aumento = salario_reajustado - salario
    
    resultado = f'''
    Salário antes do reajuste: R${salario:.2f}
    Percentual de aumento aplicado: {taxa}%
    Valor do aumento: R${aumento:.2f}
    Novo salário: R${salario_reajustado:.2f}
'''
    print(resultado)


def reajuste(salario):
    if salario <= 280:
        new_salario = salario*1.20
    elif salario <= 700:
        new_salario = salario*1.15
    elif salario <= 1500:
        new_salario = salario*1.10
    elif salario > 1500:
        new_salario = salario * 1.05

    return new_salario

main()