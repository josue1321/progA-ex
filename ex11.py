def qntpassou(ns):
    return sum([1 for n in ns if n >= 5])


notas = [8.5, 9.0, 4.5, 10.0, 6.0, 3.0, 7.5, 5.5, 8.0, 2.5]

print(qntpassou(notas))
