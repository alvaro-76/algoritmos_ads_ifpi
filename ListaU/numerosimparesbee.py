
def main():
    varX = int(input(''))
    qtd_impar = 0

    while qtd_impar < 6:
        if verificar_impar(varX):
            print(varX)
            qtd_impar += 1
        varX += 1
        

def verificar_impar(var):
    if var%2 != 0:
        return True
    

main()