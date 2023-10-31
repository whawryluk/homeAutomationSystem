def test_temperature_reading(client):
    response = client.get("/temperature")
    temp_value = response.data[-5]
    assert b"current temperature:" in response.data
    assert -20 <= temp_value <= 50


def test_humidity_reading(client):
    response = client.get("/humidity")
    humidity_value = response.data[-5]
    assert b"current humidity:" in response.data
    assert 0 <= humidity_value <= 100
