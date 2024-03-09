from page.get_weather_by_coords import GetWeatherByCoords
from page.get_coords_by_your_city import GetCoords
import allure


class GetWeatherByCityName:
    @allure.step('Get weather by city')
    def get_weather_by_city_name(self, your_city: str):
        """Function return weather on the today. If you add "next_days=2" - can see more days
        :param your_city: Start index, give city name in str
        :return: List with weather on the today or more days - if you add "next_days=2" or "next_days=3"
        """
        get_coords = GetCoords()
        get_weather = GetWeatherByCoords()
        lat, lon = get_coords.get_coords_by_your_city(your_city)
        get_weather = get_weather.get_weather_by_coords(lat, lon)
        return get_weather
