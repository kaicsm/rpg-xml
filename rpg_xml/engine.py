from .util import clear_terminal
from .xmlparser import XmlParser
from .scene_processor import SceneProcessor


class Engine:
    def __init__(self, path) -> None:
        self.parser = XmlParser(path)
        self.scene_processor = SceneProcessor()
        self.scenes = self.parser.get_nodes("scene")

    def start_game(self):
        clear_terminal()
        for scene in self.scenes:
            self._process_scene(scene)

    def _process_scene(self, scene):
        self.scene_processor.process(scene)
