

from module.proj_01.index import summarize_webpage


def execute():
    config = {
        'url': 'https://code.visualstudio.com/docs/python/environments',
        'max_tokens': 300
    }
    
    response = summarize_webpage(config['url'], config['max_tokens'])
    print(response)