## for and while loops ##

shopping_list = ["eggs", "milk", "supermalt"]
print(shopping_list)

for items in shopping_list:
    print(items)

## minitask

devops_students = {
     "name": "Jared",
     "stream": "tech",
     "completed_lessons": 4,
     "completed_lesson_names": ["operators", "data types", "variables"]
}

for keys in devops_students.keys():
    print(keys)
    print(devops_students[keys])