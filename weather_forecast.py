import requests
import json
while True:
    city = input("Enter the city: ")
    print("Please wait...Loading!!")
    try:
        url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"
        r = requests.get(url)
        weatherdic = json.loads(r.text)
        x = weatherdic["current"]["temp_c"]
        print(f"temperature: {x}")
        print("region: ",weatherdic["location"]["region"],"\n")
        print("latitude : ",weatherdic["location"]["lat"],"\n")
        print("longitude: ",weatherdic["location"]["lon"],"\n")
        print("cloud: ",weatherdic["current"]["cloud"],"\n")
        print("wind(kph): ",weatherdic["current"]["wind_kph"],"\n")
        print("wind(mph): ",weatherdic["current"]["wind_mph"],"\n")
        print("wind degree: ",weatherdic["current"]["wind_degree"],"\n")
        print("wind direction: ",weatherdic["current"]["wind_dir"],"\n")
        print("humidity: ",weatherdic["current"]["humidity"],"\n")
        print("last updated: ",weatherdic["current"]["last_updated"],"\n")
    except:
        print("you are entered wrong location name")
        print("enter 0 to exit...")
    z = int(input("Enter 0 to continue or 1 to exit "))
    match z:
        case 0:continue
        case 1:break