from math import sqrt

class MyClass:
    def __init__(self):
        self.colors = ( (255, 255, 255),
            (255, 0, 0,),
            (128, 0, 0,),
            (0, 255, 0, ) )
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
