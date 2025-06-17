
def main():
    i = 1

    while i <= 10:
        j = 1
        print(f'Tabuada do {i}:')
        while j <= 10:
            print(f'{i} X {j}: {i*j}')
            j +=1
        i += 1

main()