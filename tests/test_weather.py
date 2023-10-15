from weather import get_city_name
from weather import get_coords_by_your_city
from weather import get_weather_by_coords
from weather import get_weather_by_city_name
from weather import get_weather_past_days_by_city_name
from weather import sunset_sunrise_by_city
import pytest


@pytest.mark.parametrize("a, expected_result", [("Moscow", "Moscow"), ("Berlin", "Berlin")])
def test_get_city_name(a, expected_result):
    assert get_city_name(a) == expected_result


@pytest.mark.parametrize("a, b, expected_result", [(55.75222, 37.61556, get_weather_by_coords(55.75222, 37.61556))])
def test_get_weather_by_coords(a, b, expected_result):
    assert get_weather_by_coords(a, b) == expected_result


@pytest.mark.parametrize("a, expected_result", [(get_city_name("Berlin"), (52.52437, 13.41053))])
def test_get_coords_by_your_city(a, expected_result):
    assert get_coords_by_your_city(a) == expected_result


@pytest.mark.parametrize("a, expected_result",
                         [(get_city_name("Berlin"), get_weather_by_city_name(get_city_name("Berlin")))])
def test_get_weather_by_city_name(a, expected_result):
    assert get_weather_by_city_name(a) == expected_result


@pytest.mark.parametrize("a, expected_result", [("Moscow", get_weather_past_days_by_city_name("Moscow"))])
def test_get_weather_past_days_by_city_name(a, expected_result):
    assert get_weather_past_days_by_city_name(a) == expected_result


@pytest.mark.parametrize("a, b, expected_result",
                         [("moscow", "2023-09-10", sunset_sunrise_by_city("moscow", "2023-09-10"))])
def test_sunset_sunrise_by_city(a, b, expected_result):
    assert sunset_sunrise_by_city(a, b) == expected_result
