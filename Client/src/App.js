import homepage from './components/homepage.js';
import v from './components/v'
import './App.css';

function App(homepage) {
  return (
    <div className='App-Header'>
      
    <div className='App'>
      
      <h3> WEB 3 Application </h3> 
      
      <label> Full Name:  </label>
      <input class = 'input'  type="text" placeholder="Name"/> <br/>
      <small class='small'> Your full name please </small>
      <br/><br/>
      <label> Unit Name:  </label>
      <input class = 'input' name="phone" type="text" placeholder="Unit Name" /> <br/>
      <small class='small'> The unit name of asset </small> <br/><br/>'
      <label> Description: </label>
      <input className= 'in'  type="text" placeholder="Description" /> <br/>
      <small class='small'> description of this asset </small> <br/><br/>'
      <button id = 'button'> Generate Certificates </button>' <br/> <br/>
      <button id = 'button'> Show Extra </button>'
      </div>
      </div>
    
    
  );
}

export default App;
