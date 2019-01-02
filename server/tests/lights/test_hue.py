from app.lights.hue import HueController

def test_HueController_Singleton():
    a = HueController()
    b = HueController()
    assert id(a) == id(b)
    assert a == b