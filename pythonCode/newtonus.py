from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
import torch

# extract the text from the website
url = "https://la.wikipedia.org/wiki/Isaacus_Newtonus"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

for script in soup(["script", "style"]):
    script.extract()    # rip it out

text = soup.get_text()

lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk)

# clean the text to prepare for one-hot coding
text = text.lower()
stop_symbols = '[].,;:"!?_|-/↑&`'
stop_words = ['university','is','of','and','the','i','a', \
              'newton\'s','press','isbn','newton','s',    \
              'cambridge']
word_list = text.replace('\n',' ').split()
word_list = [word.strip(stop_symbols) for word in word_list]

resultwords  = [word for word in word_list if word not in stop_words]
result = ' '.join(resultwords)
word_list = result.split()

# create encoding 
word2index_dict = {word: i for (i,word) in enumerate(word_list)}
# dictionary needs to be re-indexed so that the highest
# index is not larger than len(word2index_dict)
word2index_dict2 = {list(word2index_dict)[i]:i \
                    for i in range(len(word2index_dict))}

word_t = torch.zeros(len(word_list),len(word2index_dict2))
for i, word in enumerate(word_list):
    word_index = word2index_dict2[word]
    word_t[i][word_index] = 1

# create an array with the sums of all columns
word_counts = torch.tensor([word_t[:,i].sum() \
              for i in range(word_t.shape[1])])
word_counts = word_counts.numpy()

# get the top 10 words
ind = np.argpartition(word_counts, -10)[-10:]
print([list(word2index_dict2)[i] for i in ind])
