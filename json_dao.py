from abc import ABC, abstractmethod

from model import Post

class AbstractPostDao(ABC):
    """dao 包含查閱、上傳、更新、刪除
    """
    @classmethod
    @abstractmethod
    def get(cls, id):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_all(cls, data: Post):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def add(cls, data: Post):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def update(cls, data: Post):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def delete(cls, data: Post):
        raise NotImplementedError
    