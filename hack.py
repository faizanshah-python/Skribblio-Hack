import PIL.Image
import colors
import drawing
import matplotlib.pyplot as plt

class Image:
    def __init__(self, image):
        self.image = PIL.Image.open(image)
        self.image = self.image.resize((800, 600))
        self.image_rgb = self.image.convert('RGB')

    def get_size(self):
        return self.image.size

    def generate_grid(self):
        self.width, self.height = self.get_size()
        for row in range(1, self.height):
            for column in range(1, self.width):
                self.simplified = C.check_color(self.image_rgb.getpixel((column, row)))
                D.draw_pixel(column, row, self.simplified)




if __name__ == '__main__':
    IMAGE = 'test-image.jpg'
    GAME_CODE = '8w7uC49AuzIv'
    RGB = Image(IMAGE)
    D = drawing.Drawing(GAME_CODE)
    C = colors.Colours()
    RGB.generate_grid()
