from math import sqrt

class MyClass:
    def __init__(self):
        self.colors = ( (255, 0, 0), #RED
            (0, 255, 0,), #GREEN
            (0, 0, 255,), #BLUE 2
            (0, 0, 0,), #BLACK
            (255, 255, 255,), #WHITE
            (211, 211, 211,), #GREY
            (128, 128, 128,), #DARK GREY
            (128, 0, 0,), #DARK RED
            (255, 165, 0,), #ORANGE
            (255, 140, 0,), #DARK ORANGE
            (255, 255, 0,), #YELLOW
            (255, 215, 0,), #DARK YELLOW
            (124, 252, 0,), #GREEN
            (0, 100, 0,), #DARK GREEN
            (0, 191, 255,), #BLUE 1
            (70, 130, 180,), #DARK BLUE 1
            (0, 0, 128,), #DARK BLUE 2
            ) 



    def check_color(self, rgb_value):
        self.r, self.g, self.b = rgb_value
        self.color_diffs = []
        for color in self.colors:
            self.cr, self.cg, self.cb = color
            self.color_diff = sqrt(abs(self.r - self.cr)**2 + abs(self.g - self.cg)**2 + abs(self.b - self.cb)**2)
            self.color_diffs.append((self.color_diff, color))
        return min(self.color_diffs)[1]







if __name__ == '__main__':
    print('This is meant to be a module. Please run hack.py instead.')
