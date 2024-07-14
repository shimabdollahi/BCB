# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 23:02:00 2020

@author: Shima Abdollahi
"""
#limitor is a gene that limits a genes group
import gffutils
#to import the gtf file to a data base
db=gffutils.create_db("D:\\BCB\\motif project datas\\New folder\\Homo_sapiens.GRCh38.97.gtf","Homo_sapiens.GRCh38.97.db")

###############################################################################

def getAllGenes():
    #make a list consist of all genes name using correlationTable
    return #list

def initIsLimitor():
    genes=getAllGenes()
    #make a list wich can be indexed by gene name and init all values to false
    return #list

###############################################################################

def recursivegrouping(genes):
    if(allGenesAreLimitor(genes)):
        return
    else:
        for gene in genes :
            if(not isLimitor[gene]):
                limitor=gene
                isLimitor[gene]=True
                return recursivegrouping(limit(genes,limitor))
                isLimitor[gene]=False
        return
    
###############################################################################

def allGenesAreLimitor(genes):
    for gene in genes:
        if(not isLimitor[gene]):
            return False
    return True

###############################################################################

def limit(genes,limitor):
    for gene in genes:
        if(correlation(gene,limitor)< TRESHOLD):
            genes.remove(gene)
    return genes

###############################################################################