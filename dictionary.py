import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def dictionary(word):
    word=word.lower()
    if word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn= input("Did you mean {} instead? Enter Y for yes and N for no" .format(get_close_matches(word,data.keys())[0]))
        if yn =="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="N":
            return "The word doesn't exist in dictionary"
        else:
            return "Sorry!!!..Please repeat the query"
    else:
        return "The word doesn't exist in dictonary"

word=input("enter word:")

result=dictionary(word)
if isinstance(result, list):
    for item in result:
        print(item)
else:
    print(result)
