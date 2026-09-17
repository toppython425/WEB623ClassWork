example_list_str = ['Drama', 'Comedy', 'Fantasy']
example_list_int = [1, 2, 3]
example_list_float = [1.5, 2.5, 3.5]
example_list_list = [['Drama', 'Comedy', 'Fantasy'], [1, 2, 3]]
example_list_dict = [{'key1': 'value1'}, {1: 1050}]


class ExampleClass:
    def __init__(self):
        pass


ex_obj = ExampleClass()
example_list_mix = ['Drama', 2.5, 1, ['Drama', 'Comedy', 'Fantasy'], {'key1': 'value1'}, ex_obj]
print(example_list_mix)

example_list_str_01 = ['Drama', 'Comedy', 'Fantasy', 'Drama', 'Comedy', 'Fantasy']
print(example_list_str_01, len(example_list_str_01))
example_list_set = set(example_list_str_01)
print(example_list_set, len(example_list_set))
unique_list = list(example_list_set)
print(unique_list)