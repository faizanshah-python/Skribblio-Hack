import PIL.Image

class Image:
    def __init__(self, image):
        self.image = PIL.Image.open(image)
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
            print(self.grid[row-1])



if __name__ == '__main__':
    IMAGE = 'test-image.jpg'
    RGB = Image(IMAGE)
    RGB.generate_grid()
    image = PIL.Image.open(IMAGE)
    new_image = image.resize((500, 500))
    new_image.show()
