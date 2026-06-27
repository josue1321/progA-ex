def contar(textos):
    return [(sum([1 for c in txt])) for txt in textos]


textos = ["python", "java", "javascript", "c"]

print(contar(textos))
