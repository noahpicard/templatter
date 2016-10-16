import random


class Color:
    """
    Represents a color in the hsl color space
    """
    def __init__(self, h, s, l):

        # keep values in bounds
        h %= 360
        if s < 0 or s > 100:
            raise ValueError("Saturation out of range [0, 100]: %d." % s)
        if l < 0 or l > 100:
            raise ValueError("Lightness out of range [0, 100]: %d." % l)

        self.hue = h
        self.saturation = s
        self.lightness = l

    def __str_(self):
        return make_color_hsl(self.hue, self.saturation, self.lightness)


def get_random_color():
    hue_max = 360

    sat_max = 100
    light_max = 100

    sat_base = 0
    light_base = 0

    sat = (random.random() * (sat_max - sat_base*2)) + sat_base
    light = (random.random() * (light_max - light_base*2)) + light_base
    hue = (random.random() * hue_max)

    return Color(h=hue, s=sat, l=light)


def make_color_hsl(h, s, l):
    return "hsl(" + str(h) + "," + str(s) + "%," + str(l) + "%)"
