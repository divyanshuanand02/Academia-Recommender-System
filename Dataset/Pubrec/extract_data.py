# -*- coding: utf-8 -*-
"""pubrec-extract-data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OtretFxRQCqfIsYoGr_N_kW84M-eojCi
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/My\ Drive/pub-rec-data

import numpy as np
import pandas as pd
import pickle as p

f = open("./AMiner-Paper.txt", "r")
data=[]
for x in f:
  data=f.readlines()

data_i=[]
temp=[]
for string in data:
    if string != '\n':
        temp.append(string)
    else:
        data_i.append(temp)
        temp=[]

processed_data=[]
for dp in data_i:
    for string in dp:
        if(string[:2]=='#!'):
            processed_data.append(dp)

len(processed_data)

abs_list=[]
pv_list=[]
author_list=[]
title_list=[]
for dp in processed_data:
    for string in dp:
        if(string[:2]=='#c'):
            pv_list.append(string[3:].strip('\n'))
        if(string[:2]=='#!'):
            abs_list.append(string[3:].strip('\n'))
        if(string[:2]=='#*'):
            title_list.append(string[3:].strip('\n'))
        if(string[:2]=='#@'):
            author_list.append(' ; '.join(string[3:].strip('\n').split(";")))

all_data = pd.DataFrame(data={'abstract': abs_list, 'pv': pv_list, 'authors': author_list, 'title': title_list})

filtered = all_data.groupby('pv').filter(lambda x: len(x) >= 500)

all_data=filtered.copy()

data_points=len(all_data)

np.random.seed(42)
shuffled = all_data.iloc[np.random.permutation(data_points), :]

train_data=shuffled[:int(data_points*0.8)]
val_data=shuffled[int(data_points*0.8):int(data_points*0.9)]
test_data=shuffled[int(data_points*0.9):]

p.dump(train_data['abstract'].tolist(),open('./abstract_train.p', mode='wb'))
p.dump(val_data['abstract'].tolist(),open('./abstract_val.p', mode='wb'))
p.dump(test_data['abstract'].tolist(),open('./abstract_test.p', mode='wb'))
p.dump(train_data['pv'].tolist(),open('./pv_train.p', mode='wb'))
p.dump(val_data['pv'].tolist(),open('./pv_val.p', mode='wb'))
p.dump(test_data['pv'].tolist(),open('./pv_test.p', mode='wb'))
p.dump(train_data['authors'].tolist(),open('./authors_train.p', mode='wb'))
p.dump(val_data['authors'].tolist(),open('./authors_val.p', mode='wb'))
p.dump(test_data['authors'].tolist(),open('./authors_test.p', mode='wb'))
p.dump(train_data['title'].tolist(),open('./title_train.p', mode='wb'))
p.dump(val_data['title'].tolist(),open('./title_val.p', mode='wb'))
p.dump(test_data['title'].tolist(),open('./title_test.p', mode='wb'))

len(train_data['pv'].unique())
