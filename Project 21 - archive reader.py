#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:28:49 2018

@author: caser
"""
#1 import libraries
import numpy as np
import pandas as pd
import os

pathname="/media/caser/Music/60 classical"

#3 Generate the file details in dataframe 
df = pd.DataFrame(columns=['Filelist','Directory','Filename','Filesize','Extension','ending'])

for root, dirs, files in os.walk(pathname):
    for name in files:
      flnm=os.path.join(root, name)
      flsz=os.path.getsize(flnm)
      extn=os.path.splitext(name)[1].lower()
      ending=os.path.splitext(name)[1][-1:]
      df_=pd.DataFrame({'Filelist': [flnm],'Directory':[root],'Filename':[name], 'Filesize': [flsz],'Extension':[extn],'ending':ending})
      df=df.append(df_, ignore_index=1)
   
    
#4 Covert the size to M.bytes
clmn1=np.divide(df['Filesize'],10.0**6)
df['Filesize']=clmn1

#5 Check if last word is blank
blanks=df[(df['ending']=='')]

#6 Check file type and filesize>1mb delete file 
not_mp3=df[(df['Extension']!='.mp3') & (df['Extension']!='.wma') & (df['Filesize']>=1)]

#7 export the list
writer = pd.ExcelWriter(str(pathname.split('/')[-1]+'.xlsx'))
df.to_excel(writer,'list', float_format='%.1f')
blanks.to_excel(writer,'blanks', float_format='%.1f')
not_mp3.to_excel(writer,'not_mp3', float_format='%.1f')
writer.save()


#
##8 delete big files
#for i in range(not_mp3['Filelist'].count()):
#    os.remove(not_mp3.iloc[i,2])


##sort by size
#not_mp3=not_mp3.sort_values(by=['Filesize'], axis=0, ascending=0,  na_position='first')