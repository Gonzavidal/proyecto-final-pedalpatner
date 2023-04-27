import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="container-fluid text-center">
		<h1>Bienvenido a Pedal Partner</h1>
		<hr/>
		<div className="row">
		  <div className="col">
		  </div>
		</div>
	  </div>
	);
};
