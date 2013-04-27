import os
import math
import pygame

from spritesheet import SpriteSheet

__author__ = 'lennart'
class SpriteSheetLoader(object):
    def __init__(self, datapath):
        self.datapath = datapath

    def load_sprite_sheet(self, filename, spritesize):
        surf = pygame.image.load(os.path.join(self.datapath, filename))
        (width, height) = surf.get_size()
        spritelist = []
        if width % spritesize == 0 and height % spritesize == 0:
            for i in range(0, width/spritesize):
                spritelist.append([])
                for j in range(0, height/spritesize):
                    rect = pygame.Rect((i*spritesize,j*spritesize), (spritesize, spritesize))
                    image = pygame.Surface(rect.size)
                    image.blit(surf, (0,0), rect)
                    spritelist[i].append(image)

            spritesheet = SpriteSheet(spritelist, spritesize, math.floor(width/spritesize), math.floor(height/spritesize))

            return spritesheet
        return None

if __name__ == "__main__":
    pygame.init()
    sl = SpriteSheetLoader("/home/lennart/programming/python/minimalism/data/")
    sl.load_sprite_sheet("spritesheet.png", 16)




