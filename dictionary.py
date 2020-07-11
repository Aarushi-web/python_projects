import json
from difflib import get_close_matches

data= json.load (open("original.json"))

print("Welcome to my dictionary!")
print("_________________________")
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()] 
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead of" %get_close_matches(word, data.keys())[0])
        decide = input("Press y for yes or n for no: ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            print("The word is not in the dictionary. Try Google!")
        else:
            return("Please check your input again")
    else :
        print("The word is not in the dictionary. Try Google!")
   
word= input("Enter the word you want to search: ")
output = translate(word)
if type(output) == list:
    for item in output :
        print(item)
else:
    print(output)