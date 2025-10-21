

from abc import ABC
from typing import TypedDict


class ModelResponse[T](TypedDict):
    content: str
    model_format: T

class ResponseAdapterInterface(ABC):
    def process[T](self, response: T) -> ModelResponse[T]:
        raise NotImplementedError


__all__ = [
    'ModelResponse',
    'ResponseAdapterInterface'
]