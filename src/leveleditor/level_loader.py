import json
from src.leveleditor.serializable import SerializableLevel


class LevelLoader(object):
    def __init__(self):
        pass

    def load_from_file(self, filepath):
        f = open(filepath)
        json_obj = json.load(f)

        try:
            layers = self._load_layers(json_obj["layers"])
            entities = self._load_entities(json_obj["entities"])

            return SerializableLevel(layers, entities)
        except KeyError as keyerror:
            print keyerror.message
        except LevelLoadException as levelload:
            print levelload.message

    def _load_layers(self, json):
        pass

    def _load_single_layer(self, json):
        pass

    def _load_entities(self, json):
        pass

    def _load_single_entity(self, json):
        pass


class LevelLoadException(Exception):
    pass
