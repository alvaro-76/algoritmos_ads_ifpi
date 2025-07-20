'''QE(quociente eleitoral): (soma do número de votos válidos)/(número de cadeiras em disputa) -> atingir
o quociente eleitoral = direito a uma vaga. Sobra de vagas: (número de votos válidos do partido)/(numero de lugares obtidos + 1),
quem alcançar o maior resultado = assume a cadeira '''

import vetor_funcionalidades, os

def main():
    menu = '''
    a - Exibir partidos/coligações e seus dados
    b - Exibir vereadores e seus dados
    c - Consultar total de votos válidos
    d - Consultar quociente eleitoral
    e - Consultar votos por coligação
    0 - Sair

    Opção -> '''

    option = input(menu).lower()

    while option != '0':
        if option == 'a':
            coligacoes = vetor_funcionalidades.load_partido_coligacoes('partidos_coligacoes.csv')
            print(*coligacoes, sep='\n')

        elif option == 'b':
            vereadores = vetor_funcionalidades.load_candidatos_votos('candidatos_votos.csv')
            print(*vereadores, sep='\n')

        elif option == 'c':
            votos_validos = vetor_funcionalidades.consultar_votos_validos()
            print(f'Total de votos válidos: {votos_validos}')

        elif option == 'd':
            quociente_eleitoral = vetor_funcionalidades.calcular_quociente_eleitoral()
            print(f'Quociente eleitoral: {quociente_eleitoral}')

        elif option == 'e':
            votos_coligacao = vetor_funcionalidades.votos_coligacao()
            print(*votos_coligacao, sep='\n')
    
        input('>continue')
        os.system('cls')
        option = input(menu)

    print('Encerrando...')



main()