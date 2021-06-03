from array import array

# >>> Ranges <<<
names1 = ['Susan', 'Christopher', 'Bill']
# starting index, and number of items to retrieve
presenters = names1[0:2]

print("'names' identifier items: ", names1)
print("'presenters' identifier items", presenters)
print("#####################################################")

# >>> Lists <<<
names2 = ['Christopher', 'Susan']
scores1 = []

scores1.append(98)
scores1.append(99)

print(names2)
print(scores1)
print("#####################################################")

# >>> Dictionaries <<<
person = {'first': 'Christopher'}
person['last'] = 'Harrison'

print(person)
print(person['first'])

# >>> Arrays <<<
scores2 = array('d')
scores2.append(98)
scores2.append(94)
scores2.append(91)

print(scores2)
print("#####################################################")

# Tuples
tup1 = ("Mon", "Tue", "Wed")
tup2 = (1, 6, 7, 8)
tup3 = ("python", 30, 14.7)
tup4 = tup3 + (15,)
tup4 = tup4 + (22, 55)

print(tup1)
print(tup1[2])
print(tup2)
print(tup3)
print(tup4)

# >>> Common Operations <<<
names1 = ['Christopher', 'Susan']
print(len(names1))

names1.insert(0, 'Bill')
print(names1)
