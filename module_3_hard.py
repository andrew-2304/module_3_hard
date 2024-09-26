# #Example
# a = [1,3,[2,[3,[4,[5,[6,[7,[8,[9,[[[55]]]]]],45]]]]]]
# print(type(str(a)))
# print(str(a).replace('[', '').replace(']', ''))
# list_string_numbers = str(a).replace('[', '').replace(']', '').split(', ')
# sum_number = 0
# i = 0
# # sum_number += float(list_string_numbers[i])
# # print(sum_number)
# # i += 1
# # sum_number += float(list_string_numbers[i])
# # print(sum_number)
# # i += 1
# while i < len(list_string_numbers):
#     sum_number += float(list_string_numbers[i])
#     print(sum_number)
#     i += 1

#Вариант без ф-ии
# data_structure = [
# [1, 2, 3],
# {'a': 4, 'b': 5},
# (6, {'cube': 7, 'drum': 8}),
# "Hello",
# ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
# list_values = str(data_structure).replace('[', '').replace(']', '')
# list_values = list_values.replace('(', '').replace(')', '')
# list_values = list_values.replace('{', '').replace('}', '')
# list_values = list_values.replace(':', ',').replace("'", '').split(', ')
# print(list_values)
#
# sum_value = 0
# i = 0
#
# while i < len(list_values):
#     value = list_values[i]
#     if value.isdigit():
#         sum_value += int(value)
#
#     else:
#         sum_value += len(value)
#     i += 1
#
# print(sum_value)


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    total_sum = 0

    for arg in args:
        if isinstance(arg, (list, tuple, set)):
            total_sum += calculate_structure_sum(*arg)
        elif isinstance(arg, dict):
            total_sum += calculate_structure_sum(*arg.items())
        elif isinstance(arg, str):
            total_sum += len(arg)
        elif isinstance(arg, (int, float)):
            total_sum += arg
        elif arg is None:
            pass
    return total_sum

result = calculate_structure_sum(data_structure)
print(result)

















