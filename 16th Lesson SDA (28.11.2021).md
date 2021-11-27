# 16th Lesson SDA (28.11.2021)

• JSON </p>
• API </p>

```Py
import  requests
import json

deepl_api_key = "224dd4fb-9c29-8ee9-759a-a71057134c5d:fx"
deepl_url = "https://api-free.deepl.com/v2/translate"

"""
https://www.deepl.com/docs-api/
"""
LANGUAGES = ["EN", "CS"]

text = "Ahoj jmenuji se Petr"

# vytvorime si slovnik
parametry = {
    "auth_key":deepl_api_key,
    "text": text,
    "target_lang": "DE"
}

# preklad = requests.get(url=deepl_url, params=parametry).text
preklad = requests.get(url=deepl_url, params=parametry).json()
# preklad = requests.get(deepl_url)  # alternativni zapis

print(preklad)
print(preklad["translations"][0]["text"])

```
