# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 12:07:27 2016

@author: fang2
"""
#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline,FeatureUnion
from sklearn.cross_validation import StratifiedKFold
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import confusion_matrix
from sklearn.feature_selection import RFE
from sklearn.feature_selection import SelectKBest,SelectPercentile
from sklearn.feature_selection import f_classif
from sklearn.decomposition import PCA
#from sklearn.linear_model import RandomizedLasso
from sklearn.svm import LinearSVC,SVC
from sklearn.grid_search import GridSearchCV
"""
get clinical information and count number of M0 and M1
"""

def get_Metastasis(sampleID_list,df_clinical):
    num_M0=0
    num_M1=0
    list_Metastasis=[]
    list_Metastasis.append('Metastasis')

    for ID in sampleID_list:
        row_number=df_clinical.loc[df_clinical.sampleID==ID].index[0]
        list_Metastasis.append(df_clinical.loc[row_number,'pathologic_M'])
        
    for i in range(1,len(list_Metastasis)):
        if list_Metastasis[i]!="M0" and isinstance(list_Metastasis[i],str):
            list_Metastasis[i]="M1"
            num_M1+=1
            list_Metastasis[i]=1
        elif list_Metastasis[i]=="M0":
            num_M0+=1
            list_Metastasis[i]=0
#        else:
#            list_Metastasis[i]=None
            
    return list_Metastasis, num_M1, num_M0  
            
def get_columnIncludeNan(list_M):

    column_should_drop=[]
    list_M1=[]

    for i in range(len(list_M)):
        if isinstance(list_M[i],int):
            list_M1.append(list_M[i])
        else:
            column_should_drop.append(i)
            
    return column_should_drop, list_M1

def mergeFeature(feature_selected, feature_weight):
    result=dict()
    length=len(feature_selected[0])
    for key in feature_selected.keys():
        feature_selected[key].shape=(1,length)
    for key in feature_selected.keys():
        temp=[]
        for i in range(length):
            temp.append([feature_selected[key][0][i],feature_weight[key][0][i]])
        result[key]=temp
    return result



"""
read Data
"""

path_for_clinical_data="clinical_data"                            
path_for_genomicMatrix="genomicMatrix"
df_clinical = pd.read_table(path_for_clinical_data)
df_genomicMatrix = pd.read_table(path_for_genomicMatrix)
    ##get rid of row include nan
    
  
"""
Add metastasis information
"""
sampleID_list=list(df_genomicMatrix.columns.values)
sampleID_list=sampleID_list[1:]
list_M=[]

list_M,num_M1,num_M0=get_Metastasis(sampleID_list,df_clinical)
column_should_drop,list_M1=get_columnIncludeNan(list_M[1:])
df_genomicMatrix=df_genomicMatrix.dropna(axis=0)
df_genomicMatrix=df_genomicMatrix.drop(df_genomicMatrix.columns[column_should_drop],axis=1)  

X=df_genomicMatrix.iloc[1:len(df_genomicMatrix),1:].values.T
y=list_M1
le=LabelEncoder()
y=le.fit_transform(y)
#y=label_binarize(y,classes=[0,1])


X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.3,random_state=0)


#"""
#pipeline1:choose parameter
#"""
#normalization=StandardScaler()
##svc=SVC(kernel='linear')
#feature_selection=SelectPercentile(f_classif,percentile=10)
#parameters_for_svm={'kernel':('linear','rbf','sigmoid'),'C':[1,10,100]}
#            
#svr=SVC(cache_size=800)
#clf=GridSearchCV(svr,parameters_for_svm)
#pipe_lr=Pipeline([("normalization",normalization),
#                 ("feature_selection",feature_selection),
#                ("clf",clf)])
#pipe_lr.fit(X_train,y_train)
#score=pipe_lr.score(X_test,y_test)            
"""
kfold test
"""
normalization=StandardScaler()
feature_selection=SelectPercentile(f_classif,percentile=10)
classify=SVC(C=1,cache_size=800,kernel='linear')
pipeline=Pipeline([("normalization",normalization),
                   ("feature_selecation",feature_selection),
                   ("classify",classify)])                
kfold=StratifiedKFold(y=y_train,n_folds=10,random_state=1)
scores=[]
fpr=dict()
tpr=dict()
feature_selected=dict()
support_vector=dict()
roc_auc=dict()
for k,(train,test) in enumerate(kfold):
    
    pipeline.fit(X_train[train],y_train[train])
    score=pipeline.score(X_train[test],y_train[test])
    y_pred=pipeline.predict(X_test)
    y_score=pipeline.decision_function(X_test)
    confmat=confusion_matrix(y_true=y_test, y_pred=y_pred)
    fpr[k], tpr[k], thresholds=roc_curve(y_true=y_test,y_score=y_score)
    feature_selected[k]=pipeline.named_steps['feature_selecation'].get_support(indices=True)
    roc_auc[k]=auc(fpr[k],tpr[k])
    support_vector[k]=pipeline.named_steps['classify'].coef_
    scores.append(score)
    print('Fold: %s, class dist.: %s,Acc:%.3f'%(k+1,np.bincount(y_train[train]),score))

#%%
plt.figure()
lw = 2
plt.plot(fpr[0], tpr[0], color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc[9])
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()
#%%
merged_feature=mergeFeature(feature_selected,support_vector)


#%%