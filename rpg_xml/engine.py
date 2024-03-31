from .util import TerminalUI
from .xmlparser import XmlParser
from .scene_controller import SceneController


class Engine:
    def __init__(self, path) -> None:
        self.parser = XmlParser(path)
        self.ui = TerminalUI()
        self.scene_processor = SceneController(self.ui, self.parser)
        self.scenes = self.parser.get_nodes("scene")
        self.current_scene_index = 0

    def start_game(self):
        self.ui.clear_screen()
        self.process_scene(self.current_scene_index)
        self.ui.run_forever()

    def process_scene(self, scene_index):
        scene = self.scenes[scene_index]
        next_scene_id = self.scene_processor.process(scene)
        if next_scene_id is not None:
            next_scene_index = self.get_scene_index_by_id(next_scene_id)
            if next_scene_index is not None:
                self.current_scene_index = next_scene_index
                self.process_scene(self.current_scene_index)
            else:
                self.ui.type_message("Cena não encontrada", color="red")
        else:
            self.ui.type_message("Fim do jogo", color="red")
            self.ui.close()

    def get_scene_index_by_id(self, scene_id):
        for i, scene in enumerate(self.scenes):
            if scene.get("id") == scene_id:
                return i
        return None
