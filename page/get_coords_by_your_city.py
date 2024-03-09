from data.weather_data import Urls
from typing import Tuple
import requests
import allure


class GetCoords:
    @allure.step('Get latitude and longitude')
    def get_coords_by_your_city(self, your_city: str) -> Tuple[float, float]:
        """This function return coords by city.
        :param your_city: The name to use
        :return: coords lat and lon
        """
        params = {'name': your_city}
        geocoding = requests.get(Urls.URL_GEOCODING, params=params).json()

        lat = geocoding["results"][0]["latitude"]
        lon = geocoding["results"][0]["longitude"]
        return lat, lon
