def pegletra(ps):
    return [c for p in ps for c in p]


palavras = ["python", "java"]

print(pegletra(palavras))
