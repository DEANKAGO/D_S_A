# Creatinga dictionary
my_dict = dict()
print(my_dict)
my_dict2 = {}
print(my_dict2)

eng_sp = dict(one = 'uno', two = 'dos', three = 'tres')
print(eng_sp)

eng_sp2 = {'one':'uno', 'two':'dos', 'three':'tres'}
print(eng_sp2)

eng_sp_list = [('one','uno'), ('two','dos'), ('three','tres')]
eng_sp3 = dict(eng_sp_list)
print(eng_sp3)

# Traversing through a dictionary
my_dict = {'name': 'Kago', 'age': '20', 'address': 'Kenya'}
def traverseDict(dict):
    for key in dict:
        print(key, dict[key])
traverseDict(my_dict)