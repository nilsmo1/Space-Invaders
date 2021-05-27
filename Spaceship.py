# Spaceship

class Spaceship:
    def __init__(self):
        self.x      = None 
        self.y      = None
        self.width  = 200
        self.height = 50

    def get_pos(self):
        return (self.x, self.y)

    def get_size(self):
        return (self.width, self.height)

    def set_pos(self, x, y):
        self.x = x
        self.y = y
