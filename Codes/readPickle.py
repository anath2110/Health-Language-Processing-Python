# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:11:42 2020

@author: isguser
"""
import pickle

def load_from_pickle(pickle_file):
	with open(pickle_file, "rb") as pickle_in:
		return pickle.load(pickle_in)
task_instances_dict, tag_statistics, question_keys_and_tags=load_from_pickle('../dataSample/positivesample2.pkl')
print(tag_statistics)
#print(task_instances_dict)
# =============================================================================
# x="abc"
# y="def"
# z=(x,y)
# print(z)
# =============================================================================
