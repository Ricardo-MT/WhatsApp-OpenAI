import os


import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')


def text_complition(prompt: str) -> dict:
    '''
    Call Openai API for text completion

    Parameters:
        - prompt: user query (str)

    Returns:
        - dict
    '''
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            # prompt=f'Human: {prompt}\nAI: ',
            messages=[
            {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=1000,
            frequency_penalty=0,
            presence_penalty=0.5,
            # stop=['Human:', 'AI:']
        )
        return {
            'status': 1,
            'response': response['choices'][0]['message']["content"]
        }
    except:
        return {
            'status': 0,
            'response': ''
        }
        