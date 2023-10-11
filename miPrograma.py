import os
import openai
import spacy
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

modelo = "text-davinci-002"
prompt = "cuenta una historia breve."

respuesta = openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    n=1,
    max_tokens=100)
texto_generado  = respuesta.choices[0].text.strip()
print(texto_generado)

print('***')
modelo_spacy = spacy.load("es_core_news_md")
analisis = modelo_spacy(texto_generado)

for token in analisis:
    print(token.text, token.pos_)