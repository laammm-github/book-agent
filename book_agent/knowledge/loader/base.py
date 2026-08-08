from abc import ABC, abstractmethod


class BookLoader(ABC):
    @abstractmethod
    def load(self, path: str):
        raise NotImplementedError
