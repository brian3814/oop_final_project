import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Switch, Route, Link } from 'react-router-dom'
import Login from './Components/Login'
import {useState} from 'react'
import TokenHandler from './Components/TokenHandler';
import Dashboard from './Components/Dashboard';

function App() {
	const [loggedIn,setLoggedIn] = useState(false);

	if(!loggedIn) {
		return <Login setLoggedIn={setLoggedIn} />
	}	

	return (
		<Dashboard/>
  	);
}

export default App;
