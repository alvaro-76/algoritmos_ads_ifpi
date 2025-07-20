
def mapear(colecao, funcao):
    nova_colecao = []

    for item in colecao:
        novo_item = funcao(item)
        nova_colecao.append(novo_item)

    return nova_colecao


def filtrar(colecao, criterio):
    nova_colecao = []

    for item in colecao:
        if criterio(item):
            nova_colecao.append(item)

    return nova_colecao


def somatorio(colecao):
    somatorio = 0
    for item in colecao:
        item = int(item)
        somatorio += item

    return somatorio

''' a função load_partido_coligacoes pega o nome do arquivo, a partir dele abre o arquivo e retorna um map onde para cada nome
de partido/coligação presente na lista, cria-se um dicionario, ou seja, cada nome vira um dicionario contendo 
o nome da coligação, total de votos, de vagas e votos de sobra
'''
def load_partido_coligacoes(nome_arquivo):
    return mapear(open(nome_arquivo, encoding='utf-8').readlines(), lambda x:{
        'coligacao': x.strip(),
        'total_votos': 0,
        'qtd_vagas': 0,
        'votos_sobra': 0
    })


def load_candidatos_votos(nome_arquivo):
    candidatos = []

    try:
        with open(nome_arquivo, encoding= 'utf-8') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')

                try:
                    candidato = {
                        'nome': dados[0],
                        'numero': dados[1],
                        'partido': dados[2],
                        'coligacao': dados[3],
                        'total_votos': int(dados[4])
                    }

                    candidatos.append(candidato)
                except ValueError:
                    continue

            return candidatos
        
    except FileNotFoundError:
        print(f'ERRO! {nome_arquivo} não encontrado')
        return None
    

def consultar_votos_validos():
    try:
        candidatos = load_candidatos_votos('candidatos_votos.csv')
        votos = mapear(candidatos, lambda candidato: candidato['total_votos'])
        soma_votos = somatorio(votos)

        return soma_votos
    except ValueError:
        print('ERRO! Algum dado no campo de votos está incorreto')
        return None
    

def calcular_quociente_eleitoral():
    total_votos = consultar_votos_validos()
    qe = total_votos//29
    return qe


def votos_coligacao():
    candidatos = load_candidatos_votos('candidatos_votos.csv')
    coligacoes = list(set(mapear(candidatos, lambda candidato: candidato['coligacao'])))

    votos = []

    for coligacao in coligacoes:
        qtd_votos = 0
        for candidato in candidatos:
            if candidato['coligacao'] == coligacao:
                qtd_votos += candidato['total_votos']

        votos.append({'coligacao': coligacao, 'total_votos': qtd_votos})

    for item in votos:
        print(f"{item['coligacao']}: {item['total_votos']} votos")
        
    return votos


