# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 17:37:24 2021

@author: Shima Abdollahi
"""
import pandas as pd
#in each tissue,group genes by their value,so we have a matrix of arrays(group members)
#threshold=max of input matrix /2
DF=
def maxOfdf(df): #to get maxof a pandas dataframe
    columns=df.columns
    MAX=0
    for col in columns:
        Max=df[col].max()
        if(Max>MAX):
            MAX=Max
    return MAX
###############################################################################
def breakTissueIn2Groups(tissue_name,break_value):
    global DF
    group1=[]
    group2=[]
    gene_ids=DF.index
    for gene_id in gene_ids:
        if(DF[gene_id][tissue_name] <= break_value):
            group1.append(gene_id)
        else:
            group2.append(gene_id)
    return [group1,group2]
###############################################################################
def breakMatrixIn2Groups(reference_df_matrix):
    break_value=maxOfdf(reference_df_matrix)/2  #"""اصلاح شود"""
    
    df=pd.DataFrame()
    tissues=reference_df_matrix.columns
    for tissue in tissues:
        df[tissue]=breakTissueIn2Groups(tissue,break_value)
    #get intersects:

"""
name=['shima','aida','mahtab']
age=[26,25,24]
family=['ab','fd','kv']
dic1={'name':name,'age':age,'family':family}
df1=pd.DataFrame(dic1)
dic2={'name':name,'family':family,'age':age}
df2=pd.DataFrame(dic2)
df=df1.append(df2)
dic3={'name':name,'age':age}
df3=pd.DataFrame(dic3)
df=df1.append(df3)
dft=df.T
"""











    
for i in range(1000000000000):
    print(i)
print("finished!")    
