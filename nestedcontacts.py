contacts={
        'number':3,
        'students':[
                   { 'name':'sarah','email':'sarah@gmail.com'},
                   {'name':'leasha','email':'leasha@gmail.com'},
                   {'name':'meena','email':'meena@gmail.com'}
        ]
}

print("student emails: ")
for student in contacts['students']:
    print(student['email'])

