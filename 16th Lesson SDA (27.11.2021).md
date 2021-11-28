# 16th Lesson SDA (27.11.2021)

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

```Py
import  requests
import json

# deepl_api_key = "224dd4fb-9c29-8ee9-759a-a71057134c5d:fx"
# deepl_url = "https://api-free.deepl.com/v2/translate"

"""
https://www.deepl.com/docs-api/
"""

def translate(text, target_lang, source_lang=None):
    deepl_api_key = "224dd4fb-9c29-8ee9-759a-a71057134c5d:fx"
    deepl_url = "https://api-free.deepl.com/v2/translate"

    parametry = {
        "auth_key": deepl_api_key,
        "text": text,
        "target_lang": target_lang
    }

    if source_lang:
        parametry.update({"source":source_lang})

    # return requests.get(url=deepl_url, params=parametry).json()
    preklad = requests.get(url=deepl_url, params=parametry).json()
    return preklad["translations"][0]["text"]

text_test = "Kiwi neni zelenina"
jazyk = "EN"

translator_test = translate(text_test, jazyk, "CS")

print(translator_test)
```

```py
import  requests
import json


def translate(text, target_lang, source_lang=None):
    deepl_api_key = "224dd4fb-9c29-8ee9-759a-a71057134c5d:fx"
    deepl_url = "https://api-free.deepl.com/v2/translate"

    parametry = {
        "auth_key": deepl_api_key,
        "text": text,
        "target_lang": target_lang
    }

    # return requests.get(url=deepl_url, params=parametry).json()
    preklad = requests.get(url=deepl_url, params=parametry).json()
    return preklad["translations"][0]["text"]

def translator():
    """INPUT VALUES"""
    text = input("Enter your text for translate: \n")
    target_lang = input("Enter \"EN\" for English, Enter \"DE\" for German: \n")
    return translate(text, target_lang)


print(translator())
```
