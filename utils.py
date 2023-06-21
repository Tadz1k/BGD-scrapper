import re

def clean_tags(text):
    tags = re.findall(r'\\\\u[0-9]{1,4}[a-z A-Z]{0,3}', text)
    for tag in tags:
        text = text.replace(tag, '')
    return text