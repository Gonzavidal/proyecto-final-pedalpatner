import React from "react";
import MVDP from '../../img/MVDP.jpg';

export const Noticias = () => {
  return (
    <div className="container-fluid position-relative d-inline-block p-2" id="mainView">
      <h1 className="text-center my-1">Noticias</h1>
      <hr className="hr" />
      <div className="row justify-content-center">
        <div className="col-12 align-center">
          <div className="card container-fluid p-0 m-0 my-2" id="structure">
            <div className="row justify-content-center mx-0">
                <div className="col-4 overflow-hidden">
                    <img src={MVDP} alt="Mapa" id="regPhoto" className="img-fluid" />
                </div>
                <div className="col-8 card-body">
                    <p className="card-subtitle text-secondary text-end fs-6 my-0">Domingo 30 de abril del 2023</p>
                    <h2 className="card-title my-1 text-end">El ciclista neerlandés Mathieu van der Poel conquista su primera París-Roubaix</h2>
                    <div className="overflow-y-scroll">
                        <p className="card-text text-end overflow-y-scroll">gitLa 120ª edición de la carrera de la francesa París-Roubaix de un solo día se celebró este domingo.
            El neerlandés Mathieu van der Poel conquistó su primera París-Roubaix fascinando con su ataque a 15 km del final.
            Un total de 175 ciclistas pedalearon 257 kilómetros.
                        </p>
                    </div>
                </div>
            </div>
          </div>
        </div>
      </div>
    </div>)};


          