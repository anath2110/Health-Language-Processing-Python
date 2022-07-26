import numpy as np
import json
# subtasklist=['name','age','relation','close_contact','where','when']
# tweetdetails=[('123456','jjjhgjhjhgj gfhhggjghj',1,'jjj',[62,88]),\
#               ('1569','jjjhgjhjhgj gfhhggjghj',0,'jjj',[28,48]),\
#                   ('123456','jjjhgjhjhgj gfhhggjghj',1,'kkk',[72,49]),\
#                   ('1569','jjjhgjhjhgj gfhhggjghj',0,'kkk',[99,49])]
# updatedlist={}
# already_predicted=[]
# for subtask in subtasklist:
#     updatedlist[subtask]={}
#     for i in range(len(tweetdetails)):
#         updatedlist[subtask][i]={}
#         tweetid=tweetdetails[i][0]
#         tweet=tweetdetails[i][1]
#         predictedlabel=tweetdetails[i][2]
#         chunk=tweetdetails[i][3]
#         chunkoffset=tweetdetails[i][4]
#         if len(already_predicted)>0:
#             if predictedlabel==1:
#                 for j in range(len(already_predicted)):
#                     if subtask == already_predicted[j][0] and tweetid==already_predicted[j][1]:
#                         #print("match")
#                         #print(subtask,i,tweetid)
                       
#                         chunk=[chunk,already_predicted[j][3]]
#                         chunkoffset=[chunkoffset,already_predicted[j][4]]
                    
                  
#         already_predicted.append((subtask,tweetid,predictedlabel,chunk,chunkoffset))
#         list_to_print_tojson = [str(tweetid),str(chunk),str(chunkoffset)]
#         updatedlist[subtask][i]["updated"]=list_to_print_tojson
# #print(already_predicted)
# print(updatedlist)
# gold_chunk=['many friends that','many friends ']
# gold_chunkStr=str(gold_chunk)
# #print(gold_chunkStr)
# #print(len(gold_chunk))
# offsetList=[]
# if len(gold_chunk)==1:
#     goldchunk_start_text_id=tweet.find(gold_chunk[0])
#     goldchunk_end_text_id=goldchunk_start_text_id + len(gold_chunk[0])
#     goldchunkoffset=[goldchunk_start_text_id,goldchunk_end_text_id]
#     #print(goldchunkoffset)
# else:
#     if len(gold_chunk)>1:
#         for eachchunk in gold_chunk:
#             goldchunk_start_text_id=tweet.find(str(eachchunk))
#             goldchunk_end_text_id=(goldchunk_start_text_id + len(str(eachchunk)))
           
#             goldchunkoffset=[goldchunk_start_text_id,goldchunk_end_text_id]
#             #print(goldchunkoffset)
#             offsetList.append(goldchunkoffset)		
#         print(offsetList)
#         print(str(offsetList))            
            
#=============================================================================
y=[]
x1=("'id':'33322'", "part2-where.Response:dsffdgfddfg")
x2=("'id':'2222'", "part2-where.Response:")
x3=("'id':'2222'", "part2-name.Response:dsffdgfddfg")
x4=("'id':'2222'", "part2-name.Response:xyz")
x5=("'id':'2222'", "part2-name.Response:")
x6=("'id':'2222'", "part2-age.Response:[28,49]")
x7=("'id':'2222'", "part2-age.Response:[28,48]")
x8=("'id':'2222'", "part2-age.Response:")
x9=("'id':'33322'", "part2-age.Response:")
ids=["33322","2222"]

y=[x1,x2,x3,x4,x5,x6,x7,x8,x9]
#print(y)
#print(y[1]==y[4])
#print(np.array(y))
#print(np.unique(np.array(y)))
  # insert the list to the set 
list_set = set(y) 
# convert the set to the list 
unique_list = (list(list_set)) 
predictionText={}
listtuples=[]
subtaskList=[]
for j in range(len(y)):
    splittedannotation=y[j][1].split(":")
                      #print(splittedannotation)
    subtaskList.append(splittedannotation[0])
subtaskList=list(set(subtaskList))

for i in ids:
  
    predictionText[i]={}
  
    for subtask in subtaskList:
        predictionText[i][subtask]={}
        predannolist=[]
        for annoindex in range(len(y)):                     
                
                  eachid=y[annoindex][0].split(":")[1].strip('\'')
                  splittedannotation=y[annoindex][1].split(":") 
                  if i==eachid and subtask==splittedannotation[0]:  
                              
                              annotation=splittedannotation[1]
                              #print(subtask + " " + annotation )
                              if(annotation!=''):
                                  predannolist.append(annotation)
                                  predictionText[i][subtask]=\
                                      predannolist
        if len(predictionText[i][subtask])==0:
             predictionText[i][subtask]=['Not Specified']
                                  
    
   

predictionIdText={}
for keys,values in predictionText.items():
    
    predictionIdText[keys]={'id':str(keys),'predicted_annotation':values}
print(predictionIdText)
with open(r'./submit.jsonl', 'w') as f:
		for keys,values in predictionIdText.items():
 			f.write("%s\n" % json.dumps(values))
# output = []
# with open(r'D:\AninditaPennSummer2020\Box Sync\WNUT2020TASK3_extractEventsfromTwitter\ChallegeWebsite\extract_COVID19_events_from_Twitter-master\extract_COVID19_events_from_Twitter-master\data\can_not_test.jsonl', 'r') as f:
#         for line in f:
#             output.append(json.loads(line))
# question_tag = output[0]['annotation']
# #print(output)
# print(question_tag)
# =============================================================================
