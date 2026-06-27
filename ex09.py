def primo(n):
    return [
        p for p in range(2, n + 1) if sum([1 for x in range(2, p) if p % x == 0]) == 0
    ]


print(primo(20))
