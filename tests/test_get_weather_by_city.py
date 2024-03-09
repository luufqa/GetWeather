from page.get_weather_by_city import GetWeatherByCityName
import pytest
import allure


class TestGetWeatherByCity:
    @allure.title('Positive test - check weather by city')
    @pytest.mark.parametrize("your_city, expected_result", [
        ("Berlin", 168),
        ("Moscow", 168),
        ("London", 168)])
    def test_get_coords_by_your_city(self, your_city, expected_result):
        get_weather = GetWeatherByCityName()
        assert len(get_weather.get_weather_by_city_name(your_city)) == expected_result
