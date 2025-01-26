import requests

def test_sumtwo_1():
    resp = requests.get("http://localhost:8000/sumtwo", params={"a":1, "b":4})
    text = resp.text
    print(text)
    assert "5" in text