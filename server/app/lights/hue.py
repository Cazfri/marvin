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

# rgb <-> xy conversions shamelessly copied from
# https://github.com/sqmk/Phue/blob/master/library/Phue/Helper/ColorConversion.php
def rgb_to_xy(red, green, blue):
    def vividize_colors(color):
        if color > 0.04045:
            return pow((color + 0.055) / (1.055), 2.4)
        else:
            return color / 12.92

    rgb = [vividize_colors(color / 255.0) for color in (red, green, blue)]

    x = rgb[0] * 0.664511 + rgb[1] * 0.154324 + rgb[2] * 0.162028
    y = rgb[0] * 0.283881 + rgb[1] * 0.668433 + rgb[2] * 0.047685
    z = rgb[0] * 0.000000 + rgb[1] * 0.072310 + rgb[2] * 0.986039

    xyz_sum = x + y + z

    if xyz_sum == 0:
        x = 0
        y = 0
    else:
        x = x / xyz_sum
        y = y / xyz_sum

    return x, y, round(y * 255)

def xy_to_rgb(in_x, in_y, bri = 255):
    in_z = 1.0 - in_x - in_y

    y = bri / 255
    x = (y / in_y) * in_x
    z = (y / in_y) * in_z

    red = x * 1.656492 - y * 0.354851 - z * 0.255038
    green = -x * 0.707196 + y * 1.655397 + z * 0.036152
    blue = x * 0.051713 - y * 0.121364 + z * 1.011530

    def reverse_gamma_scale(color):
        new_color = 0.0
        if color <= 0.0031308:
            new_color = 12.92 * color
        else:
            new_color = 1.055 * pow(color, 1.0 / 2.4) - 0.055
        return round(new_color * 255)

    return [reverse_gamma_scale(color) for color in (red, green, blue)]

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
    def set_color_rgb(self, red, green, blue):
        x, y, _ = rgb_to_xy(red, green, blue)
        self.set_color_xy(x, y)
