acronyms =['lol','idk','smh','tbh']
word='bfn'

if word in acronyms:
    print(word+ " is in the list")
    print(acronyms)
else:
    print(word+ " is not in the list")
    acronyms.append(word)
    print(acronyms)


#looping over each item in the list
for result in acronyms:
    print(result)
