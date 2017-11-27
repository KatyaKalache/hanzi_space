#!/usr/bin/python3
# inserts key meanings for future dict
with open('./rad2_radicals.txt', mode='r', encoding='UTF-8') as fin:
  with open('./rad3_radicals.txt', mode='w',  encoding='UTF-8') as fout:
    for line in fin:
      fout.write(line.replace("\":\":", "\":\""))
