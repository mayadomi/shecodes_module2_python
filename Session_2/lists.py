# Lists - storage of multiple data points
list_name = [1, 2, 3, 4, 5] # str, int, float, list
# square brackets is syntax for list container
# group similar elements together with descriptive name
# position/indexing of elements starts at zero
print(list_name)
print(type(list_name))

# print(list_name[0]) # first element
# print(list_name[-1]) # very last element, regardless of number of elements

# Slicing a list
# print(list_name[0:4]) # start index : end index - start is inclusive, end is exclusive
# print(list_name[3:]) # empty end index goes to end of list
# print(list_name[-2:5])

# print(list_name[0:5:1]) # last argument - how many to skip - [1,2,3,4,5]
# print(list_name[0:5:2]) # [1,3,5]

# print(len(list_name))

# list_name.append(6)

# print(list_name)

# popped_element = list_name.pop(0)

# print(list_name)
# print(popped_element)

# list_name[1] = 90
# print(list_name)

# Nested lists

letters = ['a', 'b', 'c', 'd',['Emily', 'Julie']]
print(letters[4][0]) # drill down to inner list item: <listname>[outer list][iner list]

if 'a' in letters:
    print("It is in the list")

