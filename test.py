from collections import deque,defaultdict
from collections import Counter
import re
from itertools import islice
from gensim.parsing.preprocessing import *
from nltk.tokenize import word_tokenize,sent_tokenize

# PunktSentenceTokenizer
# PunktWordTokenizer

from gutenberg.cleanup import strip_headers
import requests
# http://nbviewer.jupyter.org/github/rare-technologies/gensim/blob/develop/docs/notebooks/atmodel_tutorial.ipynb

def load_etext(num):
  url ='http://www.gutenberg.org/files/{0}/{0}-0.txt'.format(num)
  data= requests.get(url)
  return data.text

texts =[]
text_nums=[1342,76,11,2701,98,2591]
text_names =['Pride and Prejudice','Adventures of Huckleberry Finn',"Alice’s Adventures in Wonderland",
            "Moby Dick", "A Tale of Two Cities","Grimms’ Fairy Tales"]
for text_num in text_nums:
    text = strip_headers(load_etext(text_num))
    texts.append(text)

paragraph_regex = re.compile("\\n\\s*\\n")
all_paragraphs=re.split(paragraph_regex, texts[0])
all_paragraphs=filter(lambda x: len(x)>0, all_paragraphs)
# paragraph_lengths=map(lambda x: len(x), all_paragraphs)
# print reduce(lambda x, y: x + y, paragraph_lengths) / len(paragraph_lengths)

# 
# https://github.com/Kapiche/caterpillar/blob/master/caterpillar/processing/analysis/tokenize.py

# DEFAULT_FILTERS = [lambda x: x.lower(), strip_tags, strip_multiple_whitespaces]
# text=preprocess_string(texts[0],filters=DEFAULT_FILTERS)

paragraph_lengths=[]
for paragraph in all_paragraphs: 
  paragraph_lengths.append(len(paragraph))

  # paragraph length
  # similarity to previous paragraphs
  # num words 

words = word_tokenize(text)
last_four_words =deque([])
word_counter = defaultdict(int)
two_gram_counter = defaultdict(int)
three_gram_counter = defaultdict(int)
four_gram_counter = defaultdict(int)

def slice(n,words):
  n_gram = list(islice(words, n, 4))
  return " ".join(n_gram)

for word in words:
  word_counter[word]+=1
  last_four_words.append(word)
  # N grams 
  if len(last_four_words)>4:
    last_four_words.popleft()
    four_gram_counter[slice(0,last_four_words)] +=1 
  if len(last_four_words)>=2:
    two_gram_counter[slice(2,last_four_words)] +=1
  if len(last_four_words)>=3:
    three_gram_counter[slice(1,last_four_words)] +=1


Counter(four_gram_counter).most_common()[0:5]
Counter(three_gram_counter).most_common()[0:5]
Counter(two_gram_counter).most_common()[0:5]