from abc import ABC, abstractmethod

class AIClient(ABC):
    def __init__(self, client_config):
        self.client_config = client_config

    @abstractmethod
    def ask_query(self, prompt: str) -> str:
        pass

    @abstractmethod
    def init_client(self) -> None:
        pass