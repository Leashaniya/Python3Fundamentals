import requests

response=requests.get("http://api.open-notify.org/astros.json")
result=response.json()
print(result) 

#printing each person (name and craft name )
for i in result['people']:
    print(i)

#just only printing the name part 
for j in result['people']:                  #name and people are key
    print(j['name'])  


#format of the dictonary and the list was
'''
{'message':'success',
 'people': 
        [{
            'name':'jasmin', 'craf' : 'iss'
            .....
            ....

        }]   
        }
''' 