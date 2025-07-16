
def load_arquivo(nome_arquivo):
    escolas = []
    arquivo = open(nome_arquivo)

    try:
        for linha in arquivo:
            dados = linha.strip().split(';')
            escola = {}
            escola['ranking'] = dados[0]
            escola['nome'] = dados[1]
            escola['municipio'] = dados[2]
            escola['uf'] = dados[3]
            escola['rede'] = dados[4]
            escola['permanencia'] = dados[5]
            escola['nivel_socio_economico'] = dados[6]
            escola['media_objetivas'] = dados[7]
            escola['linguagens'] = dados[8]
            escola['matematica'] = dados[9]
            escola['ciencias_natureza'] = dados[10]
            escola['humanas'] = dados[11]
            escola['redacao'] = dados[12]

            escolas.append(escola)
    except FileNotFoundError:
        print(f'ERRO! Arquivo {nome_arquivo} não encontrado.')
        return None
    
    arquivo.close()
    return escolas


def filtrar(colecao, criterio):
    nova_colecao = []

    for item in colecao:
        if criterio(item):
            nova_colecao.append(item)

    return nova_colecao


def mapear(colecao, funcao):
    nova_colecao = []

    for item in colecao:
        novo_item = funcao(item)
        nova_colecao.append(novo_item)

    return nova_colecao


def reduzir(colecao, funcao, item_inicial):
    reduzido = item_inicial

    for item in colecao:
        reduzido = funcao(reduzido, item)

    return reduzido


def somatorio(colecao):
    somatorio = 0

    for item in colecao:
        somatorio += item

    return somatorio


def topn_brasil(escolas, n):
    top_escolas = []

    escolas_ordenadas = sorted(escolas, key=lambda x:float(x['media_objetivas'].replace(',', '.')), reverse=True)

    for i in range(min(n, len(escolas_ordenadas))):
        escola = escolas_ordenadas[i]
        top_escolas.append(escola['nome'])

    return top_escolas


def topn_brasil_area(escolas, area, n):
    try:
        top_escolas = []

        escolas_ordenadas = sorted(escolas, key=lambda x:float(x[area].replace(',', '.')), reverse=True)

        for i in range(min(n, len(escolas_ordenadas))):
            escola = escolas_ordenadas[i]
            top_escolas.append(escola['nome'])

        return top_escolas
    except:
        return ['INVÁLIDO']


def topn_estado(escolas, estado, n):
    escolas_estado = filtrar(escolas, lambda escola: escola['uf'] == estado)

    return topn_brasil(escolas_estado, n)


def top_estados_rede(escolas, estado, rede, n):
    escolas_estado = filtrar(escolas, lambda escola: escola['uf'] == estado)
    escolas_rede = filtrar(escolas_estado, lambda escola: escola['rede'] == rede)

    return topn_brasil(escolas_rede, n)


def media_nacional_area(escolas, area):
    try:

        escolas_filtradas = filtrar(escolas, lambda escola: escola[area])
        escolas_filtradas = mapear(escolas_filtradas, lambda x: float(x[area].replace(',', '.')))

        media = somatorio(escolas_filtradas)/len(escolas_filtradas)

        return f'{media:.2f}'
    except KeyError:
        return ['INVÁLIDO']


def melhor_escola_area_estado(escolas, area, estado):
    escolas_estado = filtrar(escolas, lambda escola: escola['uf'] == estado)
    melhor_escola = topn_brasil_area(escolas_estado, area, n=1)

    return melhor_escola


def ordenar_estado_renda(escolas, estado):
    resultado = []

    escolas_estado = filtrar(escolas, lambda escola: escola['uf'] == estado)
    escolas_validas = filtrar(escolas_estado, lambda escola: escola['nivel_socio_economico'] != 'Sem informação')
    escolas_ordenadas = sorted(escolas_validas, key= lambda x: x['nivel_socio_economico'], reverse= True)

    for i in range(len(escolas_ordenadas)):
        escola = escolas_ordenadas[i]
        resultado.append(escola['nome'])

    return resultado


def menu_areas():
    menu = '''
            * Digite exatamente conforme está escrito
    - linguagens
    - matematica
    - ciencias_natureza
    - humanas
    - redacao

    -> '''

    return menu


def procurar_nome(escolas, parte_nome):
    nomes_escolas = []

    for escola in escolas:
        nomes_escolas.append(escola['nome'])

    escolas_filtradas = []

    for nome in nomes_escolas:
        if parte_nome in nome:
            escolas_filtradas.append(nome)

    return escolas_filtradas


def ranking_enem_estado(escolas, estado):
    ranking = []

    escolas_estado = filtrar(escolas, lambda escola: escola['uf'] == estado)

    escolas_ordenadas = sorted(escolas_estado, key=lambda x:float(x['ranking'].replace(',', '.')))

    for i in range(len(escolas_ordenadas)):
        escola = escolas_ordenadas[i]
        ranking.append(escola['nome'])

    return ranking


def ranking_enem_regiao(escolas, estado, n):
    resultado = []

    regioes = {
        'regiao_norte': ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'],
        'regiao_nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
        'regiao_sudeste': ['ES', 'MG', 'RJ', 'SP'],
        'regiao_centroeste': ['GO', 'MT', 'MS', 'DF'],
        'regiao_sul': ['PR', 'SC', 'RS']
    }

    regiao_escolhida = None
    for regiao, estados in regioes.items():
        if estado in estados:
            regiao_escolhida = regiao
            break

    if not regiao_escolhida:
        return ['Estado não encontrado']

    estados_regiao = regioes[regiao_escolhida]
    escolas_regiao = filtrar(escolas, lambda escola: escola['uf'] in estados_regiao)
    escolas_ordenadas = sorted(escolas_regiao, key= lambda x: float(x['media_objetivas'].replace(',', '.')), reverse=True)[:n]

    for i in range(len(escolas_ordenadas)):
        escola = escolas_ordenadas[i]
        resultado.append(escola['nome'])

    return resultado


        
    