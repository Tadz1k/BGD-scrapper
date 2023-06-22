import re

def clean_tags(text):
    tags = re.findall(r'\\\\u[0-9]{1,4}[a-z A-Z]{0,3}', text)
    tags2 = re.findall(r'\\\\n', text)
    for tag in tags:
        text = text.replace(tag, '')
    for tag2 in tags2:
        text = text.replace(tag2, '')
    return text