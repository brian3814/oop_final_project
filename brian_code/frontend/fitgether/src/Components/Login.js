import React, {useState} from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import "./Login.css";


async function checkAccess(credentials) {
	return fetch("http://192.168.0.14:5000/checkaccess", {
		method: "POST",
		headers: {
			"Access-Control-Allow-Headers":"Origin, X-Requested-With, Content-Type, Accept",
			"Access-Control-Allow-Origin":"*" ,
			"Content-Type": "application/json",
		},
		body: JSON.stringify(credentials)
	})
	.then((data) => data.json());
}

export default function Login({setLoggedIn}) {
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");

	function validateForm() {
		return email.length > 0 && password.length > 0;
	}

	async function handleSubmit(event) {
		event.preventDefault();

		const info = await checkAccess({
			email,
			password
		});
		console.log(info)
		if(info!==null)
		{
			setLoggedIn(true);
		}
	}

	return ( 
		<div className = "Login" >
			<Form onSubmit = {handleSubmit}>
				<Form.Group size = "lg" controlId = "email" >
					<Form.Label > Email: </Form.Label>
					<Form.Control autoFocus type = "email" value = {email} onChange = {(e) => setEmail(e.target.value)}/>
				</Form.Group> 
				<br/>
				<Form.Group size = "lg" controlId = "password" >
					<Form.Label > Password: </Form.Label> 
					<Form.Control type = "password" value = {password} onChange = {(e) => setPassword(e.target.value)}/>
				</Form.Group>
				<Button block size = "lg" type = "submit" disabled = {!validateForm()} >
					Login 
				</Button>
			</Form> 
		</div>
	);
}