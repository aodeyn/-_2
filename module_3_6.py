n = 0
def calculate_structure_sum(data_structure):
    global n
    if isinstance(data_structure, int):
        n += data_structure
    elif isinstance( data_structure, str):
        n += int(len(data_structure))
    elif isinstance(data_structure, list):
        for i in range(int(len(data_structure))):
            calculate_structure_sum(data_structure[i])
    elif isinstance(data_structure, dict):
        data_structure_1 = tuple(data_structure.items())
        for k in range(int(len(data_structure_1))):
            calculate_structure_sum(data_structure_1[k])
    elif isinstance(data_structure, tuple):
        for j in range(int(len(data_structure))):
            calculate_structure_sum(data_structure[j])
    elif isinstance(data_structure, set):
        for m in data_structure:
            calculate_structure_sum(m)
    return n


data_structure = [

  [1, 2, 3],

  {'a': 4, 'b': 5},

  (6, {'cube': 7, 'drum': 8}),

  "Hello",

  ((), [{(2, 'Urban', ('Urban2', 35))}])

]
print(calculate_structure_sum(data_structure))