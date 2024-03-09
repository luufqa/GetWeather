from page.get_coords_by_your_city import GetCoords
from data.weather_data import Urls
from datetime import datetime
from typing import Tuple
import requests
import allure


class GetSunsetSunrise:
    @allure.step('Get sunset and sunrise')
    def get_sunset_sunrise_by_your_city(self, your_city: str, date=None, next_days=0) -> Tuple[str, str]:
        """This function return value sunset and sunrise. Default sunset/sunrise for today (first day)
        :param your_city: Start index, enter your city name in str "city"
        :param date: Second index, in format "YYYY-MM-DD"
        :param next_days: how many days
        :return: return weather by coords
        """
        get_coords = GetCoords()
        lat, lon = get_coords.get_coords_by_your_city(your_city)

        if date is not None:
            start_date = date
            end_date = start_date
        else:
            start_date = str(datetime.now())[0:10]
            end_date = start_date

        params = {'latitude': lat,
                  'longitude': lon,
                  'daily': 'sunset,sunrise',
                  'forecast_days': next_days,
                  'timezone': 'auto',
                  'start_date': start_date,
                  'end_date': end_date}

        req_weather_your_city = requests.get(Urls.URL_WEATHER, params=params).json()

        suns = req_weather_your_city["daily"]["sunset"]
        sunr = req_weather_your_city["daily"]["sunrise"]

        """
        suns: First index, sunset date in list
        sunr: Second index, sunrise date in list
        return: Put time in result
        """

        for a in suns:
            a = f"Sunset in your city in - {a[-5:]}"
            for b in sunr:
                b: str = f"Sunrise in your city in - {b[-5:]}"
                return a, b
