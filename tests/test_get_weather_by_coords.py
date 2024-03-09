from page.get_weather_by_coords import GetWeatherByCoords
import pytest
import allure


class TestGetWeatherByCoords:
    @allure.title('Positive test - check weather by coords')
    @pytest.mark.parametrize("lat, lon, next_days, past_days, expected_result", [
        (52.52437, 13.41053, 16, 0, 384),
        (52.52437, 13.41053, 1, 0, 24),
        (55.75222, 37.61556, 0, 1, 24),
        (55.75222, 37.61556, 0, 92, 2208)])
    def test_get_weather_by_coords(self, lat, lon, next_days, past_days, expected_result):
        weather = GetWeatherByCoords()
        assert len(weather.get_weather_by_coords(lat, lon, next_days, past_days)) == expected_result
