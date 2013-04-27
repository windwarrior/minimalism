import abc

class BaseState(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, game):
        self.game = game

    @abc.abstractmethod
    def on_state_changed(self):
        # the method called on changing the state to this state
        pass

    @abc.abstractmethod
    def render(self):
        pass

    @abc.abstractmethod
    def process_events(self, events):     
        pass

    @abc.abstractmethod
    def update(self):
        pass
