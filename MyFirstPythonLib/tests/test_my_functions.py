from lib import my_functions


def test_haversine():
    assert my_functions.haversine(52.370216, 4.895168, 52.520008,
    13.404954) == 945793.4375088713
