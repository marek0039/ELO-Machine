//created by Marek Niemyjski
//copied from Geeks for Geeks
//https://www.geeksforgeeks.org/create-a-responsive-navbar-using-reactjs/

import React from "react";
import "./App.css";
import Navbar from "./components/Navbar";
import {
	BrowserRouter as Router,
	Routes,
	Route,
} from "react-router-dom";
import Home from "./pages";
import Bracket from "./pages/bracket";
import Leaderboards from "./pages/leaderboards";
import Matches from "./pages/matches";
import Rules from "./pages/rules";

function App() {
	return (
		<Router>
			<Navbar />
			<Routes>
				<Route path="/" element={<Home />} />
				<Route path="/rules" element={<Rules />} />
				<Route path="/leaderboards" element={<Leaderboards />} />
				<Route path="/matches" element={<Matches />} />
				<Route path="/bracket" element={<Bracket />} />
			</Routes>
		</Router>
	);
}

export default App;
