#!/usr/bin/python3
# repalce key name CHARACTER with character

with open('./dictionary.txt', mode='r', encoding='UTF-8') as fin:
  with open('./fin_dictionary.txt', mode='w',  encoding='UTF-8') as fout:
    for line in fin:
      fout.write(line.replace("HINT", "hint"))
