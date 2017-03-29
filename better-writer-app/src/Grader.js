import React, { Component } from 'react';

export default function Grader(props) {
  
    const { analysisKeys, analysis } = props;

    //grade
    const grade = ['a NC. Your essay could use improvement.','an F. Your essay could use improvement.', 'a D. Your essay could use improvement.', 'a C.', 'a B. Your essay shows promise. With a little more work you could receive an A!', 'an A. Great Work!', 'an A+. Excellent Job!']
    const xg_boost = analysis.xg_boost.map(n => {
      return parseFloat(n)
    })
    const gradeIndex = xg_boost.indexOf(Math.max.apply(null, xg_boost))
    const gradePercents = xg_boost.map(n => {  
      return n * 100
    })

    const grades = ['NC','F','D','C','B','A','A+']
    //mcClass
    const mcClassListStartText = 'Your essay is about the following topics: '
    
    let mcClassList = analysis.meaning_cloud_classification.category_list.reduce((prev, cur) =>{
      return prev + cur.label +','
    }, mcClassListStartText)
    
    const showMcClass = mcClassList !== mcClassListStartText
    
    mcClassList = mcClassList.slice(0, -1);

    //classifyText
    const classifyTextKeys = Object.keys(analysis.classify_text)
    const classifyText = classifyTextKeys.reduce((prev, cur) => {
      if(analysis.classify_text[prev] > analysis.classify_text[cur]){
        return prev
      }else{
        return cur
      }
    },'')




    console.log('mcClassList', mcClassList)

    //not checking for nested objects
    let data = analysisKeys.map( (item, i ) => {
      if(typeof(analysis[item]) !== 'object'){
        const formattedWords = item.split('_').map(word =>{
          return word[0].toUpperCase() + word.slice(1)
        }).join(' ')
        return <li key={i}>{formattedWords} = {analysis[item]}</li>
      }
    })

    let word_percents = grades.map((item, i ) => {

          return <li key={i}>{item} : { Math.round(gradePercents[i],-1)}</li>


    })

    return(
      <div>
        <h1> Mr.Meow, the robotic English teaching cat, has read through your essay and has determined you should receive {grade[gradeIndex]}</h1>
        <h2> Here's how your grade probabilities breakdown </h2> 
        <ul> 
            {word_percents}
        </ul>
        <h2> Here's some facts about your writing </h2>
        <ul>
        {showMcClass && <li>{mcClassList}</li>}
          <li>You write similar to the book {classifyText}.</li>
        </ul>
        <ul>
          {data}
        </ul>
        <h1> Meow! </h1>  


      </div>
    )
}


