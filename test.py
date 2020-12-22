import csv
from pykakasi import kakasi
import codecs
import pandas as pd
kakasi = kakasi()
kakasi.setMode('H', 'a')
kakasi.setMode('K', 'a')
kakasi.setMode('J', 'a')
kakasi.setMode("s", True) #wakati

conv = kakasi.getConverter()

row_data = pd.read_csv('input_a.csv',encoding="utf-8",header=0)
df = pd.DataFrame(row_data,columns=['origin'])
input_list = df.values.tolist()
converted_list = list()
m_list = list()
s_list = list()
hb_list = list()
w_list = list()
score = list()


for input_item in input_list:
    for string in input_item:
        converted_list.append(conv.do(string))

for word in converted_list:
    m_list.append(word.count('m'))
    s_list.append(word.count('s')-word.count('tsu'))
    hb_list.append(word.count('h')+word.count('b')-word.count('shi'))
    w_list.append(word.count('w'))

for i in range(len(converted_list)):
    score.append([m_list[i]+s_list[i]+hb_list[i]+w_list[i],i])

top10_index = sorted(score)[-10:]
print(top10_index)
top10_list = list()
for i in range(9,0,-1):
    top10_list.append(input_list[top10_index[i][1]])
print(top10_list)

top10_df =pd.DataFrame({    'origin':top10_list,})

output_df = pd.DataFrame({  '原文（日本語）':input_list,
                            '変換後（ローマ字）':converted_list,
                            'm':m_list,
                            's':s_list,
                            'hb':hb_list,
                            'w':w_list,})

#print(output_df)
output_df.to_csv("output.csv")

