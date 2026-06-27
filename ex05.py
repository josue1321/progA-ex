def filtrar(lista):
    return [nome for nome in lista if len(nome) >= 5]


nomes = ["Ana", "João", "Carlos", "Beatriz", "Guilherme", "Maria Eduarda"]

print(filtrar(nomes))
