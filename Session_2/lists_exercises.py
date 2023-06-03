# Q1
# Given the list of foods below, print:
# The first item in the list.
# The third item in the list.
# The last item in the list.
# The first three items in the list.
# The last three items in the list.
# The last item in the sublist

# foods = ["orange","apple","banana","strawberry","grape","blueberry",
#         ["carrot", "cauliflower", "pumpkin"],
#         "passionfruit","mango","kiwifruit"]

# print(foods[0])
# print(foods[2])
# print(foods[-1])
# print(foods[0:3])
# print(foods[-3:])
# print(foods[6][-1])

# Q4 ormat and print the contents of the following 
# list so that the output appears as depicted

# ppl_list = [
#             ["Monica", "in my life"],
#             ["Erica", "by my side"],
#             ["Rita's", "all I need"],
#             ["Tina's", "what I see"],
#             ["Sandra", "in the sun"],
#             ["Mary", "having fun"],
#             ["Jessica", "here I am"]
#             ]

# first_text = "A little bit of "
# print(first_text + ppl_list[0][0] + " " + ppl_list[0][1] + ";")
# print(first_text + ppl_list[1][0] + " " + ppl_list[1][1] + ";")
# print(first_text + ppl_list[2][0] + " " + ppl_list[2][1] + ";")
# print(first_text + ppl_list[3][0] + " " + ppl_list[3][1] + ";")
# print(first_text + ppl_list[4][0] + " " + ppl_list[4][1] + ";")
# print(first_text + ppl_list[5][0] + " " + ppl_list[5][1] + ";")
# print(first_text + ppl_list[6][0] + ", " + ppl_list[6][1] + ";")
# ppl_list.append(["you", "makes me your man (ah!)"])
# print(first_text + ppl_list[7][0] + " " + ppl_list[7][1])
# ppl_list.append("*trumpet solo*")
# print(ppl_list[8])

# Q3 
# Ask the user for three names. Add each name to a list, 
# and then print the list

# first_name = input("Please provide a name: ")
# second_name = input("Thanks, please provide another name: ")
# third_name = input("One last name offering: ")

# list_of_names = [first_name, second_name, third_name]

# print(list_of_names)

#Q4

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

# compiled_list_one = [a, b, c]
# print(compiled_list_one)

# compiled_list_two = [a[0], a[1], a[2], b[0], b[1], b[2], c[0], c[1], c[2]]
a.extend(b)
a.extend(c)
print(a)



