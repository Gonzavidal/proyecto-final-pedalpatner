import React from "react";
import Mapa from '/workspaces/finalPedalPartner.com/src/front/img/mapa.jpg';
import Estructura1 from "./evento1.jsx";
import Estructura2 from "./evento2.jsx";

export const Eventos = () => {
    return (
        <div className="container-fluid position-relative d-inline-block my-2 px-0" id="mainView">
            <h1 className="text-center">Eventos</h1>
            <hr className="hr" />
            <div className="row row-cols-1 container-fluid m-0 p-2">
                <Estructura1 />
                <Estructura2 />
            </div>
        </div>)}
                