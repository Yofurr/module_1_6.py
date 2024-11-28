# Работа со словарями
my_dict = {'Dima': 1989,'Vasya': 1990, 'Masha': 1991}
print(my_dict)
print(my_dict ['Masha'])
print(my_dict.get('Kostik'))
my_dict['Stepan']=1995
print(my_dict)

my_dict.update({'Afanasiy': 1934,
                'Johan': 1662})
print(my_dict)

a = my_dict.pop('Vasya')
print(a)
print(my_dict)

# Работа с множествами
my_set = {1, 2.2, True, 'Mouse', 1, 2.2, 2.2, 1, 'Mouse'}
print(my_set)
my_set.update({(1,2,3), 'Lera'})
my_set.discard(2.2)
print(my_set)
