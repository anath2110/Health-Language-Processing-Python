# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 20:27:15 2020

@author: Anindita Nath
"""
import json
def read_json_line(path):

	output = []
	with open(path, 'r') as f:
		for line in f:
			output.append(json.loads(line))

	return output

def comparejsonFiles(file1,file2):
    file1List=read_json_line(file1)
    file2List=read_json_line(file2)
    # print(len(file1List))
    # print(len(file2List))
    #print(file1List[0])
    idlistfromFile1=[]
    idlistfromFile2=[]
    annoheaderList1=[]
    annoheaderList2=[]
    annoList1=[]
    annoList2=[]
    for each in file1List:
        for keys,values in each.items():
            if keys=="id":
                idlistfromFile1.append(values)
            if keys=="annotation":
                for key, value in values.items():                    
                    annoheaderList1.append(key)
                    #annoList1.append((key,value))
    for each in file2List:
        for keys,values in each.items():
            if keys=="id":
                idlistfromFile2.append(values)
            if keys=="annotation":
                for key, value in values.items():                    
                    annoheaderList2.append(key)
                    #annoList2.append((key,value))
    # print(idlistfromFile1)
    # print(idlistfromFile2)
    # print(annoheaderList1[0])
    # print(annoheaderList2[0])
    if (set(idlistfromFile1)==set(idlistfromFile2)):
        print("identical ids")
    if (set(annoheaderList1)==set(annoheaderList2)):
        print("identical annotation headers")
    # if (set(annoList1)==set(annoList2)):
    #     print("identical annotations")

# list1=['one','two', 'three']
# list2=['one','two', 'three']
# print(set(list1)==set(list2))

comparejsonFiles(r'D:\AninditaPennSummer2020\Box Sync\WNUT2020TASK3_extractEventsfromTwitter\ChallegeWebsite\extract_COVID19_events_from_Twitter-master\extract_COVID19_events_from_Twitter-master\data\can_not_test.jsonl',\
                 r'D:\AninditaPennSummer2020\Box Sync\WNUT2020TASK3_extractEventsfromTwitter\ChallegeWebsite\extract_COVID19_events_from_Twitter-master\extract_COVID19_events_from_Twitter-master\data\newdata\can_not_test.jsonl')
comparejsonFiles(r'D:\AninditaPennSummer2020\Box Sync\WNUT2020TASK3_extractEventsfromTwitter\ChallegeWebsite\extract_COVID19_events_from_Twitter-master\extract_COVID19_events_from_Twitter-master\data\cure_and_prevention.jsonl',\
                 r'D:\AninditaPennSummer2020\Box Sync\WNUT2020TASK3_extractEventsfromTwitter\ChallegeWebsite\extract_COVID19_events_from_Twitter-master\extract_COVID19_events_from_Twitter-master\data\newdata\cure_and_prevention.jsonl')
comparejsonFiles(r'D:\AninditaPennSummer2020\Box Sync\WNUT2020TASK3_extractEventsfromTwitter\ChallegeWebsite\extract_COVID19_events_from_Twitter-master\extract_COVID19_events_from_Twitter-master\data\death.jsonl',\
                 r'D:\AninditaPennSummer2020\Box Sync\WNUT2020TASK3_extractEventsfromTwitter\ChallegeWebsite\extract_COVID19_events_from_Twitter-master\extract_COVID19_events_from_Twitter-master\data\newdata\death.jsonl')
comparejsonFiles(r'D:\AninditaPennSummer2020\Box Sync\WNUT2020TASK3_extractEventsfromTwitter\ChallegeWebsite\extract_COVID19_events_from_Twitter-master\extract_COVID19_events_from_Twitter-master\data\negative.jsonl',\
                 r'D:\AninditaPennSummer2020\Box Sync\WNUT2020TASK3_extractEventsfromTwitter\ChallegeWebsite\extract_COVID19_events_from_Twitter-master\extract_COVID19_events_from_Twitter-master\data\newdata\negative.jsonl')
comparejsonFiles(r'D:\AninditaPennSummer2020\Box Sync\WNUT2020TASK3_extractEventsfromTwitter\ChallegeWebsite\extract_COVID19_events_from_Twitter-master\extract_COVID19_events_from_Twitter-master\data\positive.jsonl',\
                 r'D:\AninditaPennSummer2020\Box Sync\WNUT2020TASK3_extractEventsfromTwitter\ChallegeWebsite\extract_COVID19_events_from_Twitter-master\extract_COVID19_events_from_Twitter-master\data\newdata\positive.jsonl')