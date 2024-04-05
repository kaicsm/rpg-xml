import xml.etree.ElementTree as ET


class XmlParser:
    def __init__(self, path):
        self.path = path
        self._parse_xml()

    def _parse_xml(self):
        try:
            self.tree = ET.parse(self.path)
            self.root = self.tree.getroot()
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found at {self.path}") from e
        except ET.ParseError as e:
            raise ValueError(f"Invalid XML format in file {self.path}") from e

    def get_tag(self, tag):
        return self.root.find(tag)

    def get_nodes(self, node):
        return self.root.findall(node)

    def get_node_by_id(self, id):
        """Retorna a cena pelo id"""
        for node in self.root.iter():
            if node.get("id") == id:
                return node
        return None

    def get_attribute(self, element, attribute):
        return element.get(attribute)

    def get_text(self, element):
        return element.text.strip() if element.text else None
