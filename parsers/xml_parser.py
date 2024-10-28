import xml.etree.ElementTree as ET

from parsers.parser import DataParser

class XmlParser(DataParser):
    def parse(self, file_path: str):
        tree = ET.parse(file_path)
        return tree.getroot()