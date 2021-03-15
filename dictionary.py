import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def definition(word):
    # data is only lower case, so lets change it all to lower
    word = word.lower()
    # simple boolean check to see if word exists in data
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    # checks to see if data has any close matches
    elif len(word_check(word)) > 0:
        # I am dumb
        # if you don't use return here, the program will return None.
        # even if there are returns in the method you're calling! 
        return word_logic(word)
    else:
        return "That word doesn't exist. Please double check your spelling."

def word_check(word):
    return get_close_matches(word, data.keys(), cutoff=0.8)

def word_logic(word):
    yn = input("Did you mean %s? Enter Y/N: " % word_check(word)[0])
    yn = yn.lower()
    if yn == "Y":
        return data[word_check(word)[0]]
    elif yn == "N":
        return "That word doesn't exist. Please double check your spelling."
    else:
        return "I didn't understand that"


word = input("Enter word: ")

output = definition(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)