import React from "react"
import CPM from '../../img/cpm.jpg';

const Estructura2 = () => {
    return (
        <div className="col-12 align-center">
            <div className="card container-fluid p-0 m-0 my-2" id="structure">
                <div className="row justify-content-center mx-0">
                    <div className="col-4 overflow-hidden">
                        <img src={CPM} alt="Mapa" id="regPhoto" className="img-fluid" />
                    </div>
                    <div className="col-8 card-body">
                        <p className="card-subtitle text-secondary text-end fs-6 my-0">Domingo 30 de abril del 2023</p>
                        <h2 className="card-title my-1 text-end">Convocatorias Cicletada del Primer Martes</h2>
                        <div className="overflow-y-scroll">
                            <p className="card-text text-end overflow-y-scroll">La Cicletada del Primer Martes (CPM) es una instancia en la que muchos/as ciclistas se reunen a pedalear y hacen un recorrido por la ciudad al estilo "ciclomarcha" visibilizando la gran cantidad de personas que usan actualmente la bicicleta.
                                En Santiago tuvo sus inicios en los 90 y ya después del 2012 muchas otras ciudades en Chile comenzaron a sumarse. En otras regiones se hacen convocatorias parecidas pero el primer viernes, el último sábado, último martes, etc.
                                Internacionalmente también está asociada al concepto de Masa Crítica, en relación a la gran cantidad de ciclistas que participan (en Santiago hablamos de miles).
                                El concepto viene de cómo se vivían las calles en China, donde los ciclistas tenían que esperar en los semáforos hasta acumular suficiente gente como para poder cruzar y avanzar seguros en masa.
                            </p>
                        </div>
                    </div>
                </div>
            </div>


        </div>)
}










export default Estructura2