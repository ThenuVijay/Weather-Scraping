import requests 
file = requests.get("https://weather.com/en-IN/weather/today/l/bf01d09009561812f3f95abece23d16e123d8c08fd0b8ec7ffc9215c0154913c")
from bs4 import BeautifulSoup 
soup = BeautifulSoup(file.content, "html.parser") 
results = soup.find(id='todayDetails')
weather=results.find_all('section',class_="card Card--card--4VS_Q TodayDetailsCard--todaysDetailsCard--1VDig")
for i in weather:
    title=i.find('h2',class_="Card--cardHeading--3et4e")
    temp=i.find('div',class_="TodayDetailsCard--feelsLikeTemp--2GFqN")
    print(title.text)
    print(temp.text)
    tempdetails=i.find('div',class_="TodayDetailsCard--detailsContainer--1tqay")
    for j in tempdetails:
        print(j.text)
    print()
    
    
