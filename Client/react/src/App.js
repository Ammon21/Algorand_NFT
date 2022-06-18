import './App.css';
import React from 'react';

function App() {
  return (
    <div className='App-Header'>

     <div class="topnav">
     <a class="active" href="#home">10 Academy</a>
     <a href="#news">Trainee</a>
     <a href="#contact">Certificates</a>
     <a href="#about">Wallet</a>
      
    </div>   
      
    <div className='App'>
      
      <h3> Algorand Certificates </h3> 
      <form>
      <label> Full Name:  </label>
      <input class = 'input'  type="text" placeholder="Name"/> <br/>
      <small class='small'> Your full name please </small>
      <br/><br/>
      <label> Unit Name:  </label>
      <input class = 'input' name="phone" type="text" placeholder="Unit Name" /> <br/>
      <small class='small'> The unit name of assets </small> <br/><br/>'
      <label> Description: </label>
      <input className= 'in'  type="text" placeholder="Description" /> <br/>
      <small class='small'> description of this asset </small> <br/><br/>'
      <button id = 'button'> Generate Certificates </button>' <br/> <br/>
      <button id = 'button'> Show Extra </button>'
      </form>
      </div>
      </div>
    
    
  );
}

export default App;
