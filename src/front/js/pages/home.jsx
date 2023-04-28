import React, { useContext } from "react";
import { Context } from "../store/AppContext";
import "../../styles/home.css";
import MVDP from '../../img/MVDP.jpg';
import Mapa from '/workspaces/finalPedalPartner.com/src/front/img/mapa.jpg';

export const Home = () => {
  const { store, actions } = useContext(Context);

  return (
    <div className="container-fluid position-relative d-inline-block justify-content-center p-3" id="mainView">
      <h1 className="text-center my-0">Bienvenido a Pedal Partner</h1>
      <h2 className="text-center">Tu guía en el mundo de la bicicleta</h2>
      <hr />
      <div className="container-fluid position-relative">
        <div className="row container-fluid justify-content-around mx-0 px-5">
      {/* each section will become their own col, just one per row */}
          <div className="col-5 align-center"> 
            <div className="card container px-0" id="homeCard">{/* for Eventos */}
              <h3 className="card-header my-0">Próximo evento:</h3>
              <div className="overflow-hidden" id="samPhoto">
                <img src={Mapa} alt="Mapa" id="regPhoto" className="card-img img-responsive" />
              </div>
              <div className="card-body py-0 d-inline">
                <a className="card-title" href="eventos">
                  <h4 className="card-title mt-2">Ciclovías y Calles Abiertas</h4>
                </a>
                <p className="card-subtitle text-secondary">Miercoles 12 de abril del 2023</p>
                <a className="btn btn-outline-primary my-1" role="button" href="eventos">Muéstrame mas</a>
              </div>
            </div>
          </div>
          <div className="col-5 align-center"> {/* for Noticias */}
        <div className="card container px-0" id="homeCard">
          <h3 className="card-header my-0">Última Noticia:</h3>
          <div className="overflow-hidden" id="samPhoto">
            <img src={MVDP} alt="MVDP" id='regPhoto' className="card-img img-responsive"/>
          </div>
          <div className="card-body my-0 py-0 d-inline">
            <a className="card-title my-1" href="noticias">
              <h4 className="card-title mt-2">El ciclista neerlandés Mathieu van der Poel conquista su primera París-Roubaix</h4>
            </a>
            <p className="card-subtitle text-secondary">Miercoles 12 de abril del 2023</p>
            <a className="btn btn-outline-primary my-1" role="button" href="noticias">Muéstrame mas</a>
          </div>
    
      </div>



        </div>
      </div>

      
    </div>
      
      
      </div>


      
    

  );
};
