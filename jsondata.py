import requests

response=requests.get("http://api.open-notify.org/astros.json")
result=response.json()
print(result) 

#printing each person (name and craft name )
for i in result['people']:
    print(i)

#just only printing the name part 
for j in result['people']:
    print(j['name'])  