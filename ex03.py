def achatar(array):
    return [n for x in array for n in (achatar(x) if isinstance(x, list) else [x])]


print(achatar([1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]))
