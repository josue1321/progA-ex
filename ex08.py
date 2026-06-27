def epar(ns):
    return [n for n in ns if n % 2 == 0]


nums = [42, 10, -5, 0, 100, 7, -12, 88]

print(epar(nums))
