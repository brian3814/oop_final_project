import { BrowserRouter, Switch, Route, Link } from 'react-router-dom'
import {useState} from 'react'

const Dashboard = ()=>{
    return(
        <BrowserRouter>
			<Switch>
				<Route>
                    set meal
                </Route>
				<Route>
                    Check intake
                </Route>
			</Switch>
		</BrowserRouter>
    )
}

export default Dashboard;