from .music_controller import MusicController

msg_attr = ["type-vel", "delay-before", "wrap-line", "color"]


class SceneProcessor:
    def __init__(self, ui, parser) -> None:
        self.ui = ui
        self.parser = parser
        self.music_controller = MusicController()

    def process(self, scene):
        self._proc_messages(scene)
        return self._proc_option(scene)

    def _proc_messages(self, scene):
        for item in scene:
            if item.tag == "music":
                if item.get("play"):
                    self.music_controller.play_music(item.get("play"))
                elif item.get("stop"):
                    self.music_controller.stop_music()
            elif item.tag == "msg":
                attrs_found = self._get_attr(item, msg_attr)
                wrap_line = attrs_found.get("wrap-line", "True").lower() == "true"
                self.ui.type_message(
                    item.text,
                    delay_before=int(attrs_found.get("delay-before", 100)),
                    wrap_line=wrap_line,
                    type_vel=int(attrs_found.get("type-vel", 50)),
                    color=attrs_found.get("color", "default"),
                )

    def _proc_option(self, scene):
        option = scene.find("option")
        if option is None:
            return None

        queries = option.findall("query")
        if not queries:
            return None

        go_to_ids = [query.get("go-to") for query in queries]
        queries_text = [query.text for query in queries]

        selected_query = self.ui.render_menu(queries_text)

        selected_index = queries_text.index(selected_query)
        go_to_scene_id = go_to_ids[selected_index]

        if go_to_scene_id:
            return go_to_scene_id
        else:
            return None

    def _get_attr(self, tag, attr_rules) -> dict:
        attrs_found = {}
        for attr in attr_rules:
            attr_value = tag.get(attr)
            if attr_value is not None:
                attrs_found[attr] = attr_value
        return attrs_found
