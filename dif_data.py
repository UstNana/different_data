#-*- coding: utf8 -*-
import json
from pprint import pprint

d = {}
with open("newsafr.json", encoding="utf8") as json_file:
     data_json = json.load(json_file)
     for key, value in data_json.items():
         d[len(key)] = [key]
         for key_2, value_2 in value.items():
             d[len(key_2)] = [key_2]
             if key_2 == "channel":
               for key_3, value_3 in value_2.items():
                 d[len(key_3)] = [key_3]
                 print(d)
                 if key_3 == "items":
                     for elements in value_3:
                       for key_4, value_4 in elements.items():
                           d[len(key_4)] = [key_4]


for key in reversed(sorted(d.keys())):
    print(key, ":", d[key])
