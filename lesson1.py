import datetime
import requests

# url api с параметрами
urlWeather = "https://api.open-meteo.com/v1/forecast?"
urlGeocoding = "https://geocoding-api.open-meteo.com/v1/search?name="

yesSeriesDays = 0
startDate = datetime.date.today()
endDate = startDate
lat = 0
lon = 0
dataTemp = 0
tempCity = 0
pastDay = 0

def stAndDat():
    chooseDay = input("Today or Other?")
    if chooseDay == "Today":
        pass
    else:
        global startDate, endDate
        startDate = input("Enter date: YYYY-MM-DD")
        endDate = startDate
    return startDate, endDate
def sunsetSunrise(suns, sunr):
    for a in suns:
        print(f"Sunset in you city in - {a[-5:]}")
    for b in sunr:
        print(f"Sunrise in you city in - {b[-5:]}")
    return a, b
def get_cityName():
    city = input("city?")
    return city
def get_coords_by_yourCity(youCity):
    Geocoding = requests.get(urlGeocoding+youCity).json()
    global lat, lon
    lat = Geocoding["results"][0]["latitude"]
    lon = Geocoding["results"][0]["longitude"]
    return lat, lon
def get_weather_by_coords(lat, lon, yesSeriesDays=0, pastDay=0):

    weatherYourCity = urlWeather + f"latitude={lat}" + "&" + f"longitude={lon}" + "&hourly=temperature_2m" + f"&forecast_days={yesSeriesDays}" + f"&past_days={pastDay}"
    reqWeatherYourCity = requests.get(weatherYourCity).json()
    # из JSON получаем Дату и Температуру
    global dataTemp, tempCity
    dataTemp = reqWeatherYourCity["hourly"]["time"]
    tempCity = reqWeatherYourCity["hourly"]["temperature_2m"]



    # формируем красивый вывод погоды на сегодня
    compilationDataTemp = []
    for d, t in zip(dataTemp, tempCity):
        res = (str(d) + " - " + str(t) + " °C")
        compilationDataTemp.append(res)
    return compilationDataTemp

def last(lat, lon, yesSeriesDays=0):
    stAndDat()
    weatherYourCity = urlWeather + f"latitude={lat}" + "&" + f"longitude={lon}" + f"&forecast_days={yesSeriesDays}" + f"&daily=sunset,sunrise" + f"&timezone=auto" + f"&start_date={startDate}" + f"&end_date={endDate}"
    reqWeatherYourCity = requests.get(weatherYourCity).json()

    # из JSON получаем Дату и Температуру
    global suns, sunr
    suns = reqWeatherYourCity["daily"]["sunset"]
    sunr = reqWeatherYourCity["daily"]["sunrise"]
    sunsetSunrise(suns, sunr)

def get_weather_by_cityName(coords, weather):
    return coords, weather
def get_weatherPastday_by_cityName(coords, weather):
    return coords, weather
def get_sunsetSunrise_by_city(coords, sunsetAndSunrise):
    return coords, sunsetAndSunrise





#print(get_cityName())
#print(get_coords_by_yourCity(get_cityName()))
#print(get_weather_by_coords(lat, lon, yesSeriesDays=input("how much days? since 1 for 16")))
#print(get_weather_by_cityName(get_coords_by_yourCity(get_cityName()),get_weather_by_coords(lat, lon, yesSeriesDays=input('how much days? since 1 for 16'))))
#print(get_weather_by_cityName(get_coords_by_yourCity(get_cityName()),get_weather_by_coords(lat, lon, yesSeriesDays, pastDay=input("how past day? 1 2"))))
#print(get_sunsetSunrise_by_city(get_coords_by_yourCity(get_cityName()), last(lat, lon)))


