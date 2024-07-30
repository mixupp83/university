n = int(input("Введите число от 3 до 20: "))
pairs = []
for i in range(1, n):
    for j in range(i, n):
        pairs.append((i, j))
result = ''
for pair in pairs:
    if (sum(pair) % n) == 0:
        result += str(pair[0]) + str(pair[1])
print(result)