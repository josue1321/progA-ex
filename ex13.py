def epositivo(m):
    return [n for row in m for n in row if n > 0]


matriz = [
    [10, -2, 15, 8, 22],
    [4, 8, -1, 20, 3],
    [7, 12, 5, -3, 19],
    [25, 11, 6, 14, 30],
    [-5, 18, 21, 9, -7],
]

print(epositivo(matriz))
