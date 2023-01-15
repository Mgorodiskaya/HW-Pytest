import requests

cred = ("admin", "admin123")

session = requests.Session()
session.auth = cred

auth_resp = session.get("https://www.aqa.science/users/3032/")
data = eval(auth_resp.text)


def test_name():
    assert data["username"] == "Serhii_334", print("Yes! You are this man, Serhiiy")
