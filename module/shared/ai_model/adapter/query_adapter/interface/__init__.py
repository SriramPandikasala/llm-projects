from abc import ABC, abstractmethod
from typing import TypedDict, Literal

class AppPromptMessage(TypedDict):
    role: Literal["system", "user"]
    content: str

class ConvertedPromptMessage[T](AppPromptMessage):
    model_format: [T]


class QueryAdapterInterface(ABC):
    def query(self, query: str) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def process[T](self, prompt: list[AppPromptMessage]) -> list[ConvertedPromptMessage[T]]:
        pass

__all__ = [
    'QueryAdapterInterface',
    'AppPromptMessage',
    'ConvertedPromptMessage'
]