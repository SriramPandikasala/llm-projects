import os
from module.shared.website_scraper import fetch_website_contents
# from IPython.display import Markdown, display
from module.shared.ai_model.factory.ai_client_factory import AIClientFactory



def summarize_webpage(url: str, max_tokens: int = 300) -> str:
    # Fetch the website content
    content = fetch_website_contents(url)
    if not content:
        return "Failed to fetch the website content."


    system_prompt = f"""
    You are a helpful assistant that summarizes website content.
    """
    # Create a summary prompt
    summary_prompt = f"""
    Please summarize the following content in {max_tokens} tokens or less:
    {content}
    """

    # Create a client for Anthropic
    client = AIClientFactory.create_client('anthropic', {
        'api_key': os.getenv('ANTHROPIC_API_KEY'),
        'model': 'claude-sonnet-4-5',
        'max_tokens': max_tokens
    })

    # Ask the client for a summary

    response = client.ask_query({
        'messages': [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': summary_prompt}
        ]
    })

    return response['response']['content']





