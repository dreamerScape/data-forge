from abc import ABC, abstractmethod

class DataParser(ABC):
    @abstractmethod
    def parse(self, file_path: str):
        pass


