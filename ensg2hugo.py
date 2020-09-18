#!/usr/bin/python
import os
import sys
import numpy as np
import pandas as pd
import fileinput
import re

dictgene = {}
for each_line_of_text in fileinput.input('Homo_sapiens.GRCh37.75.gtf'):
    if each_line_of_text.startswith("#"):
        continue
    splitcolumn_array = re.split(r'[;,\t,\"]',each_line_of_text)
    ENSG = splitcolumn_array[9]
    id_geneName = splitcolumn_array.index(' gene_name ') + 1
    geneName = splitcolumn_array[id_geneName]
    dictgene[ENSG] = geneName

if sys.argv[1][:2] == '-f':
    col_num = int(sys.argv[1][2:])-1
    ensg_file = sys.argv[2]
        
else:
    col_num = 0
    ensg_file = sys.argv[1]
    
expres = pd.read_csv(ensg_file)
if expres.columns[col_num] != 'gene_id':
    expres.rename( columns = { expres.columns[col_num]: 'gene_id' }, inplace = True )

expres['gene_id'] = expres['gene_id'].map(lambda x: (str) (x)[:15])
expres['gene_id'] = expres['gene_id'].map(dictgene)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)
print(expres)
