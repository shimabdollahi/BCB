# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:21:34 2019

@author: Shima Abdollahi
"""
directory="C:/Users/BCB_USER2/Desktop/Python/motif project datas/"
import pandas as pd

def writeDFtoCSV(df,path):
    df.to_csv(path)
    return

def readCSVtoDF(path):
    return pd.read_csv(path)

def readTSVtoDF(path):
    return pd.read_csv(path,sep='\t')