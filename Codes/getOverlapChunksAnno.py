# -*- coding: utf-8 -*-
#Anindita Nath
#Aug 8th, 2020

"""
Spyder Editor

This is a temporary script file.
"""
import json
def read_json_line(path):
    lines = []
    #fieldsarray=[]
    with open(path, 'r') as f:
        for line in f:
            lines.append(json.loads(line))            
            # fields=line.split(",")
            # for field in fields:
            #     fieldsarray.append(field)              
          
    #return lines,fieldsarray
    return lines

#lines,fieldsarray=read_json_line(r"D:/AninditaPennSummer2020/Box Sync/WNUT2020TASK3_extractEventsfromTwitter/ChallegeWebsite/extract_COVID19_events_from_Twitter-master/extract_COVID19_events_from_Twitter-master/dataSample/sample.jsonl")
# lines=read_json_line(r"D:/AninditaPennSummer2020/Box Sync/WNUT2020TASK3_extractEventsfromTwitter/ChallegeWebsite/extract_COVID19_events_from_Twitter-master/extract_COVID19_events_from_Twitter-master/dataSample/sample.jsonl")
# print(lines[0])

def main():
   annotationLines= read_json_line(r"D:/AninditaPennSummer2020/Box Sync/WNUT2020TASK3_extractEventsfromTwitter/ChallegeWebsite/extract_COVID19_events_from_Twitter-master/extract_COVID19_events_from_Twitter-master/data/cure_and_prevention-add_text.jsonl")
   #annotationLines= read_json_line(r"D:/AninditaPennSummer2020/Box Sync/WNUT2020TASK3_extractEventsfromTwitter/ChallegeWebsite/extract_COVID19_events_from_Twitter-master/extract_COVID19_events_from_Twitter-master/dataSample/sample.jsonl")
   
   annotations_dict = {}
   #predictions_dict={}
   for each_line in annotationLines:
        annotations_dict[each_line['id']] = each_line['annotation']
   #print(annotations_dict)
   counttotal=0
   for key, annotations in annotations_dict.items():
       
       uniqueannotatedvalue=[]
       
       for eachtask in annotations:
           
         annotatedvalue= [i for i in annotations[eachtask] if i!= 'yes' and i!= 'Yes' and i!= 'no' and i!= 'No' and i!= 'Not Specified' and i!= 'N'and i!= 'O' and i!= '_' and i!= 'C' and i!= 'S' and i!= 'E' and i!= 'U']
            
         if annotatedvalue!=[]:
             #print(annotatedvalue)

             if(annotatedvalue not in uniqueannotatedvalue):
                 uniqueannotatedvalue.append(annotatedvalue)
                 
             else:
                 
                 counttotal=counttotal+1
                 print(key, eachtask,annotations[eachtask])
                 #print("Duplicate" + ":" + str(count))
                 #print(key)
                 #print(annotatedvalue)
   
  
   print("Duplicate" + ":" + str(counttotal))            
       
  
   
   

  
if __name__ == '__main__':
   main()