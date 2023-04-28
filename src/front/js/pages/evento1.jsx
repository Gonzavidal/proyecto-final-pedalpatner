import React from "react";
import Mapa from '/workspaces/finalPedalPartner.com/src/front/img/mapa.jpg';

const Estructura1 = () => {
    return (
        <div className="col-12 align-center">
                <div className="card container-fluid p-0 m-0" id="structure">
                    <div className="row justify-content-center mx-0">
                        <div className="col-4 object-fit-contain">
                            <img src={Mapa} alt="Mapa" id="regPhoto" className="img-fluid" />
                        </div>
                        <div className="col-8 card-body">
                            <p className="card-subtitle text-secondary text-end fs-6 my-0">Miercoles 12 de abril del 2023</p>
                            <h2 className="card-title my-1 text-end">Ciclorecreovías y «Calles Abiertas» en la Región Metropolitana</h2>
                            <div className="overflow-y-scroll">
                                <p className="card-text text-end overflow-y-scroll">Todos los domingo del año entre las 09:00 y 14:00, más de 40 km de vías en la Región Metropolitana se cierran al tránsito motorizado. 
                    Algunas iniciativas que buscan fomentar el uso de ciclos, son las «CicloRecreovías» y 
                    «Calles Abiertas Familiares»; la primera ya disponible en Providencia, Las Condes, Santiago Centro, 
                    Vitacura, Ñuñoa y Renca. Se recomienda a los conductores de vehículos motorizados, a que 
                    tomen precaución por posibles rutas desviadas.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>


                </div>
           )

}

export default Estructura1;