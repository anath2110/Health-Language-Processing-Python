import numpy as np
import json
subtasklist=['name','age','relation','close_contact','where','when']
tweetdetails=[('123456','jjjhgjhjhgj gfhhggjghj',1,'jjj',[28,48]),\
              ('123456','jjjhgjhjhgj gfhhggjghj',0,'jjj',[28,48]),\
                  ('123456','jjjhgjhjhgj gfhhggjghj',1,'kkk',[28,49])
                  ('896666','jjjhgjhjhgj gfhhggjghj',1,'kkk',[28,49])]
already_predicted=[]
for subtask in subtasklist:
    for i in range(10):
        tweetid='12356'
        tweet="My friends are not my friends, many friends that say are liars"
        predictedlabel=1
        already_predicted.append([subtask,tweetid,predictedlabel,str(chunk),str(chunkoffset)])
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
# y=[]
# x1=("'id':'33322'", "part2-where.Response:['dsffdgfddfg']")
# x2=("'id':'2222'", "part2-where.Response:['Not Specified']")
# x3=("'id':'2222'", "part2-name.Response:['dsffdgfddfg']")
# x4=("'id':'2222'", "part2-name.Response:['xyz']")
# x5=("'id':'2222'", "part2-name.Response:['Not Specified']")
# x6=("'id':'2222'", "part2-age.Response:[[28,49]]")
# x7=("'id':'2222'", "part2-age.Response:[[28,48]]")
# x8=("'id':'2222'", "part2-age.Response:['Not Specified']")
# ids=["33322","2222"]
# 
# y=[x1,x2,x3,x4,x5]
# #print(y)
# #print(y[1]==y[4])
# #print(np.array(y))
# #print(np.unique(np.array(y)))
#  # insert the list to the set 
# list_set = set(y) 
# # convert the set to the list 
# unique_list = (list(list_set)) 
# predictionText={}
# 
# count=0
# for i in ids:
#     print(i)
#     predicted_annotationList=[]
#     subtaskList=[]
#     for j in range(len(y)):
#                   
#                   #print(y[j][0].split(":")[1])
#                   eachid=y[j][0].split(":")[1].strip('\'')
#                   if i==eachid:
#                       
#                       #print("match")
#                       splittedannotation=y[j][1].split(":")
#                       #print(splittedannotation)
#                       subtask=splittedannotation[0]
#                       subtaskList.append(subtask)
#                       predicted_annotation=splittedannotation[1]
#                       #print(predicted_annotation)
#                       predicted_annotationList.append(predicted_annotation)
#                    
#                      
#                       
#                       #print(predicted_annotationList)
#     
#     # print(subtaskList)
#     # print(predicted_annotationList)
#     
#     predictionText[i]={'id':str(i),'predicted_annotation':dict(zip(subtaskList,predicted_annotationList))}
# 
# #print(predictionText)
# with open(r'./submit.jsonl', 'w') as f:
# 		for keys,values in predictionText.items():
# 			f.write("%s\n" % json.dumps(values))
# # output = []
# # with open(r'D:\AninditaPennSummer2020\Box Sync\WNUT2020TASK3_extractEventsfromTwitter\ChallegeWebsite\extract_COVID19_events_from_Twitter-master\extract_COVID19_events_from_Twitter-master\data\can_not_test.jsonl', 'r') as f:
# #         for line in f:
# #             output.append(json.loads(line))
# # question_tag = output[0]['annotation']
# # #print(output)
# # print(question_tag)
# =============================================================================
