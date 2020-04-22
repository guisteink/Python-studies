from sys import getsizeof

# gerando uma lista por list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# gerando uma lista por set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# gerando uma lista por dict comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# gerando uma lista por generator expression
gen_comp = getsizeof(x * 10 for x in range(1000))

print('O porque generator expression sao mais eficientes')
print(f'Lista-list: {list_comp} bytes')
print(f'Lista-set: {set_comp} bytes')
print(f'Lista-dict: {dict_comp} bytes')
print(f'Lista-generator: {gen_comp} bytes')

#ex gen iteravel
gen = (x * 10 for x in range(10))
print('\n',gen)
print(type(gen))

for num in gen:
    print(num)



