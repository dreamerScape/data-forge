import yaml

from parsers.parser import DataParser

class YamlParser(DataParser):
    def parse(self, file_path: str):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)