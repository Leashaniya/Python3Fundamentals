import requests

url='http://api.weatherapi.com/v1/current.json?key=819d6590293d4b639ba125132231512&q=London&aqi=no'

response=requests.get(url)
weather=response.json()

print(weather)

#to find the current temp in farenheit
temp=weather.get('current').get('temp_f')
print(temp)

#to find the current condition in text
text=weather.get('current').get('condition').get('text')
print(text)



'''

{
    'location ' :{
                    'name':'london',
                    'region': 'greater london',
                    ....

    },
    'current' :{
                'last updated': '2023-2-15',
                'temp_f': 8.0,
                'condition':{
                        'text':'partly cloud',
                        'code': 1003
                }
    },
'wind_mph':2.2,
'pressure': 30.62
'uv':3.0
........

}


'''