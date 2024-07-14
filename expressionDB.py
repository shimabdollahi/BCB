# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:37:23 2019

@author: Shima Abdollahi
"""
import pandas as pd
from sklearn.cluster import OPTICS#, cluster_optics_dbscan
import numpy as np
import scipy.spatial.distance as ssd
#import Promoter as P
GROUPS=[]
###############################################################################
Rpath='D:/BCB/expression/rna_tissue_matrix.csv'
Wpath='D:/BCB/expression/rna_tissue_Transposed_matrix.csv'
WpathtissueCorr='D:/BCB/expression/rna_tissue_Transposed_correlation_matrix.csv'

cluster_geneId_path='D:/BCB/expression/tissue_gene_cluster_geneId.csv'
groups_path='D:/BCB/expression/rna_tissue_groups/Group_'
###############################################################################
'C:/Users/BCB_USER2/Desktop/Python/motif project datas/expression/rna_celline.tsv'
"""
def transposeMatrix(readPath,writePath):
    df=pd.read_csv(readPath) #read csv file
    #3matrix=pd.DataFrame()
    df.set_index('Unnamed: 0',inplace=True)
    #print(df)
    transposedMatrix=df.T
    transposedMatrix.to_csv(writePath)
    return transposedMatrix
    #df.loc[1,1]
#transposeMatrix(Rpath,Wpath)
"""
"""
df=pd.read_csv(Rpath)
df.index
df.columns
df.set_index('Unnamed: 0',inplace=True)
df.columns
"""
###############################################################################
def prepareDB(readPath,writePath):
    df=pd.read_csv(readPath,sep='\t') #read csv file
    majorDf=pd.DataFrame()
    while ((df.count().Gene)>0):#while df is not empty
        geneId=df.loc[0,'Gene']
        tmp=df[df['Gene']==geneId]
        tmp=tmp[['Sample','Value']]
        tmp=tmp.set_index('Sample')
        tmp=tmp.T
        tmp=tmp.rename(index={'Value':geneId})
        majorDf=majorDf.append(tmp)
        df=df[df.Gene!=geneId]
        index=list(range(df.count().Gene))
        df['index']=index
        df=df.set_index('index')
    majorDf.to_csv(writePath)
    return majorDf
###############################################################################    
def prepareCorrelation(DB,path):
    corrDB=DB.corr(method='pearson')
    corrDB.to_csv(path)
    return corrDB
###############################################################################
def runOPTICSclustering(readPath,writePath):
    #load correlation matrix to a dataframe
    df=pd.read_csv(readPath)
    df.set_index('Unnamed: 0',inplace=True)
    print(df)
   # gene_ids=pd.DataFrame()
    #gene_ids['Gene']=df.index
    #print(gene_ids)
    #convert dataframe to ndarray by df.to_numpy()
    X=df.to_numpy()
    print(X)
    print("\n\n\n")
    print(X[0])
    print(X[0][1])
    #run OPTICS clustering
    clust = OPTICS(metric= 'chebyshev',min_samples=10,max_eps=5 , xi=.005,algorithm='auto',n_jobs=-1)
   # Y = ssd.pdist(X, 'chebyshev')
 
    clust.fit(X,ssd.pdist(X, 'chebyshev'))
    #labels = clust.labels_[clust.ordering_]
    labels = clust.labels_
    print(labels)
    result=pd.DataFrame(labels,columns=['Cluster'])
    result['Gene']=df.index
    print(result)
    result.to_csv('D:/BCB/expression/tissue_gene_cluster_geneId.csv')
    #clust.ordering_
    np.savetxt(writePath, labels, delimiter=",")
   # reachability=clust.reachability_[clust.ordering_]
    return #labels
#runOPTICSclustering('D:/BCB/expression/rna_tissue_matrix.csv',"D:/BCB/expression/tissue_gene_cluster_labels.csv")    
#df=pd.read_csv('D:/BCB/expression/rna_tissue_matrix.csv')    
#prepareCorrelation(transposeMatrix(Rpath,Wpath),WpathtissueCorr)
###############################################################################
def sortGeneIdGroups(cluster_geneId_path):
    df=pd.read_csv(cluster_geneId_path)
    df=df.drop(columns=['Unnamed: 0'])
    #print(df)
    df = df[df['Cluster'] != -1]
   # num_of_clusters=df['Cluster'].max()+1
    rslt_df = df.sort_values(by = 'Cluster')
    #print(df.head(15))
    #print(df.shape)
    
    return rslt_df
#sortGeneIdGroups(cluster_geneId_path)
###############################################################################
def getGroups_geneIds_list(groups_path):
    df=sortGeneIdGroups(cluster_geneId_path) #sorted_geneId_clusters_df
    num_of_clusters=df['Cluster'].max()+1
    groups=[]
    
    rna_tissue_df=pd.read_csv('D:/BCB/expression/rna_tissue_matrix.csv')
    ##rna_tissue_df.set_index('Unnamed: 0',inplace=True)
    #print(rna_tissue_df)
    
    for i in range(num_of_clusters):
        #for each cluster get list of gene ids
        group_geneIds=df[df['Cluster'] == i ]['Gene'].to_list()
       # print(group_geneIds)
        #write a csv file based on rna tissue matrix filtered by each group gene_ids
        sub_rna=rna_tissue_df[rna_tissue_df['Unnamed: 0'].isin(group_geneIds) ]
        sub_rna.set_index('Unnamed: 0',inplace=True)
        #print(sub_rna)
        sub_rna.to_csv(groups_path+str(i)+'.csv')
        #add list of each cluster gene_ids to list of groups members
        groups.append(group_geneIds)
    #print(GROUPS)
    return groups #for iterate on P.getPromoter**************

GROUPS=getGroups_geneIds_list(groups_path)
###############################################################################

###############################################################################    
