import requests

def call_chatgpd(api_key: str, model: str, chat_messages: list):
    baseUrl = 'https://api.openai.com/v1/chat/completions'

    headers = {
        'Content-type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    body = {
        "messages": chat_messages,
        "max_tokens": 4000,
        "model": model
    }

    response = requests.post(baseUrl, headers=headers, json=body)
    responseJson = response.json()
   
    messageChatResult = responseJson['choices'][-1]['message']['content']
    
    return messageChatResult