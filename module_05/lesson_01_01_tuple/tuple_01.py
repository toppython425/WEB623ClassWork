# my_tuple_01 = ('Cat', 'Turtle', 'Snake', 'Dog')
# my_tuple_02 = 'Cat', 'Turtle', 'Snake', 'Dog'
# print(my_tuple_01 == my_tuple_02)
#
# my_list = ['Cat', 'Turtle', 'Snake', 'Dog']
# my_tuple_03 = tuple(my_list)
# print(my_tuple_03, type(my_tuple_03))
#
# my_tuple_04 = ('Cat',)
# my_tuple_05 = 'Cat',
# print(my_tuple_04, my_tuple_05)
#
# animal1, animal2, animal3, animal4 = my_tuple_01
# print(animal1)
# print(animal4)
#
# animal1, animal2 = animal2, animal1
# print(animal1)
# print(animal2)

# my_tuple_01 = ('Cat', 'Turtle', 'Snake', 'Dog')
# print(my_tuple_01[1])
# print(my_tuple_01[-1])
# print(my_tuple_01[1:3])

nums_tuple1 = (1, 2, 3)
nums_tuple2 = (1, 2, 4)
print(nums_tuple1 < nums_tuple2)

nums_tuple1 = (1, 2, 3)
nums_tuple2 = (1, 2, 3, 0)
print(nums_tuple1 < nums_tuple2)

nums_tuple1 = (1, 2, 4)
nums_tuple2 = (1, 2, 3, 0)
print(nums_tuple1 > nums_tuple2)

animals_tuple1 = ('Cat', 'Dog')
animals_tuple2 = ('Cat', 'Parrot')
print(animals_tuple1 < animals_tuple2)

animals_tuple_1 = ('Cat', 'Turtle', 'Snake', 'Dog')
animals_tuple_2 = 'Cat', 'Turtle', 'Snake', 'Dog', 'Parrot'
print(animals_tuple_1 < animals_tuple_2)


