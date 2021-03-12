import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def definition(word):
    # data is only lower case, so lets change it all to lower
    word = word.lower()
    # simple boolean check to see if word exists in data
    if word in data:
        return data[word]
    # checks to see if data has any close matches
    elif len(word_check(word)) > 0:
        return "Did you mean %s?" % word_check(word)[0]
    else:
        return "That word doesn't exist. Please double check your spelling."

def word_check(word):
    return get_close_matches(word, data.keys(), cutoff=0.8)

word = input("Enter word: ")

print(definition(word))