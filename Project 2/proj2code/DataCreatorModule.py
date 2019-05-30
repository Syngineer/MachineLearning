
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd



# In[8]:


def createHDataCSV(filename):
    
   #collect Samepaior data 
    samepairDataset = {}
    samepairDataset = pd.read_csv('same_pairs.csv')
    img_id_A   = samepairDataset['img_id_A'].values
    img_id_B = samepairDataset['img_id_B'].values
    target = samepairDataset['target'].values
    
    
    
    featureDataSet = pd.read_csv('HumanObserved-Features-Data.csv')
    
   # print (searchedResult)
    
    #img_id_feature_dataset = samepairDataset['img_id'].values
    imageAData = []
    imageBData = []
    targetData = []
    w, h = 1582, 19;
    featureDataA = [[0 for x in range(w)] for y in range(h)] 
    featureDataB = [[0 for x in range(w)] for y in range(h)]
    featureDataSubtract = [[0 for x in range(w)] for y in range(h)] 
    outPutDatasetSubtract = {}
    outPutDatasetConcat = {}
    
    # search through each value of img_id_A and img_id_B and copy f1 t0 f9 
    for i in range(0,791):
        imageA = img_id_A[i]
        imageB = img_id_B[i]
        searchedResultA = featureDataSet[featureDataSet['img_id'] == imageA]
        searchedResultB = featureDataSet[featureDataSet['img_id'] == imageB]
#        print(imageA)
#        print(imageB)
        imageAData.append(imageA)
        imageBData.append(imageB)
        targetData.append(target[i])
        featuresA = []
        featuresB = []
        
        for j in range(1,10):
            featureName = 'f'+ str(j)
            print(featureName)
            intA = searchedResultA[featureName].values[0]
            intB = searchedResultB[featureName].values[0]
           # print(intA)
           # print(intB)
            featureDataA[j][i] = intA  ;
            featureDataB[j][i] = intB  ;
            featureDataSubtract[j][i] = abs(intA-intB) 
            featuresA.append(intA)
            featuresB.append(intB)
        samepairDataset = {}
    samepairDataset = pd.read_csv('diffn_pairs.csv')
    img_id_A   = samepairDataset['img_id_A'].values
    img_id_B = samepairDataset['img_id_B'].values
    target = samepairDataset['target'].values
    for i in range(0,791):
        imageA = img_id_A[i]
        imageB = img_id_B[i]
        searchedResultA = featureDataSet[featureDataSet['img_id'] == imageA]
        searchedResultB = featureDataSet[featureDataSet['img_id'] == imageB]
#        print(imageA)
#        print(imageB)
        imageAData.append(imageA)
        imageBData.append(imageB)
        targetData.append(target[i])
        featuresA = []
        featuresB = []
        
        for j in range(1,10):
            featureName = 'f'+ str(j)
            print(featureName)
            intA = searchedResultA[featureName].values[0]
            intB = searchedResultB[featureName].values[0]
           # print(intA)
           # print(intB)
            featureDataA[j][791+i] = intA  ;
            featureDataB[j][791+i] = intB  ;
            featureDataSubtract[j][791+i] = abs(intA-intB) 
            featuresA.append(intA)
            featuresB.append(intB)
   
    
    outPutDatasetSubtract["img_id_A"]= imageAData
    outPutDatasetSubtract["img_id_B"]= imageBData
    for j in range(1,10):
        outPutDatasetSubtract['f'+ str(j)] =  featureDataSubtract[j]
    outPutDatasetSubtract["target"]= targetData 
        
    outPutDatasetConcat["img_id_A"]= imageAData
    outPutDatasetConcat["img_id_B"]= imageBData
    for j in range(1,10):
        outPutDatasetConcat['fA'+ str(j)] =  featureDataA[j]
    for j in range(1,10):
        outPutDatasetConcat['fB'+ str(j)] =  featureDataB[j]  
    outPutDatasetConcat["target"]= targetData 
    pd.DataFrame(outPutDatasetSubtract).to_csv("HD_Subtract.csv")
    pd.DataFrame(outPutDatasetConcat).to_csv("HD_Concat.csv")
     
