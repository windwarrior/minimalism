import abc


class Entity(object):
    __metaclass__ = abc.ABCMeta
    health = 0
    pos_x = 0
    pos_y = 0
    max_vel = 10
    velocity = 0.0, 0.0
    alive = True

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def action(self):
        pass

    @abc.abstractmethod
    def move(self):
        pass

    @abc.abstractmethod
    def get_sprite(self):
        pass

    @abc.abstractmethod
    def die(self):
        pass

    def is_alive(self):
        return self.alive

    def get_max_velocity(self):
        return self.max_vel

    def set_max_velocity(self, vel):
        self.max_vel = vel

    def set_velocity(self, velocity):
        self.velocity = velocity

    def set_velocity(self, vel_x, vel_y):
        self.velocity = vel_x, vel_y

    def set_velocity_x(self, x):
        self.velocity = (float(x), float(self.velocity[1]))

    def set_velocity_y(self, y):
        self.velocity = (float(self.velocity[0]), float(y))

    def get_velocity(self):
        return self.velocity

    def get_x(self):
        return self.pos_x

    def get_y(self):
        return self.pos_y

    def get_xy(self):
        return self.pos_x, self.pos_y

    def set_x(self, x):
        self.pos_x = int(x)

    def set_y(self, y):
        self.pos_y = int(y)

    def draw(self):
        #TODO: draw sprite here @ pos_x,pos_y
        pass