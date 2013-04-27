from tile import *
from pygame import Color
class ColorToTile(object):
    def __init__(self):
        #TODO uitlezen uit een file
        self.ground = GroundTile()
        self.grass = GrassTile()
        self.airtile = Tile()
        self.list = []
        self.list.append((Color('#971914'), self.ground))
        self.list.append((Color('#00ff00'), self.grass))

    def get_tile_by_color(self, color):
        for (tile_color, tile) in self.list:
            if color == tile_color:
                return tile

        return self.airtile
