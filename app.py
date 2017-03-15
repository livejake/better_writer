from flask import Flask
from flask import request
from gensim.parsing.preprocessing import preprocess_string
from gensim import corpora,models, similarities
import gensim
import urllib
from textstat.textstat import textstat
app = Flask(__name__)

def classify_text(text):
  # load dictionary 
  # load model
  text=urllib.unquote(urllib.unquote(text))
  text_names =['Pride and Prejudice',
  'Adventures of Huckleberry Finn',
  "Alice's Adventures in Wonderland",
  "Moby Dick", "A Tale of Two Cities",
  "Grimms' Fairy Tales"]
  corpus = gensim.corpora.MmCorpus('./NLP Project/gutenberg.mm')
  dictionary=gensim.corpora.Dictionary.load('./NLP Project/gutenberg.dict')
  lsi = models.LsiModel(corpus)
  print lsi.show_topics()
  lsi= gensim.models.LsiModel.load('./NLP Project/gutenberg.model')
  index = similarities.MatrixSimilarity(lsi[corpus])
  index.load("./NLP Project/gutenberg.index")
  vec_bow = dictionary.doc2bow(preprocess_string(text))
  vec_lsi = lsi[vec_bow] 
  sims = index[vec_lsi]
  return sorted(zip(text_names,sims),key=lambda x: x[1],reverse=True)


def query(doc):
    vec_bow = dictionary.doc2bow(preprocess_string(doc))
    vec_lsi = lsi[vec_bow] 
    return vec_lsi

# https://github.com/coding-robots/goiwl
@app.route("/")
def hello():
    html ="""
    <html> 
  <form action="/api"  method="get">
  <textarea name="textbox" cols="40" rows="5"></textarea>
  <input type="submit" value="Submit">

  </form>

    </html>

    """
    return html


@app.route("/api/<string:text>",methods=['GET','POST'])
def analyze(text):
     analyis_str="""
     Flesch Reading:{} <br/>
     Smog Index: {} <br/>
     Flesch Kincaid: {} <br/>
     Coleman Liau Index:{} <br/>
     Automated Readability: {} <br/>
     Dale Chall Readability:{} <br/>
     Difficult Words:{} <br/>
     Linsear Write Formula: {} <br/>
     Gunning Fog: {} <br/>
     Text Standard:{},<br/>
     Similar Authors: {}
     """.format(textstat.flesch_reading_ease(text),
      textstat.smog_index(text),
      textstat.flesch_kincaid_grade(text),
      textstat.coleman_liau_index(text),
      textstat.automated_readability_index(text),
      textstat.dale_chall_readability_score(text),
      textstat.difficult_words(text),
      textstat.linsear_write_formula(text),
      textstat.gunning_fog(text),
      textstat.text_standard(text),
      classify_text(text)
      )
     return analyis_str


if __name__ == "__main__":
    app.run(debug=True)
