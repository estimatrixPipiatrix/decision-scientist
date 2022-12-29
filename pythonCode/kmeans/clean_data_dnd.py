import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer

data = pd.read_json('srd_5e_monsters.json')
data['monster num'] = data.index
rows_to_keep = pd.read_csv('rows_to_keep.csv')
data = data.iloc[rows_to_keep['keep']]
data = data.dropna(axis=1).reset_index(drop=True)

data = data.drop('img_url',axis=1)
for i in range(data.shape[0]):
    data.loc[i,'Hit Points'] =int(re.search(r"(\d+)", \
                              data.loc[i]['Hit Points']).group())
    data.loc[i,'Challenge']  =int(re.search(r"(\d+)", \
                              data.loc[i]['Challenge']).group())
    data.loc[i,'Armor Class']=int(re.search(r"(\d+)", \
                              data.loc[i]['Armor Class']).group())
    data.loc[i,'Speed']      =int(re.search(r"(\d+)", \
                              data.loc[i]['Speed']).group())
    data.loc[i,'STR_mod']    =int(re.search(r"(\d+)", \
                              data.loc[i]['STR_mod']).group())
    data.loc[i,'DEX_mod']    =int(re.search(r"(\d+)", \
                              data.loc[i]['DEX_mod']).group())
    data.loc[i,'CON_mod']    =int(re.search(r"(\d+)", \
                              data.loc[i]['CON_mod']).group())
    data.loc[i,'CHA_mod']    =int(re.search(r"(\d+)", \
                              data.loc[i]['CHA_mod']).group())
    data.loc[i,'INT_mod']    =int(re.search(r"(\d+)", \
                              data.loc[i]['INT_mod']).group())
    data.loc[i,'WIS_mod']    =int(re.search(r"(\d+)", \
                              data.loc[i]['WIS_mod']).group())

vec = CountVectorizer()
langs = vec.fit_transform(data['Languages'])
langs = pd.DataFrame(langs.toarray(), \
                     columns=vec.get_feature_names_out())
data = data.drop(['Languages'],axis=1)

meta = vec.fit_transform(data['meta'])
meta = pd.DataFrame(meta.toarray(), \
                    columns=vec.get_feature_names_out())
data = data.drop(['meta'],axis=1)

senses = vec.fit_transform(data['Senses'])
senses = pd.DataFrame(senses.toarray(), \
                      columns=vec.get_feature_names_out())
data = data.drop(['Senses'],axis=1)

data = pd.concat((data,langs,meta,senses),axis=1)

data.to_csv('monsters_cleaned.csv',index=False)
