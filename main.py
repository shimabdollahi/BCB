# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:49:54 2019

@author: Shima Abdollahi
"""
import RWgtf as gtf
import Promoter as P
#import seqFinder as SF
import CoExpression as CE
import geneAddressDataBase as GADB
import RWcsv as csv
import RWfasta as fa
import pandas as pd
import expressionDB as e

GENE_INFO_DB=pd.DataFrame()

BAMMinputPATH='D:/BCB/BAMM_inputs/'
###############################################################################
def loadGeneInfoDB():
    global GENE_INFO_DB
    GENE_INFO_DB=pd.read_csv("D:/BCB/motif project datas/geneAddress-promoterAddress-gene_name-strand-seqname.csv") 
    GENE_INFO_DB=GENE_INFO_DB.set_index("gene_id") 
    return
"""
def prepareBAMMinputs(groups,path):
    for i in range(len(groups)):
        group_name='Group '+str(i)       
        fa.writefileTopath( P.getPromoters(groups[i],group_name,GENE_INFO_DB),group_name,path)
    return
"""
def prepareBAMMinputs(groups,path):
    for i in [1] :
        group_name='Group '+str(i)       
        fa.writefileTopath( P.getPromoters(groups[i],group_name,GENE_INFO_DB),group_name,path)
    return
###############################################################################
"""

#set gene address table for once
#gene_df=gtf.filterByGene(gtf.read("Homo_sapiens.GRCh38.92")) #Done
#assign gene_ids to row names:
#gene_df=gtf.read("Homo_sapiens.GRCh38.92")
#justGeneGTF=gene_df.set_index("gene_id",drop=False) #Done

justGeneGTF=pd.read_csv("C:/Users/BCB_USER2/Desktop/Python/motif project datas/Homo_sapiens.GRCh38.92-justGene.csv")
#write gene_df to a csv file:
csv.writeDFtoCSV(gene_df,"Homo_sapiens.GRCh38.92-justGene") #Done

#add promoter address for once or anytime i want
DB=P.setAndAddArea(3000,500,justGeneGTF) #Done
#write gene addresse table to a csv file
csv.writeDFtoCSV(DB,"geneAddress-promoterAddress-gene_name-strand-seqname") #Done
#read human genome database for once
#DNAs=fa.readMultiple("hg38") #Done
#write separate fasta files based on different seqnames
#fa.write(DNAs) #Done

"""

#clustering genes based on expressions



#load Data Base:
#DB=GADB.loadDB("Homo_sapiens.GRCh38.92-geneAddress-promoterAddress-gene_name-strand-seqname")
loadGeneInfoDB()
#have a list of coexpression genes
#gene_list=CE.getGroup(factor) #give a factor
#give the gene lists to module seqfinder
#for gene in gene_list:
 #   start=GADB.startOfPromoter(gen,DB)
  #  end=GADB.endOfPromoter(gen,DB)
   # seqname=GADB.seqname(gen,DB)
    #strand=GADB.strand(gen,DB)
    #promoter=SF.getSeq(seqname,start,end,strand) 
#prepare input files for BAMMmotif processing
prepareBAMMinputs(e.GROUPS,BAMMinputPATH)
#P.getPromoters(["ENSG00000243485","ENSG00000279928","ENSG00000237973","ENSG00000229905","ENSG00000267857","ENSG00000171189","ENSG00000258301","ENSG00000232581","ENSG00000155026","ENSG00000277463"],"shimaGroup",DB)
   
#give the file to bammotif server,get results from bamserver as a file(pdf?)



'''

def readTSVtoDF(path):
    return pd.read_csv(path,sep='\t')

rna_tissue=readTSVtoDF('D:/BCB/expression/rna_tissue.tsv')
rna_tissue.set_index('Gene')
geneIdToName=rna_tissue[['Gene','Gene name']]
geneIdToName=geneIdToName.drop_duplicates()
geneIdToName=geneIdToName.set_index('Gene')
rna_tissue_matrix=pd.read_csv('D:/BCB/expression/rna_tissue_matrix.csv')
rna_tissue_matrix=rna_tissue_matrix.set_index('Unnamed: 0')
result=pd.concat([geneIdToName, rna_tissue_matrix], axis=1, join="inner")
result.to_csv('D:/BCB/expression/named_rna_tissue_matrix.csv')
for i in range(35):
    group=pd.read_csv('D:/BCB/expression/rna_tissue_groups/Group_'+str(i)+'.csv')
    group=group.set_index('Unnamed: 0')
    result=pd.concat([geneIdToName,group], axis=1, join="inner")
    result.to_csv('D:/BCB/expression/named_rna_tissue_groups/Group_'+str(i)+'.csv')
    
'''