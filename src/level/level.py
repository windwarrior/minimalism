class Level(object):
    def __init__(self, level_array):
        self.level_array = level_array

    def print_level(self):
        for row in self.level_array:
            print row
