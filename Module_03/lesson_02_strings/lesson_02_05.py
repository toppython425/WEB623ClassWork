# my_string = "Hello World! Hello Python!"
# num_o_elements = my_string.count('o')
# print(num_o_elements)
#
# print(my_string[7:16])
# num_o_elements = my_string.count('o', 7, 16)
# print(num_o_elements)
#
# num_Hello_elements = my_string.count('Hello')
# print(num_Hello_elements)
#
# num_hello_elements = my_string.lower().count('hello')
# print(num_hello_elements)
# print(my_string)

# my_string = "Hello World! Hello Python!"
# element_idx = my_string.find('W')
# print(element_idx)
# element_idx = my_string.find('Python')
# print(element_idx)
# # print(my_string[19:25])
# element_idx = my_string.find('Yello')
# print(element_idx)
# element_idx = my_string.find('Hello', 10, 20)
# print(element_idx)

# my_string = "Hello World! Hello Python! Hello Guido!"
# element_idx = my_string.rfind('e')
# print(element_idx)
# element_idx = my_string.rfind('Hello')
# print(element_idx)
# element_idx = my_string.rfind('Yello')
# print(element_idx)
# element_idx = my_string.rfind('Hello', 10, 20)
# print(element_idx)

my_string = "Hello World! Hello Python! Hello Guido!"
element_idx = my_string.index('W')
print(element_idx)
element_idx = my_string.index('Python')
print(element_idx)
# element_idx = my_string.index('Yello')
# print(element_idx)
element_idx = my_string.index('Hello', 10, 20)
print(element_idx)

my_string = "Hello World! Hello Python! Hello Guido!"
element_idx = my_string.rindex('e')
print(element_idx)
element_idx = my_string.rindex('Hello')
print(element_idx)
# element_idx = my_string.rindex('Yello')
# print(element_idx)
element_idx = my_string.rindex('Hello', 10, 20)
print(element_idx)

