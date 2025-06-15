
def has_no_e():
    arquivo = open('br-sem-acentos.txt')
    letra_proibida = input('Informe uma letra que deseja evitar: ')
    contador_geral = 0
    contador_filtro = 0
    contador_not_filtro = 0

    for linha in arquivo:
        palavra = linha.strip()
        palavra = palavra.lower()
        tem_e = False

        for carcater in palavra:
            if carcater == letra_proibida:
                tem_e = True
                contador_not_filtro += 1
                break

        if tem_e == False:
            contador_filtro += 1
            print(palavra)

        contador_geral += 1


    arquivo.close()
    filtro_porcent = (contador_filtro*100)/contador_geral
    not_filtro_porcent = (contador_not_filtro*100)/contador_geral

    print(f'Palavras filtradas: {filtro_porcent:.2f}% // palavras não filtradas: {not_filtro_porcent:.2f}% // Total: {contador_geral:.2f}')


has_no_e()