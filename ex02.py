def descendentes(arvo):
    prim = [desc[0] for desc in arvo[1]]
    segun = [desc for asc in arvo[1] for desc in descendentes(asc)]

    return prim + segun


arv = (
    "Maria",
    [
        ("Joana", [("Lucio", []), ("Jõao", [])]),
        ("Pedro", []),
        ("Patricia", [("Marina", [("Marcelo", []), ("Tomás", [])])]),
        ("Marcos", []),
    ],
)

print(descendentes(arv))
