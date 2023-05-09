import React from "react"
import Formulario from '../../img/formContacto.jpeg'
import Vista from '../../img/vistaTienda.jpeg'
import Comunidad from '../../img/comunidad.jpg'

export const Ayuda = () => {
    return (
        <div className="container-fluid position-relative d-inline-block p-3" id="mainView">
            <h1 className="text-center">Ayuda</h1>
            <hr className="hr" />
            <div className="container text-center">
                <div className="row row-cols-2">
                    <div className="col">
                        <h2 className="text-end my-3">Encuentra tu tienda</h2>
                        <img src={Vista} alt="MVDP" id="regPhoto" className="img-fluid" />
                    </div>
                    <div className="col">
                        <h2 className="text-end my-3">Contáctanos</h2>
                        <img src={Formulario} alt="MVDP" id="regPhoto" className="img-fluid" />
                    </div>
                </div>
                <div className="row">
                    <div className="col">
                        <h2 className="text-end my-3">Comunidad</h2>
                        <img src={Comunidad} alt="MVDP" id="regPhoto" className="img-fluid" />
                    </div>
                    <div className="col">
                        <h2 className="">Mapa de Sitio</h2>
                        <h3 className="text-center my-5">En este sitio puedes encontrar:</h3>
                        <ul className="list-group list-group-flush">
                            <li className="list-group-item">Buscar Taller/Tienda</li>
                            <li className="list-group-item">Eventos</li>
                            <li className="list-group-item">Noticias</li>
                            <li className="list-group-item">Contacto</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

    );
}