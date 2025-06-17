
def main():
    qtd_funcionarios = int(input('Informe a quantidade de funcionários: '))
    controle = 1

    while controle <= qtd_funcionarios:
        id_funcionario = int(input("Informe o código do funcionário: "))
        horas_trabalhadas = int(input(f'Informe a quantidade de horas trabalhdas do funcionário ID:{id_funcionario}: '))
        qtd_dependentes = int(input(f'Informe a quantidade de dependentes do funcionário ID:{id_funcionario}: '))
        salario_bruto = (horas_trabalhadas*12) + (40*qtd_dependentes)
        inss = salario_bruto * 0.085
        imposto_renda = salario_bruto * 0.05
        descontos = inss + imposto_renda
        salario_liquido = salario_bruto - descontos
        print(f'Descontos: INSS = R${inss:.2f} IR = R${imposto_renda:.2f} // Salário líquido: R${salario_liquido:.2f}')
        controle += 1

main()