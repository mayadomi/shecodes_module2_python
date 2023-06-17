# Lists
# number = [1,2,3]
# number[0]

# Dictionary
# key, value pairs
# keys immutable & unique - string, float, integer, boolean

student_phonebook = {
    "Cindy" : 111,
    "Tracey" : 123,
    "Pauline" : 444
}

# print(student_phonebook)
# #print(type(student_phonebook))

# # add key value
# student_phonebook["Yara"] = 555

# # change key value
# student_phonebook["Cindy"] = 445

# # delete key value
# del student_phonebook["Cindy"]

# # key error (no key)
# student_phonebook['Asli']

# # iterate through values
# for value in student_phonebook.values():
#     print(value)

# # iterate through key/value pairs
# for key in student_phonebook:
#     print(key, student_phonebook[key])

# tuple of key, value pair - 'unpacking'
for key, value in student_phonebook.items():
    print (key, value)
