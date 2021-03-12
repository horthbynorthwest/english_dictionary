import json

data = json.load(open("data.json"))

def definition(word):
    return data[word]

print(definition("help"))