def sort_tuples_by_length(strings):
    tuple_list = [(s, len(s)) for s in strings]
    sorted_list = sorted(tuple_list, key=lambda x: x[1])
    return sorted_list

strings = ["apple", "banana", "cherry", "date"]
sorted_tuples = sort_tuples_by_length(strings)
print(sorted_tuples)
