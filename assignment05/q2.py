my_dict = {"key1": [1, 2, 3], "key2": [4, 5, 6, 7], "key3": [7, 8], "key4": [9, 9]}
max_unique_values = 0
max_unique_key = None
for key, value in my_dict.items():
    unique_values = len(set(value))
    if unique_values > max_unique_values:
        max_unique_values = unique_values
        max_unique_key = key
print(max_unique_key)