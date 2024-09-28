N = 2
M = 2
array = []
array.append([1, 2, 4, 29])
array.append([3, 4, 6, 1])

for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end=" ")
    print()
print()

N = 2
M = 2
array1 = []
array1.append([1, 3, 8, 22])
array1.append([2, 9, 6, 4])

for i in range(len(array1)):
    for j in range(len(array1[i])):
        print(array1[i][j], end=" ")
    print()
print()

# Сложение матриц
result = []
for i in range(len(array)):
    row = []
    for j in range(len(array[0])):
        row.append(array[i][j] + array1[i][j])
    result.append(row)
for row in result:
    print(row)
print()

# Умножение матриц
array = []
array.append([1, 2, 3])
array.append([4, 5, 6])


array1 = []
array1.append([7, 8])
array1.append([9, 10])
array1.append([11, 12])

print(array, array1, sep="\n")
print()
result = [[0 for _ in range(len(array1[0]))] for _ in range(len(array))]

# Умножение матриц
for i in range(len(array)):
    for j in range(len(array1[0])):
        for k in range(len(array1)):
            result[i][j] += array[i][k] * array1[k][j]

# Печать результата
for row in result:
    print(" ".join(map(str, row)))


# Транспонирование матриц
def transpose(array):
    return [[array[j][i] for j in range(len(array))] for i in range(len(array[0]))]


transposed_array = transpose(array)
transposed_array1 = transpose(array1)


print("Транспонированная первая матрица:")
for row in transposed_array:
    print(row)

print("\nТранспонированная вторая матрица:")
for row in transposed_array1:
    print(row)
