#!/usr/bin/python3
# Decomposes character into components

from sys import argv
from pymongo import MongoClient
import re

client = MongoClient()
db = client.dictionary

def decom():
    if (len(argv) < 2):
        print ("Please enter at least one character")
    else:
        argument = argv[1]
        valid = re.findall(r'[\u4e00-\u9fff]+', argument)
        if valid == []:
            print ("Please enter a chinese character")
        for i in valid:
            search_char = db.characters.find({"character": i})
        return (search_char)
search_char=decom()

def get_word(search_char):
    for decomp in search_char:
        character = (decomp["character"])
        definition = (decomp["definition"])
        res = (character + " " + definition)
        print (res)
    return (res)
res = get_word(search_char)
search_char=decom()

def translate(search_char):
    for decomp in search_char:
        elements = (decomp["decomposition"])
        character = (decomp["character"])
        definition = (decomp["definition"])
        res = (character + " " + definition + '\n' + elements)
        print (elements)
    return (elements)
elements = translate(search_char)

def radical(elements):
    for each in elements:
        search_radical = db.radicals.find({"radical": each})
        for radical in search_radical:
            rad_mean = (each + radical["meaning"])
            print (rad_mean)
    return (rad_mean)
rad_mean = radical(elements)
