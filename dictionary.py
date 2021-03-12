import json

data = json.load(open("data.json"))

def definition(word):
    # data is only lower case, so lets change it all to lower
    word = word.lower()
    # simple boolean check to see if word exists in data
    if word in data:
        return data[word]
    else:
        return "That word doesn't exist. Please double check your spelling."

print(definition("help"))