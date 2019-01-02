import sys
from phue import Bridge

# user = 'nmartinruben'
# username = 'lkmHfRB0ScuElOrTXS2VUFMsyrEJ9KGINdyme5Y5'

BRIDGE_IP = '192.168.1.82'
ROOM_NAME = 'Noah Bedroom'

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class HueController(object, metaclass=Singleton):
    def __init__(self):
        self.bridge = Bridge(BRIDGE_IP)
    def connect(self):
        self.bridge.connect()
    def set_all_lights(self, mode):
        for light in self.bridge.lights:
            light.on = mode
    def get_scenes(self):
        return self.bridge.scenes
    def load_scene(self, scene_name):
        self.bridge.run_scene(ROOM_NAME, scene_name)
    def set_color_hue(self, hue):
        for light in self.bridge.lights:
            light.hue = hue
    def set_color_xy(self, x, y):
        for light in self.bridge.lights:
            light.xy = [x, y]

# if __name__ == '__main__':
#     h = HueController()
#     if sys.argv[1] == 'on':
#         h.set_all_lights(True)
#     elif sys.argv[1] == 'off':
#         h.set_all_lights(False)
#     elif sys.argv[1] == 'day':
#         h.load_scene('Read')
#     elif sys.argv[1] == 'night':
#         h.load_scene('Relax')
#     elif sys.argv[1] == 'red':
#         h.set_color_xy(0.7006, 0.2993)
#     elif sys.argv[1] == 'connect':
#         h.connect()
