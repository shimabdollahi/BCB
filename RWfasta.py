# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:46:46 2019
 
@author: Shima Abdollahi
"""
#use case:	to read & write fasta files
directory="D:/BCB/motif project datas/"
def readContent(filename): #read contents of a fasta file 
    filename+=".fa"
    filename=directory+filename
    my_file = open(filename)
    return my_file.read()

def readSingle(filename): #get name & sequence for a single sequence
    file_content=readContent(filename)
    return getNameandSeq(file_content)
    
def readMultiple(filename): #in case file contains multiple sequences
    file_content=readContent(filename)
    list_of_contents=seprateDNAs(file_content)
    list_of_contents.remove("")
    sequences=[]
    for content in list_of_contents:
        sequences+=[getNameandSeq(content)]
    return sequences
    
def seprateDNAs(contents): #to separate single sequences in a multiple sequence content
    return contents.split('>')
    
        
def getNameandSeq(content): #get name of the sequence and the sequence
    arr=content.split('\n',1)
    name=arr[0]
    seq=arr[1]
    seq=seq.replace("\n","") #string.replace(old, new, count)  to delete \n characters in the sequence
    return [name,seq] 

def write(seqnameBasedsequences):
    for seq in seqnameBasedsequences:
        file = open(directory+seq[0]+".fa", "w")
        file.write(seq[1])
        file.close
    return
def appendfile(file_name,content):
    file=open(directory+file_name+".fa", "a")
    file.write(content)
    file.close
    return
def writefile(content,file_name):
    file=open(directory+file_name+".fa", "w")
    file.write(content)
    file.close
    return
def writefileTopath(content,file_name,path):
    file=open(path+file_name+".fa", "w")
    file.write(content)
    file.close
    return