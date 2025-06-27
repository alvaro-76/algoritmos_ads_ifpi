
def main():
    numA, numB, numC, numD = map(int, input('').split())

    somaCD = numC + numD
    somaAB = numA + numB

    if numB > numC and numD > numA and somaCD > somaAB and numC > 0 and numD > 0 and numA%2 == 0:
        print('Valores aceitos')
    else:
        print('Valores nao aceitos')
        

main()