menu=[['egg','bagel','coffee'],
      ['blt','pbj','turkey'],
      ['soup','salad','spaghetti','taco']
      ]

print('breakfast menu: ',menu[0])

print('lunch menu: ',menu[1])

print('dinner menu: ',menu[2])

print(menu[0][1])


menus={'breakfast':['egg','bagel','coffee'],
      'lunch':['blt','pbj','turkey'],
      'dinner':['soup','salad','spaghetti','taco'] }

print('breakfast menu: ',menus['breakfast'])

print('lunch menu: ',menus['lunch'])

print('dinner menu: ',menus['dinner'])

#for loops in dictionary gives us the keys only
for result in menus:
    print(result)

#to get the key and value in the for loop

for name,menu in menus.items():
    print (name,menu)


    
#using dictionaries to represent objects
person={'name':'sarah',
        'city':'colombo',
        'age':'100'
    }

print(person.get('name'),'is',person.get('age'),'years old')










