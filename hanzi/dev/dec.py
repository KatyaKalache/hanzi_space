#!/usr/bin/python3
# Decomposes character into components

from sys import argv
from pymongo import MongoClient
import re
from flask import jsonify

client = MongoClient()
db = client.dictionary


def decom(argument):
# Finds the in database and returns the object with its dictionary
    counter = 0
    # Validates that Chinese character passed
    valid = re.findall(r'[\u4e00-\u9fff]+', argument)
    res = []
    final = ""
    rad_mean = ""
    if (len(argument) < 1):
        return ("Please enter at least one character")
    if valid == []:
        return ("Please enter a Chinese character")

    while (counter < len(argument)):
        for i in valid:
            for j in i:
                search_char = (db.characters.find({"character": j}))
                res.append(search_char)
                for obj in res:
                    for decomp in obj:
                        character = (decomp["character"])
                        definition = (decomp["definition"])
                        char_def = character + " " + definition
                        final += char_def + "\n"
                        elements = (decomp["decomposition"])
                        for each in elements:
                            search_radical = db.radicals.find({"radical": each})
                            for radical in search_radical:
                                r = (each + " " + radical["meaning"] + "\n")
                                rad_mean += r
            the_res = final + rad_mean
            return (the_res)
        counter += 1

if __name__ == '__main__':
    pass
