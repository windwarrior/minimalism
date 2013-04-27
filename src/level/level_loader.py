import pygame, os
from tile_color_mapper import ColorToTile
from level import Level

class LevelLoader(object):
    def __init__(self, datapath):
        self.color_to_tile = ColorToTile()
        self.datapath = datapath

    def load_level(self, filename):
        surf = pygame.image.load(os.path.join(self.datapath, filename))
        (width, height) = surf.get_size()

        level = [[None for x in range(width)] for y in range(height)]

        for i in range(height):
            for j in range(width):
                pixelcolor = surf.get_at((j,i))
                level[i][j] = self.color_to_tile.get_tile_by_color(pixelcolor)

        lev_obj = Level(level)
        lev_obj.print_level()               

if __name__ == "__main__":
    ll = LevelLoader("/home/lennart/programming/python/minimalism/data/levels")
    ll.load_level("testlvl1.png")

