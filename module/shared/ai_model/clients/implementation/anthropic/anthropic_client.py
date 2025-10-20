from ...interface import AIClient


class AnthropicClient(AIClient):
    client = None

    def __init__(self, client_config):
        super().__init__(client_config)

    def init_client(self):
        from anthropic import Anthropic

        api_key = self.client_config.get('api_key', None)
        self.client = Anthropic(api_key=api_key)

        return self

    def ask_query(self, query_config=None):
        query_config = query_config or {}

        # Loop through the messages and add the role to each message
        for message in query_config.get('messages', None):
            if message['role'] == 'system':
                message['role'] = 'assistant'

        response = self.client.messages.create(

            model=query_config.get('model', None) or self.client_config.get('model', None) or 'claude-sonnet-4-5',
            max_tokens=query_config.get('max_tokens', None) or self.client_config.get('max_tokens', None) or 300, 
            messages=query_config.get('messages', None)
        )
        return response.content