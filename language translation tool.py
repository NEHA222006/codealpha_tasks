import requests

def translate_text_ms(text, target_language, subscription_key, region):
    endpoint = f"https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to={target_language}"
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': region,
        'Content-Type': 'application/json'
    }
    body = [{'Text': text}]
    
    response = requests.post(endpoint, headers=headers, json=body)
    
    if response.status_code == 200:
        translation = response.json()[0]['translations'][0]['text']
        return translation
    else:
        return "Error in translation request"

# Example usage
if __name__ == "__main__":
    text = input("Enter the text you want to translate: ")
    target_language = input("Enter the target language (e.g., 'en' for English, 'fr' for French): ")
    subscription_key = input("Enter your Microsoft Translator API subscription key: ")
    region = input("Enter your Azure region: ")
    
    translated_text = translate_text_ms(text, target_language, subscription_key, region)
    print(f"Translated text: {translated_text}")
