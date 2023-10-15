from constants.openai import OPENAI_USER_PROMPT
from models.openai import OpenAI

openai = OpenAI()
def chat_completion(user_prompt = OPENAI_USER_PROMPT):
    return openai.chat_completion(user_prompt)