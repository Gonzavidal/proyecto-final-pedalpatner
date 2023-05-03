import React from "react"
import Mapa from '../../img/mapa.jpg';

const Estructura2 = () => {
    return (
        <div className="col-12 align-center">
        <div className="card container-fluid p-0 m-0 my-2" id="structure">
            <div className="row justify-content-center mx-0">
                <div className="col-4 overflow-hidden">
                    <img src={Mapa} alt="Mapa" id="regPhoto" className="img-fluid" />
                </div>
                <div className="col-8 card-body">
                    <p className="card-subtitle text-secondary text-end fs-6 my-0">Domingo 30 de abril del 2023</p>
                    <h2 className="card-title my-1 text-end">Primer Round Copa Chile CX: Clásica Radio Rueda Libre</h2>
                    <div className="overflow-y-scroll">
                        <p className="card-text text-end overflow-y-scroll">Todos los domingo del año entre las 09:00 y 14:00, más de 40 km de vías en la Región Metropolitana se cierran al tránsito motorizado. 
            Algunas iniciativas que buscan fomentar el uso de ciclos, son las «CicloRecreovías» y 
            «Calles Abiertas Familiares»; 
                        </p>
                    </div>
                </div>
            </div>
        </div>


        </div>)}










export default Estructura2