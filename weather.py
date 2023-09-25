from datetime import datetime as dt
import requests
from typing import List, Tuple

# url api с параметрами
URL_WEATHER = "https://api.open-meteo.com/v1/forecast?"
URL_GEOCODING = "https://geocoding-api.open-meteo.com/v1/search?name="


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

    Geocoding = requests.get(URL_GEOCODING + youcity).json()

    lat = Geocoding["results"][0]["latitude"]
    lon = Geocoding["results"][0]["longitude"]
    return lat, lon


def get_weather_by_coords(lat: float, lon: float, next_days=1, past_days=0) -> List[str]:
    """This function return weather by coords. Default weather for today (first day)
    :param lat: coords city - latitude
    :param lon: coords city - longitude
    :param next_days: how many days
    :param past_days: previous days
    :return: return weather by coords
    """
    weatherYourCity = URL_WEATHER + f"latitude={lat}" + "&" + f"longitude={lon}" + "&hourly=temperature_2m" \
                      + f"&forecast_days={next_days}" + f"&past_days={past_days}"
    reqWeatherYourCity = requests.get(weatherYourCity).json()

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
    Geocoding = requests.get(URL_GEOCODING + youcity).json()
    lat = Geocoding["results"][0]["latitude"]
    lon = Geocoding["results"][0]["longitude"]
    startDate = dt.now().strftime("%Y-%M-%D")
    endDate = startDate
    if date == startDate:
        pass
    else:
        startDate = date
        endDate = startDate

    weatherYourCity = URL_WEATHER + f"latitude={lat}" + "&" + f"longitude={lon}" + f"&forecast_days={next_days}" \
                      + f"&daily=sunset,sunrise" + f"&timezone=auto" + f"&start_date={startDate}" \
                      + f"&end_date={endDate}"
    reqWeatherYourCity = requests.get(weatherYourCity).json()

    suns = reqWeatherYourCity["daily"]["sunset"]
    sunr = reqWeatherYourCity["daily"]["sunrise"]
    return get_sunset_sunrise(suns, sunr)


def get_weather_by_city_name(youcity: str, next_days=0):
    """Function return weather on the next two days or another by your city name
    :param youcity: Start index, give city name in str
    :param next_days: Second index, give number for next day
    :return: List with weather on the two days or another by your city name
    """
    Geocoding = requests.get(URL_GEOCODING + youcity).json()
    lat = Geocoding["results"][0]["latitude"]
    lon = Geocoding["results"][0]["longitude"]
    return get_weather_by_coords(lat, lon, next_days)


def get_weather_past_days_by_city_name(youcity: str, past_days=0):
    """Function return weather on the one past_days or another past_days, by your city name
    :param youcity: Start index, give city name in str
    :param past_days: Second index, give number for next past day
    :return: List with weather on the two days or another by your city name
    """

    Geocoding = requests.get(URL_GEOCODING + youcity).json()
    lat = Geocoding["results"][0]["latitude"]
    lon = Geocoding["results"][0]["longitude"]
    return get_weather_by_coords(lat, lon, past_days)

# print(get_city_name("Moscow"))
# print(get_coords_by_your_city(get_city_name("Berlin")))
# print(get_weather_by_coords(55.75222, 37.61556, next_days=2))
# print(get_weather_by_city_name("Berlin", next_days=2))
# print(get_weather_past_days_by_city_name("Moscow", past_days=5))
# print(sunset_sunrise_by_city("moscow", "2023-09-10"))
