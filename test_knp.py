#!/usr/bin/env python3
from pyknp import KNP
import csv

knp = KNP()  
result = knp.parse("独自ブランドであるカジュアルブランドのユニクロを創り上げ、急成⻑を遂げました")
title = [['キーワード','原形','品詞','品詞細分類']]
top_list=[]
every_row = result.mrph_list()
for i in every_row:
    top_list.append([i.midasi,i.genkei,i.hinsi,i.bunrui])
    # print(i.midasi,i.genkei,i.hinsi, i.bunrui,sep='\t')
with open(r'/opt/knp.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(title)
    writer.writerows(top_list)
