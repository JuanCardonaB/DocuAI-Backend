from config.config import config
import ollama

def load_data():
    with open(config["FILE_DATA_NAME"], 'r', encoding="utf-8") as file:
        return file.read()

def ask_ollama(file_data, question, model="phi3"):
    context = f"Usa la siguiente información para responder en español: {file_data}\n\nPregunta: {question}"
    response = ollama.chat(model=model, messages=[{'role': 'user', 'content': context}])
    return response["message"]["content"]