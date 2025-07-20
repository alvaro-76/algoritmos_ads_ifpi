def main():
    while True:
        k = int(input())
        if k == 0:
            break

        n, m = map(int, input().split())  # ponto divisor

        for _ in range(k):
            x, y = map(int, input().split())  # coordenadas da casa
            print(mapear(x, y, n, m))


def mapear(x, y, n, m):
    if x == n or y == m:
        return 'divisa'
    elif x > n and y > m:
        return 'NE'
    elif x > n and y < m:
        return 'SE'
    elif x < n and y > m:
        return 'NO'
    elif x < n and y < m:
        return 'SO'


main()
