#print("Hello World")

import requests
from bs4 import BeautifulSoup

instring = input("Enter City Name\nFor example :Indore\nHere :").strip()
name = instring.upper()
url = ('https://www.weather-forecast.com/locations/' + name + '/forecasts/latest')
page = requests.get(url)
status = page.status_code

if (status==200):
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    info = soup.find_all('span', class_="phrase")
    #print(info)
    desc = str(info[0].text)
    #print(desc)
    result = desc.split(",")[0]
    print("Today's weather forecast for ",name, " is: ", result)

else:
    print("There's may be a connection issue or incorrect city name.")