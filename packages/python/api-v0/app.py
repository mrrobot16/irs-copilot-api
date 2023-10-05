import json
from flask import Flask, jsonify, request
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv("open_ai_api_key")

openai.api_key = openai_api_key

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.get_json()['prompt']
    response = gpt3_completion(prompt)
    return jsonify({'response': response})

def gpt3_completion(prompt, engine='gpt-3.5-turbo-16k', temp=0.5, top_p=0.3, tokens=1000):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    try:
        response = openai.ChatCompletion.create(
            model=engine,
            messages=[
                {"role": "system", "content": "You are a helpful tax CPA for the United States of America with experience working with the IRS."},
                {"role": "user", "content": prompt}
            ],
            temperature=temp,
            max_tokens=tokens
        )
        return response['choices'][0]['message']['content']
    except Exception as oops:

        return "GPT-3 error: %s" % oops
    
 


if __name__ == '__main__':
   app.run(port=5000)