#-*- coding: utf8 -*-
import json

d = {}


with open("newsafr.json", encoding="utf8") as json_file:
      data_json = json.load(json_file)
      tems = data_json["rss"]["channel"]["items"]
      for elements in tems:
          for key, value in elements.items():
              d[len(value.split())] = [value.split()]
              for key_2 in reversed(sorted(value.split())):
                  if len(value[key_2]) <= 10:
                      print(key_2, ":", value[key_2])
                  else:
                      break





