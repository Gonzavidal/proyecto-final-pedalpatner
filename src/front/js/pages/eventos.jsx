import React from "react";
import Estructura1 from "./evento1.jsx";
import Estructura2 from "./evento2.jsx";

export const Eventos = () => {
    return (
        <div className="container-fluid position-relative d-inline-block p-2" id="mainView">
            <h1 className="text-center my-1">Eventos</h1>
            <hr className="hr" />
            <div className="row row-cols-1 container-fluid m-0 p-2">
                <Estructura1 />
                {/* <br/>
                <Estructura2 /> */}
            </div>
            <div className="row row-cols-1 container-fluid m-0 p-2">
                <Estructura2 />
                {/* <br/>
                <Estructura2 /> */}
            </div>
        </div>)}
                