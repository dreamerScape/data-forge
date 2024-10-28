from parsers.json_parser import JsonParser
from parsers.parser import DataParser
from parsers.xml_parser import XmlParser
from parsers.yaml_parser import YamlParser


class ParserFactory:
    @staticmethod
    def get_parser(file_type: str) -> DataParser:
        if file_type == 'json':
            return JsonParser()
        elif file_type == 'yaml':
            return YamlParser()
        elif file_type == 'xml':
            return XmlParser()
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
