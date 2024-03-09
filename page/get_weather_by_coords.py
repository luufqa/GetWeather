from data.weather_data import Urls
from typing import Union
import requests
import allure


class GetWeatherByCoords:
    @allure.step('Get weather by coords')
    def get_weather_by_coords(self, lat: float, lon: float, next_days=None, past_days=None) -> Union[str, list[str]]:
        """This function return weather by coords. Default weather for today (first day)
        :param lat: coords city - latitude
        :param lon: coords city - longitude
        :param next_days: you can get weather on the 1-16 next days, if add argument "next_days=2"
        or
        :param past_days: you can get weather on the 1-92 past days, if add argument "past_days=1"
        :return: return weather by coords
        """
        params = {'latitude': lat,
                  'longitude': lon,
                  'hourly': 'temperature_2m'}

        if next_days is None and past_days is None:
            pass
        elif next_days is not None and (0 <= next_days <= 16) and past_days is None:
            params['forecast_days'] = next_days
        elif past_days is not None and (0 <= past_days <= 92) and (0 <= next_days <= 16):
            params['past_days'] = past_days
            params['forecast_days'] = next_days
        else:
            return 'Bad request, uncorrect values'

        req_weather_your_city = requests.get(Urls.URL_WEATHER, params=params).json()

        data_temp = req_weather_your_city["hourly"]["time"]
        temp_city = req_weather_your_city["hourly"]["temperature_2m"]

        compilation_data_temp = []
        for d, t in zip(data_temp, temp_city):
            res = (str(d) + " = " + str(t) + " °C")
            compilation_data_temp.append(res)

        return compilation_data_temp
