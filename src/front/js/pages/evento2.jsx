import React from "react"
import Mapa from '../../img/mapa.jpg';

const Estructura2 = () => {
    return (
    <div className="row justify-content-center">
                <div className="col-4">
                    <img src={Mapa} alt="Mapa" id="regPhoto" className="img-fluid" />
                </div>
                <div className="col-7 px-4">
                    <p className="text-secondary text-end fs-6 my-0">Domingo 30 de abril del 2023</p>
                    <h2 className="text-end my-3">Primer Round Copa Chile CX: Clásica Radio Rueda Libre</h2>
                    <p className="text-end ms-4 fs-5">Todos los domingo del año entre las 09:00 y 14:00, varias calles y avenidas de la Región Metropolitana quedan disponibles a la recreación peatonal y de ciclos, y son cerradas al tránsito de vehículos motorizados.
                        Las iniciativas aplicadas a través de las «CicloRecreovías» y «Calles Abiertas Familiares» consideran más de 40 km de vías metropolitanas que en ese tramo horario y día, fomentan fomentan el uso de espacios públicos integrados y accesibles para todos y todas.

                        Por tanto recomendamos a los conductores de los vehículos motorizados estar atentos a los tramos intervenidos, para optar a un alternativa de tránsito.
                        La CicloRecreoVía está presente en Providencia, Las Condes, Santiago centro, Vitacura, Ñuñoa y Renca. También en el Parque Metropolitano, sábados y domingos.
                    </p>
                </div>
            </div>)
}

export default Estructura2