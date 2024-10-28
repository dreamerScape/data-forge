import json

from parsers.parser import DataParser

class JsonParser(DataParser):
    def parse(self, file_path: str):
        with open(file_path, 'r') as file:
            return json.load(file)
