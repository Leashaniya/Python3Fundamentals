dictionaries={'lol':'laugh out loud',
              'tbh':'to be honest',
              'idk':"i don't know"}

print (dictionaries['lol'])


acronyms={}

acronyms["lol"]="laugh out loud"
acronyms["idk"]="i don't know"

print(acronyms)

#updating values
acronyms["idk"] ="know"
print(acronyms)
print(acronyms['idk'])


#to delete
del acronyms['lol']
print(acronyms)


#none type
acronym={'lol':'laugh out loud',
              'tbh':'to be honest',
              'idk':"i don't know"}
definition=acronym.get('btw')

if definition: #if true
    print(definition)
else:
    print("key doesn't exist")

sentence= 'idk'+' what happened '+'tbh'
translation=acronym.get('idk')+' what happened '+acronym.get('tbh')
print('sentence:',sentence)
print('translation:',translation)
