import PIL.Image
import colors

class Image:
    def __init__(self, image):
        self.image = PIL.Image.open(image)
        self.image = self.image.resize((800, 600))
        self.image_rgb = self.image.convert('RGB')

    def get_size(self):
        return self.image.size

    def generate_grid(self):
        self.grid = []
        self.width, self.height = self.get_size()
        for row in range(1, self.height):
            current_row = self.grid.append([])
            for column in range(1, self.width):
                self.grid[row-1].append(self.image_rgb.getpixel((column, row)))
                self.rgb_value = self.image_rgb.getpixel((column, row))
                self.color = c.check_color(self.rgb_value)
                print(self.color)




if __name__ == '__main__':
    IMAGE = 'test-image.jpg'
    RGB = Image(IMAGE)
    c = colors.MyClass()
    RGB.generate_grid()
