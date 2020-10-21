from selenium import webdriver

class Drawing:
    def __init__(self, game_code):
        self.game_code = game_code
        self.path = 'D:\coding\chromedriver.exe'
        self.driver = webdriver.chrome(self.path)
        self.driver.get('https://skribbl.io/?' + self.game_code)

    def draw_pixel(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.color_element = self.find_color_element()

    def find_color_element(self):
        if self.color == (255, 0, 0,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[3]' #RED
        if self.color == (0, 0, 255,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[8]' #DARK BLUE
        if self.color == (255, 255, 255,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[1]' #WHITE
        if self.color == (0, 0, 0,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[1]' #BLACK
        if self.color == (211, 211, 211,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[2]' #GREY
        if self.color == (128, 0, 0,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[3]' #DARK RED
        if self.color == (255, 165, 0,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[4]' #ORANGE
        if self.color == (255, 140, 0,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[4]' #DARK ORANGE
        if self.color == (255, 255, 0,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[5]' #YELLOW
        if self.color == (255, 215, 0,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[5]' #DARK YELLOW
        if self.color == (124, 252, 0,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[6]' #GREEN
        if self.color == (0, 100, 0,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[6]' #DARK GREEN
        if self.color == (0, 191, 255,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[7]' #BLUE
        if self.color == (70, 130, 180,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[7]' #BLUE BOTTOM row
        if self.color == (0, 0, 128,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[8]' #DARK BLUE BOTTOM ROW
        if self.color == (128, 0, 128,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[10]' #PURPLE BOTTOM row
        if self.color == (255, 192, 203,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[9]' #PINK
        if self.color == (160, 82, 45,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[11]' #BROWN
        if self.color == (139, 69, 19,):
            return '//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[11]' #BROWN BOTTOM ROW


if __name__ == '__main__':
    print('This is meant to be a module. Please run hack.py instead.')
