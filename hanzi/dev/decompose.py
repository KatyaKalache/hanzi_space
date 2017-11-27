#!/usr/bin/python3
# Decomposes character into components

from sys import argv
from pymongo import MongoClient
import re

client = MongoClient()
db = client.dictionary

def character_print(argument):
# Finds the in database and returns the object with its dictionary
    counter = 0
    seen = []
    final = []
    # Validates that Chinese character passed
    valid = re.findall(r'[\u4e00-\u9fff]+', argument)
    if valid == []:
        return ("Please enter a Chinese character")
    while (counter < len(argument)):
        for i in valid:
            for j in i:
                search_char = (db.characters.find({"character": j}))
                for decomp in search_char:
                    character = (decomp["character"])
                    final.append(character)
            return (final)

def decom(argument):
# Finds the in database and returns the object with its dictionary
    counter = 0
    seen = []
    final = []
    # Validates that Chinese character passed
    valid = re.findall(r'[\u4e00-\u9fff]+', argument)
    if valid == []:
        return ("Please enter a Chinese character")
    while (counter < len(argument)):
        for i in valid:
            for j in i:
                search_char = (db.characters.find({"character": j}))
                for decomp in search_char:
                    character = (decomp["character"])
                    definition = (decomp["definition"])
                    cd = character + "  " + definition
                seen.append(cd)
                for charac in seen:
                    if charac not in final:
                        final.append(cd)
                counter += 1
            return (final)


def ele(argument):
# Finds elements from one db and their meanings from another
    counter = 0
    rad_mean = []
    valid = re.findall(r'[\u4e00-\u9fff]+', argument)
    seen = []
    seen_rad = []
    cr = []
    elem = []
    if valid == []:
        return ("Please enter a Chinese character")

    while (counter < len(argument)):
        for i in valid:
            for j in i:
                search_char = (db.characters.find({"character": j}))
                for decomp in search_char:
                    character = (decomp["character"])
                    elements = (decomp["decomposition"])
                    etymology = (decomp["etymology"])
                    char_el = character + "  =>   " + "  " + elements[1:]
                    seen.append(char_el)
                    for i in seen:
                        if i not in cr:
                            cr.append(i)
                    for each in elements:
                        search_radical = db.radicals.find({"radical": each})
                        for radical in search_radical:
                            r = (each + " " + radical["meaning"])
                            seen_rad.append(r)
                            for j in seen_rad:
                                if j not in cr:
                                    cr.append(j)
                counter += 1
            return (cr)

if __name__ == '__main__':
    pass
