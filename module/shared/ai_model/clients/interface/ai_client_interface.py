from abc import ABC, abstractmethod
from typing import TypedDict

class QueryResponse[TQuery, TResponse](TypedDict):
    response: TResponse
    query: TQuery

class AIClient(ABC):
    def __init__(self, client_config):
        self.client_config = client_config

    @abstractmethod
    def ask_query[TQuery, TResponse](self, prompt: str) -> QueryResponse[TQuery, TResponse]:
        pass

    @abstractmethod
    def init_client(self) -> None:
        pass