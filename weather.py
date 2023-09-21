from datetime import datetime as dt
import requests
from typing import List, Tuple

# url api с параметрами
urlWeather = "https://api.open-meteo.com/v1/forecast?"
urlGeocoding = "https://geocoding-api.open-meteo.com/v1/search?name="

yesSeriesDays = 0
startDate = ""         #dt.today()
endDate = startDate            #startDate
lat = 0
lon = 0
dataTemp = ""
tempCity = ""
pastDay = 0
suns = ""
sunr = ""

def stAndDat(dateR: str) -> Tuple[str, str]:
    """Function return default start-end date or user specified start-end date
    :param dateR: Start index, in format "YYYY-MM-DD"
    :type str: date, optional
    :return: response with diapason start-end date
    :rtype: str
    """
    s = dt.now().strftime("%Y-%M-%D")
    if dateR == s:
        pass
    else:
        global startDate, endDate
        startDate = dateR
        endDate = startDate
    return startDate, endDate

def sunsetSunrise(suns: str, sunr: str) -> Tuple[str, str]:
    """Function return date suns and sunr in city by coords. Put time in result.
    :param suns: First index, sunset date in list
    :type str:
    :param sunr: Second index, sunrise date in list
    :type str:
    :return: Put time in result
    :rtype: str
    """
    for a in suns:
        print(f"Sunset in you city in - {a[-5:]}")
    for b in sunr:
        print(f"Sunrise in you city in - {b[-5:]}")
    return a, b

def get_cityName(city: str) -> str:
    """This function return city name.
    :param city: The name to use
    :type str: str
    :return: city name
    :rtype: str
    """
    return city

def get_coords_by_yourCity(youCity: str) -> Tuple[float, float]:
    """This function return coords by city.
    :param youCity: The name to use
    :type str: str
    :return: coords lat and lon
    :rtype: str
    """
    Geocoding = requests.get(urlGeocoding + youCity).json()
    global lat, lon
    lat = Geocoding["results"][0]["latitude"]
    lon = Geocoding["results"][0]["longitude"]
    return lat, lon

def get_weather_by_coords(lat: float, lon: float, yesSeriesDays=1, pastDay=0) -> List[str]:
    """This function return weather by coords. Default weather for today (first day)
    :param lat: coords city - latitude
    :type float: float
    :param lon: coords city - longitude
    :type float: float
    :param yesSeriesDays: how many days
    :type int: int
    :param pastDay: previous days
    :type int: int
    :return: return weather by coords
    :rtype: str
    """
    weatherYourCity = urlWeather + f"latitude={lat}" + "&" + f"longitude={lon}" + "&hourly=temperature_2m" + f"&forecast_days={yesSeriesDays}" + f"&past_days={pastDay}"
    reqWeatherYourCity = requests.get(weatherYourCity).json()

    global dataTemp, tempCity
    dataTemp = reqWeatherYourCity["hourly"]["time"]
    tempCity = reqWeatherYourCity["hourly"]["temperature_2m"]
    # формируем красивый вывод погоды на сегодня
    compilationDataTemp = []
    # def build(dataTemp: str, tempCity: str) -> List[str]:
    for d, t in zip(dataTemp, tempCity):
        res = (str(d) + " - " + str(t) + " °C")
        compilationDataTemp.append(res)

    return compilationDataTemp

def last(date: str, lat: float, lon: float, yesSeriesDays=0) -> Tuple[str, str]:
    """This function return value sunset and sunrise. Default sunset/sunrise for today (first day)
    :param date: Start index, in format "YYYY-MM-DD"
    :type str: str
    :param lat: coords city - latitude
    :type float: float
    :param lon: coords city - longitude
    :type float: float
    :param yesSeriesDays: how many days
    :type int: int
    :return: return weather by coords
    :rtype: Tuple[str,str]
    """
    stAndDat(date)
    weatherYourCity = urlWeather + f"latitude={lat}" + "&" + f"longitude={lon}" + f"&forecast_days={yesSeriesDays}" + f"&daily=sunset,sunrise" + f"&timezone=auto" + f"&start_date={startDate}" + f"&end_date={endDate}"
    reqWeatherYourCity = requests.get(weatherYourCity).json()

    global suns, sunr
    suns = reqWeatherYourCity["daily"]["sunset"]
    sunr = reqWeatherYourCity["daily"]["sunrise"]
    return sunsetSunrise(suns, sunr)

def get_weather_by_cityName(weather, coords):
    """Function return weather on the next two days or another by your city name
    :param weather: Start index, give func "get_weather_by_coords" and func "get_coords_by_yourCity"
    :type funcs:
    :return: List with weather on the two days or another by your city name
    :rtype: Tuple[Any, Any]
    """
    return weather, coords

def get_weatherPastday_by_cityName(coords, weather):
    """Function return weather on the one pastday or another pastday, by your city name
    :param weather: Start index, give func "get_weather_by_coords" and func "get_coords_by_yourCity"
    :type funcs:
    :return: List with weather on the two days or another by your city name
    :rtype: Tuple[Any, Any]
    """
    return coords, weather

def get_sunsetSunrise_by_city(coords, sunsetAndSunrise):
    """Function return time when sunset and sunrise for the day, in the city that we specify
    :param weather: Start index, give func "get_weather_by_coords" and func "last"
    :type funcs:
    :return: List with weather on the two days or another by your city name
    :rtype: Tuple[Any, Any]
    """
    return coords, sunsetAndSunrise


#print(get_cityName("Moscow"))
#print(get_coords_by_yourCity(get_cityName("Moscow")))
#print(get_weather_by_coords(55.75222, 37.61556, yesSeriesDays=2))
#print(get_weather_by_cityName(get_weather_by_coords(lat, lon, yesSeriesDays=2), get_coords_by_yourCity(get_cityName("Moscow"))))
#print(get_weatherPastday_by_cityName(get_weather_by_coords(lat, lon, yesSeriesDays, pastDay=1), get_coords_by_yourCity(get_cityName("Moscow"))))
#get_sunsetSunrise_by_city(get_coords_by_yourCity(get_cityName("Berlin")), last("2023-09-30", lat, lon))
