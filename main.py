from typing import List

import requests
import pytest

test_data: list[str] = ["https://google.com.ua/", "https://aqa.science/", "https://poulpi.cours-pi.com/"]


@pytest.mark.parametrize("value", test_data)
def test_funct1_1(value):
    response = requests.get(value)
    assert response.status_code == 200, print(response.status_code)




