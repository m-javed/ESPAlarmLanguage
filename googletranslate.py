import requests


def get_key():
    with open('apikey.txt', 'r') as f:
        key = f.readline()
    return key


def translate(key, text, src, dest):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    payload = f'q={text}&target={dest}&source={src}'
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    try:
        data = response.json()['data']
        translations = data['translations']
        translated_text = translations[0]['translatedText']
    except KeyError:
        print(response.text)
        translated_text = ''
    print(f'Translated: {text} --> {translated_text}')
    return translated_text

