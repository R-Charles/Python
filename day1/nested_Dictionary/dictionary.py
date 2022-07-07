x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

x[1][0] = 15
print(x)

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
z[0]['y'] = 30
print(z)

students

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(students):
    list_num = 0
    for student in students:
        print(f"{list_num}) {student}")
        list_num += 1


iterateDictionary(students)


def iterateDictionary2(first_name, students):
    list_num = 0
    # for student in students:
    for first_name in students:
        print(f"{list_num}) {first_name}")
        list_num += 1


# def iterateDictionary2('first_name', students):
# for student in students:
#     print(f"{list_num}) {students[student]}")
#     list_num += 1

# for student in students.student():
#     print(student)

def iterateDictionary2(key_name, some_list):
    for list in range(len(some_list)):
        for x, y in some_list[list].items():
            if key_name == x:
                print(y)


iterateDictionary2('last', students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


def printInfo(some_dict):
    for key, value in some_dict.items():
        # print(f"{key}) {student['value']}")
        print(len(value), key.upper())
        for i in range(len(value)):
            print(value[i])


printInfo(dojo)
