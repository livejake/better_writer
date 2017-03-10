from flask import Flask
from flask import request
from textstat.textstat import textstat
app = Flask(__name__)

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
     Coleman Liau Index:{} <br/>
     Automated Readability: {} <br/>
     Dale Chall Readability:{} <br/>
     Difficult Words:{} <br/>
     Linsear Write Formula: {} <br/>
     Gunning Fog: {} <br/>
     Text Standard:{}
     """.format(textstat.flesch_reading_ease(text),
      textstat.smog_index(text),
      textstat.flesch_kincaid_grade(text),
      textstat.coleman_liau_index(text),
      textstat.automated_readability_index(text),
      textstat.dale_chall_readability_score(text),
      textstat.difficult_words(text),
      textstat.linsear_write_formula(text),
      textstat.gunning_fog(text),
      textstat.text_standard(text)
      )
     return analyis_str


if __name__ == "__main__":
    app.run(debug=True)
