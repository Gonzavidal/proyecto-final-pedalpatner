import React from "react";
import MVDP from '../../img/MVDP.jpg';
import Ciclista from '../../img/ciclista.jpg';

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
                  <p className="card-text text-end overflow-y-scroll">La 120ª edición de la carrera de la francesa París-Roubaix de un solo día se celebró este domingo.
                    El neerlandés Mathieu van der Poel conquistó su primera París-Roubaix fascinando con su ataque a 15 km del final.
                    Un total de 175 ciclistas pedalearon 257 kilómetros.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="row justify-content-center">
        <div className="col-12 align-center">
          <div className="card container-fluid p-0 m-0 my-2" id="structure">
            <div className="row justify-content-center mx-0">
              <div className="col-4 overflow-hidden">
                <img src={Ciclista} alt="Mapa" id="regPhoto" className="img-fluid" />
              </div>
              <div className="col-8 card-body">
                <p className="card-subtitle text-secondary text-end fs-6 my-0">Domingo 30 de abril del 2023</p>
                <h2 className="card-title my-1 text-end">Campeona angelina de ciclismo busca financiamiento para seguir compitiendo</h2>
                <div className="overflow-y-scroll">
                  <p className="card-text text-end overflow-y-scroll">Con 52 años y una corta pero exitosa carrera Silvia Figueroa se ha consolidado en el ciclismo local. La deportista, originaria de la comuna de Los Ángeles, conversó con radio San Cristóbal dando a conocer una realidad que, lamentablemente, se repite entre deportistas nacionales de distintas disciplinas. La falta de financiamiento es el gran problema que las entidades deportivas actuales aún no han logrado resolver y que llevan a competidoras, como Silvia, a recurrir a financiamientos privados.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>)
};


