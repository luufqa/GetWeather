from page.get_coords_by_your_city import GetCoords
import pytest
import allure


class TestGetCoords:
    @allure.title('Positive test - check latitude and longitude')
    @pytest.mark.parametrize("your_city, expected_result", [
        ("Berlin", (52.52437, 13.41053)),
        ("Moscow", (55.75222, 37.61556)),
        ("London", (51.50853, -0.12574))])
    def test_get_coords_by_your_city(self, your_city, expected_result):
        coords = GetCoords()
        assert coords.get_coords_by_your_city(your_city) == expected_result
