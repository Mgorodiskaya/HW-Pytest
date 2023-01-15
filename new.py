import requests
import pytest

from main import test_data


@pytest.mark.parametrize("value", test_data)
def test_funct2_1(value):
    value += "login/"
    response = requests.get(value)
    assert response.status_code == 200, print(response.status_code)


