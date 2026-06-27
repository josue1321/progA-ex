def count(texto):
    return sum([1 for charac in texto if charac in "aeiouAEIOU"])


texto = "abiruleibe"

print(count(texto))
