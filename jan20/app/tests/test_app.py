import requests
def test_app_sumtwo():
    resp = requests.get(
        "http://localhost:8000/sumtwo",
        params={"a": 44, "b": 55})
    assert "Summen av 44 og 55 er 99" in resp.text
