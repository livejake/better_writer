import React from "react"
 

const Technical = () => (
  <div>
<p>
The essay grader uses the XGBoost model trained on 587 features to grade essays.
 The essay training data and topics come from <a href="https://www.kaggle.com/c/asap-aes">The Hewlett Foundation: Automated Essay Scoring competition</a>. 
 Meaning Cloud API is used to classify the topic of the essay. 
 An LSA model is used to identify the similarity to a book. 
 </p>
  </div>
)

export default Technical