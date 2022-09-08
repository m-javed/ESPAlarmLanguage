import requests


def get_key():
	with open('apikey.txt', 'r') as f:
		key = f.readline()
	return key


def translate(key, text, src, dest):
	url = "https://microsoft-translator-text.p.rapidapi.com/translate"
	querystring = {"from": src, "to[0]": dest, "api-version": "3.0", "profanityAction": "NoAction", "textType": "plain"}
	payload = [{"Text": text}]
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": key,
		"X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
	}

	response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
	try:
		translations = response.json()[0]['translations']
		translated_text = translations[0]['text']
	except KeyError:
		print(response.text)
		translated_text = ''
	print(f'Translated: {text} --> {translated_text}')
	if not translated_text:
		print(response.text)
	return translated_text
