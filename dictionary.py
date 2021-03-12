import json

data = json.load(open("data.json"))

def definition(word):
    if word in data:
        return data[word]
    else:
        return "That word doesn't exist. Please double check your spelling."

print(definition("help"))