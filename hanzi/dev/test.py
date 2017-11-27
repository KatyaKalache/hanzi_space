#!/usr/bin/python3
from sys import argv
from pymongo import MongoClient

client = MongoClient()
db = client.dictionary
argument = argv[1]
for i in argument:
  search_char = db.characters.find({"character": i})
  for decomp in search_char:
    elements = decomp["decomposition"]
    print (decomp['character'])
    print (decomp["definition"])
    for each in elements:
      search_radical = db.radicals.find({"radical": each})
      for radical in search_radical:
        print (each, end=" - ")
        print (radical["meaning"])
