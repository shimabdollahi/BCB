# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:48:24 2019

@author: Shima Abdollahi
"""
directory="C:/Users/BCB_USER2/Desktop/Python/motif project datas/"

import gtfparse
from gtfparse import read_gtf
import pandas as pd

def read(file_name):
    return read_gtf(directory+file_name+".gtf")

def write(data_frame,file_name):
    return
    

def filterByGene(df):
    df_genes = df[df["feature"] == "gene"]
    return df_genes