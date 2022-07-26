# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 16:59:20 2020

@author: isguser
"""
import jsonlines
import json
import csv

with open('./data/tweets/positive.tsv') as file:
    reader = csv.DictReader(file, delimiter="\t")
    data = list(reader)
    jsondata=json.dumps(data)



# with open('./data/tweets/positive.json', 'r') as f:
#     json_data = json.load(f)

# with jsonlines.open('./data/tweets/positive.jl', 'w') as writer:
#     writer.write_all(json_data)

# import json

# with open('./data/tweets/positive.json', 'r') as f:
#     json_data = json.load(f)
    
# with open('./data/tweets/positive.jl', 'w') as outfile:
#     for entry in json_data:
#         json.dump(entry, outfile)
#         outfile.write('\n')