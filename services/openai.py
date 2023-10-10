import openai
import os
from flask import jsonify

def gpt3_completion(prompt, engine = 'gpt-3.5-turbo-16k', temp = 0.5, top_p = 0.3, tokens = 1000):
    openai_api_key = os.environ.get('OPENAI_GPT3_API_KEY')
    openai.api_key = openai_api_key
    prompt = prompt.encode(encoding = 'ASCII', errors = 'ignore').decode()
    try:
        response = openai.ChatCompletion.create(
            model = engine,
            messages = [
                { "role": "system", "content": "You are a helpful tax CPA for the United States of America with experience working with the IRS." },
                { "role": "user", "content": prompt }
            ],
            temperature = temp,
            max_tokens = tokens
        )
        return response['choices'][0]['message']['content']
    except Exception as oops:

        return "GPT-3 error: %s" % oops


def gpt4_completion(prompt, engine = 'gpt-4', temp = 0.5, top_p = 0.3, tokens = 1000):
    openai_api_key = os.environ.get('OPENAI_GPT4_API_KEY')
    openai.api_key = openai_api_key
    prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()
    try:
        response = openai.ChatCompletion.create(
            model = engine,
            messages = [
                { "role": "system", "content": "You are a helpful tax CPA for the United States of America with experience working with the IRS." },
                { "role": "user", "content": prompt }
            ],
            temperature = temp,
            max_tokens = tokens
        )
        return response['choices'][0]['message']['content']
    except Exception as oops:

        return "GPT-4 error: %s" % oops
    
def conversation(prompt, response):
    # response = gpt3_completion(prompt)
    # return jsonify({'response': response})
    return ''