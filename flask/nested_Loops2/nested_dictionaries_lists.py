x = [ [5,2,3], [10,8,9] ] 

x[1][0]=15
print(x)





students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}]


students[0]['last_name'] = 'Bryant'
print(students)


sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]

z[0]['y'] = 30
print(z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    list_num = 0
    for student in students:
        print(f"{list_num}) {student} ")
        list_num +=1


# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel

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