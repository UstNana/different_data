#-*- coding: utf8 -*-
import json


d = {}
with open("newsafr.json", encoding="utf8") as json_file:
     data_json = json.load(json_file)
     for key, value in data_json.items():
         for key_2, value_2 in value.items():
             if key_2 == "channel":
               for key_3, value_3 in value_2.items():
                 d[len(value_3)] = [value_3]
                 if key_3 == "items":
                     for elements in value_3:
                       for key_4, value_4 in elements.items():
                           d[len(value_4)] = [value_4]


for key in reversed(sorted(d.keys())):
    if len(d[key]) <= 10:
        print(key, ":", d[key])
    else:
        break

