import openai
from config import OPENAI_API_KEY_DEV
from constants.openai import OPENAI_ENGINE, OPENAI_TEMPERATURE, OPENAI_MAX_TOKENS, OPENAI_ASSISTANT_PROMPT, OPENAI_SYSTEM_PROMPT, OPENAI_USER_PROMPT

class OpenAI:

    def __init__(self, engine = OPENAI_ENGINE, keys = OPENAI_API_KEY_DEV, temperature = OPENAI_TEMPERATURE,  max_tokens = OPENAI_MAX_TOKENS):
        self.keys = keys
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        openai.api_key = self.keys

    def chat_completion(self, user_prompt = OPENAI_USER_PROMPT, system_prompt = OPENAI_SYSTEM_PROMPT, assistant_prompt = OPENAI_ASSISTANT_PROMPT):
        user_prompt = user_prompt.encode(encoding = 'ASCII', errors = 'ignore').decode()
        print(f"chat_completion propmpt: {user_prompt}")
        try:
            response = openai.ChatCompletion.create(
                model = self.engine,
                messages = [
                    system_prompt,
                    assistant_prompt,
                    { "role": "user", "content": user_prompt }
                ],
                temperature = self.temperature,
                max_tokens = self.max_tokens
            )
            print(f"response: {response}")
            return response['choices'][0]['message']['content']
        except Exception as oops:
            return "chat_completion error: %s" % oops