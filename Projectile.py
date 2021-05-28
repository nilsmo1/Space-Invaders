# Projectile

class Projectile:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = 1

    def move(self):
        self.y += self.direction*self.speed

    def get_pos(self):
        return (self.x, self.y)
