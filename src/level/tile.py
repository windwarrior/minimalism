class Tile(object):
    def __init__(self):
        pass

    def isSolid(self):
        pass

    def __str__(self):
        return " "

    def __repr__(self):
        return self.__str__()


class GroundTile(Tile):
    #TODO implementatie    
    def __str__(self):
        return "x"

    def __repr__(self):
        return self.__str__()

class GrassTile(Tile):
    #TODO implementatie
    def __str__(self):
        return "g"

    def __repr__(self):
        return self.__str__()


