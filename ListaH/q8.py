#descontos: Imposto de renda; 3% - sindicato; fgts-11%(mas a empresa que paga); entrada - valor da hora e qtd de horas
def main():
    valor_hora = float(input('Informe o valor(R$) da hora: '))
    qtd_horas = int(input('Informe a quantidade de horas trabalhadas no mês: '))

    calcular_salario(valor_hora, qtd_horas)


def calcular_salario(valor, horas):
    salario_bruto = valor * horas

    valor_ir = imposto_renda(salario_bruto)
    inss = salario_bruto * 0.10
    fgts = salario_bruto * 0.11
    descontos = valor_ir + inss
    salario_liquido = salario_bruto - descontos

    resultado = f'''
Salario bruto: ({valor}x{horas}): R${salario_bruto:.2f}
(-) IR (5%): R${valor_ir:.2f}
(-) INSS (10%): R${inss:.2f}
FGTS (11%): R${fgts:.2f}
Total de descontos: R${descontos:.2f}
Salário líquido: R${salario_liquido:.2f}
    '''
    print(resultado)


def imposto_renda(salario):
    if salario <= 900:
        salario = salario
    elif salario <= 1500:
        salario *= 0.05
    elif salario <= 2500:
        salario *= 0.10
    elif salario > 2500:
        salario *= 0.20

    return salario

main()