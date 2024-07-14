# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:03:07 2019

@author: Shima Abdollahi
"""
import RWfasta as  fa
def getChrSeq(seqname):
    seq=fa.readContent(seqname).upper()
    return arrangeSeq(seq)

def arrangeSeq(seq):
    arranged=''
    while (len(seq)>0):
        if(len(seq)>=100001):
            arranged+=seq[0:100001]+'\n'
            seq=seq[100001:]
        else:
            arranged+=seq
            seq=''
    return arranged