from .util import narrar_historia

# Atributos existentes para o elemento descricao
description_attr = [
    "atraso-antes",
    "quebrar-linha",
    "tom",
]


class SceneProcessor:
    def __init__(self) -> None:
        pass

    def process(self, scene):
        self.scene = scene
        self._proc_description()
        self._proc_option()

    def _proc_description(self):
        # Percorre todas as descricoes que estao dentro de uma cena
        for description in self.scene.findall("descricao"):
            # Coleta todos os atributos encontrados na tag
            attrs_found = self._get_attr(description, description_attr)

            narrar_historia(
                description.text,
                atraso_antes=(
                    int(attrs_found["atraso-antes"])
                    if "atraso-antes" in attrs_found
                    else 0
                ),
                quebrar_linha=(
                    bool(attrs_found["quebrar-linha"])
                    if "quebrar-linha" in attrs_found
                    else True
                ),
                tom=attrs_found["tom"] if "tom" in attrs_found else "normal",
            )

    def _proc_option(self):
        # TODO: Fazer a logica de processamento para as opcoes
        pass

    def _get_attr(self, tag, attr_rules):
        # Armazena os atributos encontrados
        attrs_found = {}
        for attr in attr_rules:
            attr_value = tag.get(attr)
            if attr_value is not None:
                # "atraso-antes":"..."
                attrs_found[attr] = attr_value
        return attrs_found
