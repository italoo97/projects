from openai import OpenAI
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GEMINI_KEY = os.getenv('GEMINI_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)
client2 = genai.Client(api_key=GEMINI_KEY)

def get_car_ai(model, brand, model_year):   
    message = ''''Faça uma descrição atrativa para o carro {} {} {} , Utilize apenas 250 caracteres que convencem o cliente.'''
    try:    
        message = message.format(brand, model, model_year)
        response = client.chat.completions.create(
            messages=[
                {
                    'role': 'user',
                    'content': message
                }
            ],
            max_tokens=1000,
            model= 'gpt-3.5-turbo',
        )
        return response.choices[0].message.content
    except Exception as e:
        response = client2.models.generate_content(
            model="gemini-2.5-flash",
            contents=message
        )
        return response.text