from src.entity.entity import Entity


class Player(Entity):
    def __init__(self):
        super(Player, self).__init__()
        self.health = 10

    def update(self):
        pass

    def move(self):
        pass

    def get_sprite(self):
        pass

    def die(self):
        pass

    def action(self):
        pass