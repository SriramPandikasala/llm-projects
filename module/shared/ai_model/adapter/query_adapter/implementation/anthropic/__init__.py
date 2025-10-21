from typing import Iterable
from anthropic.types import MessageParam
from ...interface import QueryAdapterInterface, AppPromptMessage

class AnthropicQueryAdapter(QueryAdapterInterface):
    def query(self, query: str) -> str:
        raise NotImplementedError
    
    @staticmethod
    def process_if_system_prompt(prompt: AppPromptMessage) -> str:
        if prompt['role'] == 'system':
            new_prompt = prompt.copy()
            new_prompt['role'] = 'assistant'

            prompt['model_format'] = new_prompt
        return prompt
    
    @staticmethod
    def process_if_user_prompt(prompt: AppPromptMessage) -> str:
        if prompt['role'] == 'user':
            new_prompt = prompt.copy()
            prompt['model_format'] = new_prompt
        return prompt
    
    @staticmethod
    def process( prompt: list[AppPromptMessage]) -> Iterable[MessageParam]:
        for message in prompt:
            if 'model_format' in message:
                continue
            AnthropicQueryAdapter.process_if_system_prompt(message)
            AnthropicQueryAdapter.process_if_user_prompt(message)

        return prompt


__all__ = [
    'AnthropicQueryAdapter'
]