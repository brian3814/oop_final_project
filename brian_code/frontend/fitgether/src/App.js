import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Switch, Route, Link } from 'react-router-dom'
import Login from './Components/Login'

function App() {
  return (
    <BrowserRouter>
		<Switch>
			<Route exact path='' render={({location, history})=>
				<Login/>
			}/>
			<Route exact path='login' render={()=>
				<></>
			}/>
			<Route/>
			<Route/>
		</Switch>
    </BrowserRouter>
  );
}

export default App;
