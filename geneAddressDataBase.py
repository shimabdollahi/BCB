# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 17:22:49 2019

@author: Shima Abdollahi
"""
import pandas as pd
#DB=pd.DataFrame({}) #or read from wroten tabulated file
directory="C:/Users/BCB_USER2/Desktop/Python/motif project datas/"
def loadDB(dbName):
    return pd.read_csv(directory+dbName+".csv") #load data base

def startOfPromoter(gene_id,DB):
    return DB.loc[gene_id,'beforeTSS']
def endOfPromoter(gene_id,DB):
    return DB.loc[gene_id,'afterTSS']
def seqname(gene_id,DB):
    return DB.loc[gene_id,'seqname']
def strand(gene_id,DB):
    return DB.loc[gene_id,'strand']