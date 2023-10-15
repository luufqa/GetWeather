import requests
from typing import List, Tuple
import pytest

# url api с параметрами
URL_WEATHER = "https://api.open-meteo.com/v1/forecast"
URL_GEOCODING = "https://geocoding-api.open-meteo.com/v1/search"


def get_city_name(city: str) -> str:
    """This function return city name.
    :param city: The name to use
    :return: city name
    """
    return city


def get_sunset_sunrise(suns: str, sunr: str) -> Tuple[str, str]:
    """Function return date suns and sunr in city by coords. Put time in result.
    :param suns: First index, sunset date in list
    :param sunr: Second index, sunrise date in list
    :return: Put time in result
    """

    for a in suns:
        a = f"Sunset in you city in - {a[-5:]}"
        for b in sunr:
            b: str = f"Sunrise in you city in - {b[-5:]}"
            return a, b


def get_coords_by_your_city(youcity: str) -> Tuple[float, float]:
    """This function return coords by city.
    :param youcity: The name to use
    :return: coords lat and lon
    """
    params = {'name': youcity}

    Geocoding = requests.get(URL_GEOCODING, params=params).json()

    lat = Geocoding["results"][0]["latitude"]
    lon = Geocoding["results"][0]["longitude"]
    return lat, lon


def get_weather_by_coords(lat: float, lon: float, next_days=None, past_days=None) -> List[str]:
    """This function return weather by coords. Default weather for today (first day)
    :param lat: coords city - latitude
    :param lon: coords city - longitude
    :param next_days: you can get weather on the 1-7 next days, if add argument "next_days=2"
    :param past_days: you can get weather on the 1-2 past days, if add argument "past_days=1"
    :return: return weather by coords
    """

    if next_days is None:
        next_days = 1
    if None != past_days:
        next_days = 0
    paramsWea = {'latitude': lat,
                 'longitude': lon,
                 'hourly': 'temperature_2m',
                 'forecast_days': next_days,
                 'past_days': past_days}
    reqWeatherYourCity = requests.get(URL_WEATHER, params=paramsWea).json()

    dataTemp = reqWeatherYourCity["hourly"]["time"]
    tempCity = reqWeatherYourCity["hourly"]["temperature_2m"]

    compilationDataTemp = []
    for d, t in zip(dataTemp, tempCity):
        res = (str(d) + " - " + str(t) + " °C")
        compilationDataTemp.append(res)

    return compilationDataTemp


def sunset_sunrise_by_city(youcity: str, date: str, next_days=0) -> Tuple[str, str]:
    """This function return value sunset and sunrise. Default sunset/sunrise for today (first day)
    :param youcity: Start index, enter your city name in str "city"
    :param date: Second index, in format "YYYY-MM-DD"
    :param next_days: how many days
    :return: return weather by coords
    """
    paramsGeo = {'name': youcity}
    Geocoding = requests.get(URL_GEOCODING, params=paramsGeo).json()
    lat = Geocoding["results"][0]["latitude"]
    lon = Geocoding["results"][0]["longitude"]
    startDate = date
    endDate = startDate

    paramsWea = {'latitude': lat,
                 'longitude': lon,
                 'daily': 'sunset,sunrise',
                 'forecast_days': next_days,
                 'timezone': 'auto',
                 'start_date': startDate,
                 'end_date': endDate}
    reqWeatherYourCity = requests.get(URL_WEATHER, params=paramsWea).json()

    suns = reqWeatherYourCity["daily"]["sunset"]
    sunr = reqWeatherYourCity["daily"]["sunrise"]

    return get_sunset_sunrise(suns, sunr)


def get_weather_by_city_name(youcity: str, next_days=None):
    """Function return weather on the today. If you add "next_days=2" - can see more days
    :param youcity: Start index, give city name in str
    :param next_days: Second index, give number for next day
    :return: List with weather on the today or more days - if you add "next_days=2" or "next_days=3"
    """
    paramsGeo = {'name': youcity}
    Geocoding = requests.get(URL_GEOCODING, params=paramsGeo).json()

    lat = Geocoding["results"][0]["latitude"]
    lon = Geocoding["results"][0]["longitude"]
    return get_weather_by_coords(lat, lon, next_days)


def get_weather_past_days_by_city_name(youcity: str, past_days=None):
    """Function return weather on the today. If you add "past_days=1" - can see previous days
    :param youcity: Start index, give city name in str
    :param past_days: Second index, give number for next past day
    :return: List with weather on the today. You can see previous days - if you add "past_days=1" or "past_days=2"
    """
    next_days: None = None

    paramsGeo = {'name': youcity}
    Geocoding = requests.get(URL_GEOCODING, params=paramsGeo).json()

    lat = Geocoding["results"][0]["latitude"]
    lon = Geocoding["results"][0]["longitude"]

    return get_weather_by_coords(lat, lon, next_days, past_days)


#print(get_city_name("Moscow"))
#print(get_coords_by_your_city(get_city_name("Berlin")))
#print(get_weather_by_coords(55.75222, 37.61556))  # default "next_days=1", for one day. You can add
# argument "next_days=2" and you see two days
#print(get_weather_by_city_name("Berlin"))  # default "next_days=1", for one day.
# You can add argument "next_days=2"
print(get_weather_past_days_by_city_name("Moscow", past_days=2))  # default "past_days=0", for one past day. You can add
# argument "past_days=1"
print(sunset_sunrise_by_city("moscow", "2023-09-10"))
