immutable_var = 1, 1.2, 'строка', True, [3, 4]
print(immutable_var)
# immutable_var[2] = 6
# print(immutable_var) показывает ошибку , т.к. нельзя вносить изменения в картеж
mutable_list = [5, 6.3, 'строчка', False]
mutable_list[3] = True
print(mutable_list)