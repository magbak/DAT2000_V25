import requests

def test_sumtwo_5():
    resp = requests.get("http://localhost:8000/sumtwo/", params={"a":1, "b":4})
    text = resp.text
    print("\n", text)
    assert "5" in text

def test_sumtwo_99():
    resp = requests.get("http://localhost:8000/sumtwo/", params={"a":55, "b":44})
    text = resp.text
    print("\n", text)
    assert "99" in text