
# Solutions to additional exercises.


###
greetings_strings = ['hello', 'bye', 'later']
print(greetings_strings[0])
print(greetings_strings[1][2])

###
print([greetings_strings[idx] for idx in [0, 2]])
print([greetings_strings[0][idx] for idx in [0, 2, 4]])
print([greetings_strings[0][idx] for idx in range(0,4,2)])

###
[number**2 for number in range(10)]
[str(number**2) for number in range(10)]

###
list_of_species = ['Homo sapiens', 'Escherichia Coli', 'Pan troglodytes', 'Canis lupus', 'Felis catus'] 
new_list = [X.replace('e','') for X in list_of_species]
print(new_list)