# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:53:32 2019

@author: Shima Abdollahi
"""

import pandas as pd
import geneAddressDataBase as GADB
import DNAsequencesDB as DNAdb
import RWfasta as fa
#####################################################################################
def setAndAddArea(before,after,gene_df):
    gene_id=gene_df.gene_id
    gene_name=gene_df.gene_name
    strand=gene_df.strand
    seqname=gene_df.seqname
    start=gene_df.start
    end=gene_df.end
    
    gene_address_data={'gene_id':gene_id,'gene_name':gene_name,'strand':strand,'seqname':seqname,'start':start,'end':end}
    gene_addresses=pd.DataFrame(gene_address_data)
    
    # filter DataFrame on positive strands:
    df_sense = gene_addresses[gene_addresses["strand"] == "+"]
    # filter DataFrame on negetive strands:
    df_inverse = gene_addresses[gene_addresses["strand"] == "-"]
    
    df_sense['beforeTSS']=df_sense['start']-before
    df_sense['afterTSS']=df_sense['start']+after
    df_inverse['afterTSS']=df_inverse['end']+before
    df_inverse['beforeTSS']=df_inverse['end']-after
    
    dfs=[df_sense,df_inverse]
    gene_addresses=pd.concat(dfs)
    return gene_addresses
#####################################################################################
def getPromoterSeq(gene_id,DB):
    seqname=GADB.seqname(gene_id,DB)
    Chr=DNAdb.getChrSeq("chr"+seqname)
    return Chr[GADB.startOfPromoter(gene_id,DB)-1:GADB.endOfPromoter(gene_id,DB)]
#####################################################################################
def fastaContent(gene_id,DB):
    seq=getPromoterSeq(gene_id,DB) #without newline characters!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    fasta_content=">"+gene_id+"\n"+seq+"\n"
    return fasta_content
##################################################################################### 

def getPromoters(gene_ids,group_name,DB): #gene_ids is a list of gene_id s as string
    fasta_content=""
    for gene_id in gene_ids:
        if(gene_id not in ['ENSG00000221870','ENSG00000204293','ENSG00000196661','ENSG00000279132','ENSG00000237847','ENSG00000273547','ENSG00000221961','ENSG00000278566']):
            fasta_content+=fastaContent(gene_id,DB)
    #fa.writefile(fasta_content,group_name)
    return fasta_content
#####################################################################################    