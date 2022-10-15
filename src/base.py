import abc
from typing import Any


class AbstractRepository(metaclass=abc.ABCMeta):
    _collection: Any

    @abc.abstractmethod
    def _get_one(self, *args, **kwargs):
        raise NotImplementedError()

    @abc.abstractmethod
    def _add_one(self, *args, **kwargs):
        raise NotImplementedError()

    @abc.abstractmethod
    def _delete_one(self, *args, **kwargs):
        raise NotImplementedError()


class AbstractService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def handle(self, *args, **kwargs):
        raise NotImplementedError()

