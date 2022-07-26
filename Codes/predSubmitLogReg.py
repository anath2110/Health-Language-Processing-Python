# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:22:13 2020

@author: Anindita Nath
"""
import os
import json

def load_from_json(json_file):
    with open(json_file,"r") as fp:
        data= json.loads(fp.read())
    return data

def predSubmitLogReg(pathToResults):
    taskList=["tested_positive", "tested_negative", "death", "cure","can_not_test"]
    subtask_pos=[]
    subtask_neg=[]
    subtask_death=[]
    subtask_cure=[]
    subtask_cant=[]
    pred_pos=[]
    pred_neg=[]
    pred_death=[]
    pred_cure=[]
    pred_cant=[]
  
    for dirpaths,_,_ in os.walk(pathToResults):
        dirpaths=dirpaths.split('\n')
        for dirpath in dirpaths:               
               
            dirname=os.path.basename(dirpath) 
              
            if dirname!="lr_baseline":
                    subtask=str(dirname).split('_')[-1]
                   
                    if subtask=="female" or subtask=="male":
                        subtask="gender"
                    elif subtask=="contact" or subtask=="travel" \
                        or subtask=="long" or subtask=="cure":                
                        subtask=dirname.split('_')[-2] + '_' + dirname.split('_')[-1]
                    if subtask!="gender":
                        task=dirname[:len(dirname)-len(subtask)-1]
                    else:
                        task=dirname[:len(dirname)-len(subtask) -len(dirname.split('_')[-1])-2]
                    #print(task,subtask)
                    if task=="tested_positive" :
                        subtask_pos.append(subtask)
                        if(os.path.isfile(os.path.join(dirpath,"predictions.json"))):
                
                            predictionFile=os.path.join(dirpath,"predictions.json")                
                            predictions=load_from_json(predictionFile)
                            #print(len(predictions))
                            pred_pos.append(predictions)                         
                    if task=="tested_negative" :
                        subtask_neg.append(subtask)
                        if(os.path.isfile(os.path.join(dirpath,"predictions.json"))):                
                            predictionFile=os.path.join(dirpath,"predictions.json")                
                            predictions=load_from_json(predictionFile)
                            pred_neg.append(predictions)
                    if task=="death" :
                        subtask_death.append(subtask)
                        if(os.path.isfile(os.path.join(dirpath,"predictions.json"))):                
                            predictionFile=os.path.join(dirpath,"predictions.json")                
                            predictions=load_from_json(predictionFile)
                            pred_death.append(predictions)
                    if task=="cure" :
                        subtask_cure.append(subtask)
                        if(os.path.isfile(os.path.join(dirpath,"predictions.json"))):                
                            predictionFile=os.path.join(dirpath,"predictions.json")                
                            predictions=load_from_json(predictionFile)
                            pred_cure.append(predictions)
                    if task=="can_not_test" :
                        subtask_cant.append(subtask)
                        if(os.path.isfile(os.path.join(dirpath,"predictions.json"))):                
                            predictionFile=os.path.join(dirpath,"predictions.json")                
                            predictions=load_from_json(predictionFile)
                            pred_cant.append(predictions)
 
    subtask_pos.remove("gender")
    #print(subtask_pos)   
    subtask_neg.remove("gender")
    # print(subtask_neg)    
    # print(subtask_death)    
    # print(subtask_cure)    
    # print(subtask_cant)
    #print(len(pred_pos))
    #print(pred_pos[1][0])
    
    #...for task=="tested_positive"...#
    #...creating prediciton .json file with text predictions...#
    # idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
    #     =inforfrompredictions(pred_pos,subtask_pos)
    # makejsonfile("tested_positive",subtask_pos,idlist,idannoText,pathToResults,"predText")
    #...creating prediciton .json file with offset predictions...#
    idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
        =inforfrompredictions(pred_pos,subtask_pos)
    makejsonfile("tested_positive",subtask_pos,idlist,idannoOffset,pathToResults,"predOffset")
    #...creating prediciton .json file with  gold text annotations...#
    idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
        =inforfrompredictions(pred_pos,subtask_pos)
    makejsonfile("tested_positive",subtask_pos,idlist,idgoldannoText,pathToResults,"goldAnnoText")
    #...creating prediciton .json file with gold offset annotations...#
    idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
        =inforfrompredictions(pred_pos,subtask_pos)
    makejsonfile("tested_positive",subtask_pos,idlist,idgoldOffset,pathToResults,"goldAnnoOffset")
    

    #  #...for task=="tested_negative"...#
    # #...creating prediciton .json file with text predictions...#
    # idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
    #     =inforfrompredictions(pred_neg,subtask_neg)
    # makejsonfile("tested_negative",subtask_neg,idlist,idannoText,pathToResults,"predText")
    # #...creating prediciton .json file with offset predictions...#
    # idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
    #     =inforfrompredictions(pred_neg,subtask_neg)
    # makejsonfile("tested_negative",subtask_neg,idlist,idannoOffset,pathToResults,"predOffset")
    # #...creating prediciton .json file with  gold text annotations...#
    # idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
    #     =inforfrompredictions(pred_neg,subtask_neg)
    # makejsonfile("tested_negative",subtask_neg,idlist,idgoldannoText,pathToResults,"goldAnnoText")
    # #...creating prediciton .json file with gold offset annotations...#
    # idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
    #     =inforfrompredictions(pred_neg,subtask_neg)
    # makejsonfile("tested_negative",subtask_neg,idlist,idgoldOffset,pathToResults,"goldAnnoOffset")  



    # #...for task=="death"...#
    # #...creating prediciton .json file with text predictions...#
    # idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
    #     =inforfrompredictions(pred_death,subtask_death)
    # makejsonfile("death",subtask_death,idlist,idannoText,pathToResults,"predText")
    # #...creating prediciton .json file with offset predictions...#
    # idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
    #     =inforfrompredictions(pred_death,subtask_death)
    # makejsonfile("death",subtask_death,idlist,idannoOffset,pathToResults,"predOffset")
    # #...creating prediciton .json file with  gold text annotations...#
    # idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
    #     =inforfrompredictions(pred_death,subtask_death)
    # makejsonfile("death",subtask_death,idlist,idgoldannoText,pathToResults,"goldAnnoText")
    # #...creating prediciton .json file with gold offset annotations...#
    # idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
    #     =inforfrompredictions(pred_death,subtask_death)
    # makejsonfile("death",subtask_death,idlist,idgoldOffset,pathToResults,"goldAnnoOffset") 


    # #...for task=="cure"...#
    # #...creating prediciton .json file with text predictions...#
    # idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
    #     =inforfrompredictions(pred_cure,subtask_cure)
    # makejsonfile("cure",subtask_cure,idlist,idannoText,pathToResults,"predText")
    # #...creating prediciton .json file with offset predictions...#
    # idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
    #     =inforfrompredictions(pred_cure,subtask_cure)
    # makejsonfile("cure",subtask_cure,idlist,idannoOffset,pathToResults,"predOffset")
    # #...creating prediciton .json file with  gold text annotations...#
    # idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
    #     =inforfrompredictions(pred_cure,subtask_cure)
    # makejsonfile("cure",subtask_cure,idlist,idgoldannoText,pathToResults,"goldAnnoText")
    # #...creating prediciton .json file with gold offset annotations...#
    # idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
    #     =inforfrompredictions(pred_cure,subtask_cure)
    # makejsonfile("cure",subtask_cure,idlist,idgoldOffset,pathToResults,"goldAnnoOffset")      


    # #...for task=="can_not_test"...#
    # #...creating prediciton .json file with text predictions...#
    # idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
    #     =inforfrompredictions(pred_cant,subtask_cant)
    # makejsonfile("can_not_test",subtask_cant,idlist,idannoText,pathToResults,"predText")
    # #...creating prediciton .json file with offset predictions...#
    # idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
    #     =inforfrompredictions(pred_cant,subtask_cant)
    # makejsonfile("can_not_test",subtask_cant,idlist,idannoOffset,pathToResults,"predOffset")
    # #...creating prediciton .json file with  gold text annotations...#
    # idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
    #     =inforfrompredictions(pred_cant,subtask_cant)
    # makejsonfile("can_not_test",subtask_cant,idlist,idgoldannoText,pathToResults,"goldAnnoText")
    # #...creating prediciton .json file with gold offset annotations...#
    # idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset\
    #     =inforfrompredictions(pred_cant,subtask_cant)
    # makejsonfile("can_not_test",subtask_cant,idlist,idgoldOffset,pathToResults,"goldAnnoOffset")        
#.........function that extracts inofrmation from predictions per task required 
#.........to create .json file sin submission format..................#
def inforfrompredictions(predictionslist,subtasklist):
    idlist=[]
    idannoText=[]
    idannoOffset=[]
    idgoldannoText=[]
    idgoldOffset=[]
    for idx in range(len(predictionslist)):
        for eachline in predictionslist[idx]:            
            eachlinesplit=eachline.split("^")   
            
            tweetid=eachlinesplit[3].split(':')[1] 
            #print(tweetid)
            idlist.append(tweetid)
           
            annoText=eachlinesplit[5]
            #print(annoText)
            annoOffSet=eachlinesplit[6]
            goldannoText=eachlinesplit[9]
            goldannoOffSet=eachlinesplit[10]
            idannoText.append((tweetid,annoText))
            idannoOffset.append((tweetid,annoOffSet))
            idgoldannoText.append((tweetid,goldannoText))
            idgoldOffset.append((tweetid,goldannoOffSet))
                            
    
    #print(len(idlist))
    idlist=list(set(idlist))
    #print(len(idlist))
    #print(len(idannoText))
    idannoText=list(set(idannoText))
    #print(len(idannoText))
    #print(idannoText)
    idannoOffset=list(set(idannoOffset))
    idgoldannoText=list(set(idgoldannoText))
    idgoldOffset=list(set(idgoldOffset))
    return idlist,idannoText,idannoOffset,idgoldannoText,idgoldOffset

#............creating predictions .json files.................................#
def makejsonfile(task,subtaskList,idlist,idannoList,jsonfilepath,jsonsubmissiontype):
    
    label={}
    jsonfilename=jsonfilepath + "\\" + task + "_" + jsonsubmissiontype + ".json"
    for eachid in idlist:
        #print(eachid)
        label[eachid]={}
  
        for subtask in subtaskList:
            subtask="part2-" +subtask + ".Response"
            
            label[eachid][subtask]={}
            annotationList=[]
            for annoindex in range(len(idannoList)):                     
                
                  eachidinfile=idannoList[annoindex][0]
                  #print(eachidinfile)
                  splittedannotation=idannoList[annoindex][1].strip('\'').split(":") 
                 
                  subtaskinfile=splittedannotation[0]
                  #print(subtask + "  : " + subtaskinfile)
                  if eachid==eachidinfile and subtask==subtaskinfile:  
                              
                              annotation=splittedannotation[1]
                              #print(annotation)
                              #print(eachid + " " + subtask + " " +\
                                   #subtaskinfile +  " " + annotation )
                              if(annotation!=""):                                  
                                 annotationList.append(annotation)
                                 label[eachid][subtask]=annotationList
                             
                              
            if len(label[eachid][subtask])==0:
                  label[eachid][subtask]=['Not Specified']
                                  
   

    labeljson={}
    for keys,values in label.items():
        
        labeljson[keys]={'id':keys,'predicted_annotation':values}
    #print(labeljson)
    with open(jsonfilename, 'w') as f:
    		for keys,values in labeljson.items():
     			f.write("%s\n" % json.dumps(values))
             
#....sample run.....#
predSubmitLogReg(r'D:\AninditaPennSummer2020\Box Sync\WNUT2020TASK3_extractEventsfromTwitter\ChallegeWebsite\extract_COVID19_events_from_Twitter-master\extract_COVID19_events_from_Twitter-master\results\lr_baseline')