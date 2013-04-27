__author__ = 'lennart'
class SpriteSheet(object):
    def __init__(self, sprites, spritesize, width, heigth):
        self.sprites = sprites
        self.spritesize = spritesize
        self.width = width
        self.heigth = heigth

    def get_sprite_at(self, location):
        (x,y) = location
        if (x >= 0) and (x < self.width) and (y >= 0) and (y < self.heigth):
            return self.sprites[x][y]
        return None

