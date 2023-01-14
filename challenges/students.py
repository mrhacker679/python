import json
data_list = []
with open('short.txt') as file:
    for row in file:
        lst = row.split()
        data_list.append(lst)


def to_nested_dict(data_list):
    nested_dict = {}
    for subject, student, marks in data_list:
        if student not in nested_dict:
            nested_dict[student] = {}
        nested_dict[student][subject] = marks
    return nested_dict


# print(to_nested_dict(data_list))

students = to_nested_dict(data_list)


students_json = json.dumps(students, indent=4)

print(students_json)


'''
To dynamically create a variable

for key, value in my_dict.items():
    globals()[key] = value
    
'''
