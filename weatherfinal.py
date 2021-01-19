import requests,json
city=input("Enter City : ")
url="https://api.openweathermap.org/data/2.5/weather?"+"q="+city+ "&appid=" + "daa0e2a80bcf6c23bc4f8debf113e38a"
response=requests.get(url)
if response.status_code==200:
    data=response.json()
    weather=data['main']
    temp=weather['temp']
    minimumtemp=weather['temp_min']
    maximumtemp=weather['temp_max']
    feels_like=weather['feels_like']
    pressure=weather['pressure']
    humidity=weather['humidity']
    report=data['weather']
    #rep=report['description']
    print("Location :",city)
    print("Temperature :",temp)
    print("Minimum Temperature :",minimumtemp)
    print("Maximum Temperature :",maximumtemp)
    print("Feels Like :",feels_like)
    print("Pressure :",pressure)
    print("Humidity :",humidity)
    print("Weather Report :",report[0]['description'])
else:
    print("URL not working,Please Check")
    
    
    
    
    
    