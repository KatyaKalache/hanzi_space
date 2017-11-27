#!/usr/bin/python3
# Decomposes character into components

from sys import argv
from pymongo import MongoClient
import re

client = MongoClient()
db = client.dictionary


def etymol(argument):
# Finds the in database and returns the object with its dictionary
    counter = 0
    # Validates that Chinese character passed
    valid = re.findall(r'[\u4e00-\u9fff]+', argument)
    all_etym = []
    if valid == []:
        return ("Please enter a Chinese character")
    while (counter < len(argument)):
        for i in valid:
            for j in i:
                search_char = (db.characters.find({"character": j}))
                for decomp in search_char:
                    if "etymology" not in decomp:
                        no_etymology = "Etymology info not found"
                        return (no_etymology)
                    etymology = (decomp["etymology"]["hint"])
                    all_etym.append(etymology)
            counter += 1
            return (all_etym)


if __name__ == '__main__':
    pass