def createGSCDataCSV(filename):
    
    #collect Samepaior data 
    samepairDataset = {}
    samepairDataset = pd.read_csv('GSC-Features-Data/same_pairs.csv')
    img_id_A   = samepairDataset['img_id_A'].values
    img_id_B = samepairDataset['img_id_B'].values
    target = samepairDataset['target'].values
    
    
    
    featureDataSet = pd.read_csv('GSC-Features-Data/GSC-Features.csv')
    
   # print (searchedResult)
    
    #img_id_feature_dataset = samepairDataset['img_id'].values
    imageAData = []
    imageBData = []
    targetData = []
    a = 0;
    w, h = 1430, 513;
    b=w;
    featureDataA = [[0 for x in range(w)] for y in range(h)] 
    featureDataB = [[0 for x in range(w)] for y in range(h)]
    featureDataSubtract = [[0 for x in range(w)] for y in range(h)] 
    outPutDatasetSubtract = {}
    outPutDatasetConcat = {}
    
    # search through each value of img_id_A and img_id_B and copy f1 t0 f9 
#    for i in range(a,b):
#        imageA = img_id_A[i]
#        imageB = img_id_B[i]
#        searchedResultA = featureDataSet[featureDataSet['img_id'] == imageA]
#        searchedResultB = featureDataSet[featureDataSet['img_id'] == imageB]
##        print(imageA)
##        print(imageB)
#        imageAData.append(imageA)
#        imageBData.append(imageB)
#        targetData.append(target[i])
#        featuresA = []
#        featuresB = []
#        
#        for j in range(1,513):
#            featureName = 'f'+ str(j)
#            print(featureName)
#            intA = searchedResultA[featureName].values[0]
#            intB = searchedResultB[featureName].values[0]
#           # print(intA)
#           # print(intB)
#            featureDataA[j][i] = intA  ;
#            featureDataB[j][i] = intB  ;
#            featureDataSubtract[j][i] = abs(intA-intB) 
#            featuresA.append(intA)
#            featuresB.append(intB)
    samepairDataset = pd.read_csv('GSC-Features-Data/diffn_pairs.csv')
    img_id_A   = samepairDataset['img_id_A'].values
    img_id_B = samepairDataset['img_id_B'].values
    target = samepairDataset['target'].values
    for i in range(a,b):
        imageA = img_id_A[i]
        imageB = img_id_B[i]
        searchedResultA = featureDataSet[featureDataSet['img_id'] == imageA]
        searchedResultB = featureDataSet[featureDataSet['img_id'] == imageB]
#        print(imageA)
#        print(imageB)
        imageAData.append(imageA)
        imageBData.append(imageB)
        targetData.append(target[i])
        
        for j in range(1,513):
            featureName = 'f'+ str(j)
            print(featureName)
            intA = searchedResultA[featureName].values[0]
            intB = searchedResultB[featureName].values[0]
           # print(intA)
           # print(intB)
            featureDataA[j][i] = intA  ;
            featureDataB[j][i] = intB  ;
            featureDataSubtract[j][i] = abs(intA-intB) 
   
    
    outPutDatasetSubtract["img_id_A"]= imageAData
    outPutDatasetSubtract["img_id_B"]= imageBData
    for j in range(1,513):
        outPutDatasetSubtract['f'+ str(j)] =  featureDataSubtract[j]
    outPutDatasetSubtract["target"]= targetData 
        
    outPutDatasetConcat["img_id_A"]= imageAData
    outPutDatasetConcat["img_id_B"]= imageBData
    for j in range(1,513):
        outPutDatasetConcat['fA'+ str(j)] =  featureDataA[j]
    for j in range(1,513):
        outPutDatasetConcat['fB'+ str(j)] =  featureDataB[j]  
    outPutDatasetConcat["target"]= targetData 
    pd.DataFrame(outPutDatasetSubtract).to_csv("GSC_Subtract_diff.csv")
    pd.DataFrame(outPutDatasetConcat).to_csv("GSC_Concat_diff.csv")


# In[9]:


#createHDataCSV('CustomTarget.csv')
createGSCDataCSV('CustomTarget.csv')

