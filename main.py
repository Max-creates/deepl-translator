import requests
from api import API


url = "https://api-free.deepl.com/v2/translate"
api_key = API

text_to_translate = input("Enter text: ")
target_language = input("Enter target language (e.g., IT for Italian): ")

params = {
    'auth_key': api_key,
    'text': text_to_translate,
    'target_lang': target_language
}

response = requests.get(url, data=params)
result = response.json()
translated_text = result['translations'][0]['text']

print("Translated text: ", translated_text)
save = input("Do you want to save the translated text to a file? (yes/no): ").strip().lower()
if save == "yes":
    filename = input("Enter the file name (e.g., translation.txt): ")
    with open(filename, "w") as file:
        file.write(translated_text)
    print(f"Translated text saved to {filename}.")
elif save == "no":
    print("Ok, translation will not be saved. Bye, bye!")