import xml.etree.ElementTree as ET


class XmlParser:
    """
    A simple XML parser that extracts data from an XML file.
    """

    def __init__(self, path):
        """
        Initialize the XmlParser object with the given file path.

        Args:
            path (str): Path to the XML file.
        """
        self.path = path
        self._parse_xml()

    def _parse_xml(self):
        """
        Parse the XML file and set the root element.

        Raises:
            FileNotFoundError: If the file is not found.
            ValueError: If the XML format is invalid.
        """
        try:
            self.tree = ET.parse(self.path)
            self.root = self.tree.getroot()
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found at {self.path}") from e
        except ET.ParseError as e:
            raise ValueError(f"Invalid XML format in file {self.path}") from e

    def get_tag(self, tag):
        """
        Get the first occurrence of the specified tag.

        Args:
            tag (str): The tag to search for.

        Returns:
            Element or None: The first occurrence of the specified tag, or None if not found.
        """
        return self.root.find(tag)

    def get_nodes(self, node):
        """
        Get all occurrences of the specified node.

        Args:
            node (str): The node to search for.

        Returns:
            list: A list of elements matching the specified node.
        """
        return self.root.findall(node)

    def get_attribute(self, element, attribute):
        """
        Get the value of the specified attribute of an element.

        Args:
            element (Element): The XML element.
            attribute (str): The attribute name.

        Returns:
            str: The value of the attribute, or None if the attribute is not found.
        """
        return element.get(attribute)

    def get_text(self, element):
        """
        Get the text content of an element.

        Args:
            element (Element): The XML element.

        Returns:
            str: The text content of the element, or None if the element has no text content.
        """
        return element.text.strip() if element.text else None
