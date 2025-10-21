from anthropic.types import Message
from module.shared.ai_model.adapter.response_adapter._interface import ModelResponse, ResponseAdapterInterface


class AnthropicResponseAdapter(ResponseAdapterInterface):

    @staticmethod
    def process_text_message(response: Message) -> str:
       return response.content[0].text

    @staticmethod
    def process(response: Message) -> ModelResponse[Message]:
        content = AnthropicResponseAdapter.process_text_message(response)
        
        return {
            'content': content,
            'model_format': response
        }