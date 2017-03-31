import React, { Component } from 'react';
import {
  BrowserRouter as Router, 
  Route, 
  Link,
  Switch
} from 'react-router-dom'

import PlainText from './PlainText.js'
import essays from './essays'
import Technical from './Technical'
export default class App extends Component{
  
  constructor(props){
    super(props)
  }

  render(){
    return(
      <Router>
        <div >
          <nav className="navbar navbar-default ">
          <div className="container-fluid">
              <div className="navbar-header">
                  <img height='50' width='50' src="cat_image.gif"></img>
                  <a className="navbar-brand" href="/">Mr. Meows Magical Essay Grader</a>
             </div>
          <ul className="nav navbar-nav">

              <li className="active"><Link to="/">Home</Link> </li>
              <li><Link to="/technical">Technical Info</Link> </li> 
          </ul>
          </div>

            </nav>
          <hr/>
          <Switch>
            <Route exact path="/" component={PickAnEssay}/>
            <Route exact path="/technical" component={Technical}/>
            <Route exact path="/:essay" 
              render={props => {
                const essayNum = props.match.url.replace('/', '').replace("essay","")
                return <PlainText essay={essayNum}/>
              }
            }/>
          </Switch>
        </div>
      </Router>
    )
  }
}

function createEssayRoutes(essays){
  return Object.keys(essays).map( essay => {
    return <li><Link to={`/${essay}`}>{essay}</Link></li>
  })
}

const PickAnEssay = () => (
  <div>
    <h1>Pick your Essay</h1>
    <p>Below are a set of eight essays you can use to practice your writing. Try one!</p>
     {createEssayRoutes(essays)}
  </div>
)

