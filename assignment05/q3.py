my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 3}
result_dict = {}
for key, value in my_dict.items():
    if value not in result_dict.values():
        result_dict[key] = value

print("Original Dictionary:", my_dict)
print("Dictionary after removing duplicates:", result_dict)
