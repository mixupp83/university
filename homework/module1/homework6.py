my_dict = {'картофель': 'potato', 'морковь': 'carrot', 'помидор': 'tomato', 'лук': 'onion', 'перец': 'pepper',
                    'огурец': 'cucumber', 'петрушка': 'parsley'}
print(my_dict)
print(my_dict['помидор'])
print(my_dict.get('апельсин'))
my_dict.update({'капуста': 'cabbage','баклажан': 'eggplant'})
print(my_dict)
value_pop = my_dict.pop('морковь')
print('Удаленное значение:', value_pop)
print(my_dict)

my_set = {1, "два", 3.0, "два", 4, 5, "шесть", 7, 8, "девять", 10}
print(my_set)
my_set.add('десять')
my_set.add(11)
my_set.remove('девять')
print(my_set)