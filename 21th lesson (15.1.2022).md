# 21th lesson (15.1.2022)

```Py
# import this

import re

#scraping bike name from html (wiht spaces, new lines, labels ) - "New"  'Neuron 7 WMN         New'"""
scraped_name = """New  Neuron 7 WMN      \n   New"""

def _normalize_name(raw_name):
    _name = re.sub("New", "", raw_name)
    formatted_name = _name.lstrip().rstrip().replace("\n", "")

    return formatted_name

print(_normalize_name(scraped_name))
```
