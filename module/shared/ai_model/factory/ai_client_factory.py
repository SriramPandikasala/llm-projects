# from ..clients.implementation.openai.openai_client import OpenAIClient
from re import A
from module.shared.ai_model.clients.interface import AIClient
from ..clients.implementation import AnthropicClient

class AIClientFactory:
    _instance = {}

    def __init__(self):
        pass

    @staticmethod
    def create_client(client_type: str, client_config: dict) -> AIClient:
        if client_type == 'openai':
            # if AIClientFactory._instance.get(client_type, None) is None:
            #     AIClientFactory._instance[client_type] = OpenAIClient(client_config)
            # return AIClientFactory._instance[client_type]
            pass
        elif client_type == 'anthropic':
            if AIClientFactory._instance.get(client_type, None) is None:
                AIClientFactory._instance[client_type] = AnthropicClient(client_config).init_client()
            return AIClientFactory._instance[client_type]
        else:
            raise ValueError(f"Unknown client type: {client_type}")
