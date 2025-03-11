from config.config import config

def save_prompt(text):
    with open(config["FILE_DATA_NAME"], "w") as file:
        file.write(text)
    return "Prompt saved successfully"