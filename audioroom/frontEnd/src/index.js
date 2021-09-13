import React from "react"
import ReactDOM from "react-dom"

import App from './components/App'

const root = document.getElementById('root');

const names = ["ram","ramsay","ranjith"];

ReactDOM.render(
	<div>
	{
		names.map((ele,idx) => <App name={ele} key={idx} />)
	}
	</div>
	, root
);