import React, { useContext } from "react";
import { Context } from "../store/AppContext";
import "../../styles/home.css";
import MVDP from '../../img/MVDP.jpg';
import Mapa from '../../img/mapa.jpg';

export const Home = () => {
  const { store, actions } = useContext(Context);

  return (
    <div className="container-fluid position-relative d-inline-block justify-content-center p-3" id="mainView">
      <h1 className="text-center">Bienvenido a Pedal Partner</h1>
      <h4 className="text-center">Tu guía en el mundo de la bicicleta</h4>
      <hr />
      <div className="container-fluid position-relative">
        <div className="row container-fluid justify-content-around mx-0 px-5">
      {/* each section will become their own col, just one per row */}
          <div className="col-5 align-center"> 
            <div className="card container px-0" id="homeCard">{/* for Eventos */}
              <h4 className="card-header my-0">Próximo evento:</h4>
              <div className="overflow-hidden" id="samPhoto">
                <img src={Mapa} alt="Mapa" id="regPhoto" className="card-img img-responsive" />
              </div>
              <div className="card-body py-0 d-inline">
                <a className="card-title" href="eventos">
                  <h5 className="card-title mt-2">Ciclovías y Calles Abiertas</h5>
                </a>
                <p className="card-subtitle text-secondary">Miércoles 12 de abril del 2023</p>
                <a className="btn btn-outline-primary my-1" role="button" href="eventos">Muéstrame más</a>
              </div>
            </div>
          </div>
          <div className="col-5 align-center"> {/* for Noticias */}
        <div className="card container px-0" id="homeCard">
          <h4 className="card-header my-0">Última Noticia:</h4>
          <div className="overflow-hidden" id="samPhoto">
            <img src={MVDP} alt="MVDP" id='regPhoto' className="card-img img-responsive"/>
          </div>
          <div className="card-body my-0 py-0 d-inline">
            <a className="card-title my-1" href="noticias">
              <h5 className="card-title mt-2">El ciclista neerlandés Mathieu van der Poel conquista su primera París-Roubaix</h5>
            </a>
            <p className="card-subtitle text-secondary">Miércoles 12 de abril del 2023</p>
            <a className="btn btn-outline-primary my-1" role="button" href="noticias">Muéstrame más</a>
          </div>
    
      </div>



        </div>
      </div>

      
    </div>
      
      
      </div>


      
    

  );
};
