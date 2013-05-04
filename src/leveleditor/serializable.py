import json
import abc


class Serializable(object):
    def __init__(self):
        pass

    @abc.abstractmethod
    def serialize(self):
        pass


class SerializableLevel(Serializable):
    def __init__(self, layers, entities):
        self.layers = layers
        self.entities = entities

    def serialize(self):
        result = {
            "layers": [l.serialize() for l in self.layers],
            "entities": [e.serialize() for e in self.entities]
        }

        return result

    def serialize_to_json(self):
        return json.dumps(self.serialize())


class SerializableLayer(Serializable):
    def __init__(self, scroll_speed):
        self.scroll_speed = scroll_speed

    def serialize(self):
        result = {
            "scroll_speed": self.scroll_speed
        }

        return result


class SerializableBackgroundLayer(SerializableLayer):
    def __init__(self, scroll_speed, background_image, x_repeat, y_repeat):
        super(SerializableBackgroundLayer, self).__init__(scroll_speed)
        self.background_image = background_image
        self.x_repeat = self.x_repeat
        self.y_repeat = self.y_repeat

    def serialize(self):
        serialize_parent = super(SerializableBackgroundLayer, self).serialize()
        result = {
            "type": "background",
            "background-image": self.background_image,
            "x-repeat": self.x_repeat,
            "y-repeat": self.y_repeat
        }

        return dict(json.loads(serialize_parent).items() + result.items())


class SerializableTile(Serializable):
    def __init__(self, type, xpos, ypos):
        self.type = type
        self.xpos = xpos
        self.ypos = ypos

    def serialize(self):
        result = {
            "type": self.type,
            "x-pos": self.xpos,
            "y-pos": self.ypos
        }

        return result