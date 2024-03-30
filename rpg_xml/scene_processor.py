from .util import type_message

msg_attr = [
    "delay-before",
    "wrap-line",
    "type-vel",
]


class SceneProcessor:
    def __init__(self) -> None:
        pass

    def process(self, scene):
        self.scene = scene
        self._proc_description()
        self._proc_option()

    def _proc_description(self):
        for msg in self.scene.findall("msg"):
            # Coleta todos os atributos encontrados na tag
            attrs_found = self._get_attr(msg, msg_attr)

            type_message(
                msg.text,
                delay_before=(
                    int(attrs_found["delay-before"])
                    if "delay-before" in attrs_found
                    else 0
                ),
                wrap_line=(
                    bool(attrs_found["wrap-line"])
                    if "wrap-line" in attrs_found
                    else True
                ),
                type_vel=(
                    int(attrs_found["type-vel"]) if "type-vel" in attrs_found else 50
                ),
            )

    def _proc_option(self):
        pass

    def _get_attr(self, tag, attr_rules):
        # Armazena os atributos encontrados
        attrs_found = {}
        for attr in attr_rules:
            attr_value = tag.get(attr)
            if attr_value is not None:
                attrs_found[attr] = attr_value
        return attrs_found
