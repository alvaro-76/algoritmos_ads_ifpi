import utils

def main():
    matricula = None
    soma_aprovados = 0
    soma_reprovados = 0

    while True:
        matricula = utils.obter_inteiro_positivo('Informe a matrícula do(a) aluno(a): ')
        if matricula == 0:
            break
        print(f'--> ALUNO MATRÍCULA {matricula}')
        nota1 = obter_nota(f'Informe a 1º nota do aluno {matricula}: ')
        nota2 = obter_nota(f'Informe a 2º nota do aluno {matricula}: ')
        nota3 = obter_nota(f'Informe a 3º nota do aluno {matricula}: ')

        media_final = calcular_media(nota1, nota2, nota3)
        situacao = analise(media_final).upper()

        if situacao == 'APROVADO':
            soma_aprovados += 1
        elif situacao == 'REPROVADO':
            soma_reprovados += 1

        print(f'Aluno de matricula {matricula}: {situacao}')

    resultado = f'''
        RESULTADO
Nº de alunos aprovados: {soma_aprovados}
Nº de alunos reprovados: {soma_reprovados}
'''
    print(resultado)


def obter_nota(label):
    nota = float(input(label))

    if nota < 0 or nota > 10:
        print('Informe uma nota válida(0-10)')
        return obter_nota(label)
    
    if nota == '':
        print('Entrada inválida')
        return obter_nota(label)
    
    return nota


def calcular_media(nota1, nota2, nota3):
    media = ((2*nota1)+(3*nota2)+(5*nota3))/10

    return media


def analise(media):
    if media >= 7.0:
        situacao = 'APROVADO'
    elif media < 7.0:
        situacao = 'REPROVADO'

    return situacao


main()