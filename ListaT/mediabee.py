
def main():
    n1,n2,n3,n4 = map(float, input('').split())

    media = calcular_media(n1,n2,n3,n4)
    print(f'Media: {media:.1f}')

    if media >= 7.0:
        print('Aluno aprovado.')
    elif media < 5.0:
        print('Aluno reprovado.')
    elif media >= 5.0 and media < 6.9:
        print('Aluno em exame.')
        nota_exame = float(input('Nota do exame: '))
        nova_media = (nota_exame + media)/2
        if nova_media >= 5.0:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')
        print(f'Media final: {nova_media:.1f}')


def calcular_media(n1,n2,n3,n4):
    media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10

    return media

main()