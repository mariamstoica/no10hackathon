import requests
import json
import os
from constants import openai_api_key


def get_summary(topic, location):
    url = "https://api.openai.com/v1/chat/completions"
    
    text = 'provide a summary of what the prime minister should discuss about {} in {} england'.format(topic, location)
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }
    
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    }
    
    response = requests.post(url, headers=headers, json=data)

    return response.json()['choices'][0]['message']['content']