from page.get_sunset_sunrise_by_your_city import GetSunsetSunrise
import pytest
import allure


class TestGetSunsetSunrise:
    @allure.title('Positive test - check sunset and sunrise')
    @pytest.mark.parametrize("your_city, date", [
        ("Berlin", '2024-03-10'),
        ("Moscow", None),
        ("London", '2023-12-31')])
    def test_get_sunset_sunrise_by_your_city(self, your_city, date):
        get_sunset_sunrise = GetSunsetSunrise()
        result = get_sunset_sunrise.get_sunset_sunrise_by_your_city(your_city, date)
        assert 'Sunset in your city in -' in result[0]
        assert 'Sunrise in your city in -' in result[1]
