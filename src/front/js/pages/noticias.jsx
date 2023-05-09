import React, { useEffect, useContext } from "react";
import MVDP from "../../img/MVDP.jpg";
import { Context } from "../store/AppContext";
import Estructura1 from "./evento1.jsx";

export const Noticias = () => {
  const { store, actions } = useContext(Context);
  console.log("que trae", store.contacto);
  useEffect(() => actions.getComunicacion(), []);
  return (
    <div
      className="container-fluid position-relative d-inline-block p-3"
      id="mainView"
    >
      <h1 className="text-center">Noticias</h1>
      <hr className="hr" />
      {store.contacto?.length <= 0 ? (
        <div className="row justify-content-center">
          <div className="col-4">
            <img
              src={
                "http://res.cloudinary.com/dhggemani/image/upload/v1683602157/avatars/znaktn5xazwv3vjbnlzm.jpg"
              }
              alt="MVDP"
              id="regPhoto"
              className="img-fluid m-2"
            />
          </div>
          <div className="col-7 px-4">
            <p className="text-secondary text-end fs-6 my-0">
              Miercoles 12 de abril del 2023
            </p>
            <h2 className="text-end my-3">
              El ciclista neerlandés Mathieu van der Poel conquista su primera
              París-Roubaix
            </h2>
            <p className="text-end ms-4 fs-5">
              La 120ª edición de la carrera de la francesa París-Roubaix de un
              solo día se celebró este domingo. El neerlandés Mathieu van der
              Poel conquistó su primera París-Roubaix fascinando con su ataque a
              15 km del final. Un total de 175 ciclistas pedalearon 257
              kilómetros. Los accidentes dejaron fuera de la carrera a figuras
              como el ex campeón mundial de carreras eslovaco Peter Sagan
              mientras se preparaba para retirarse. El belga Wout van Aert
              sufrió una desgracia en su duelo con el holandés Mathieu Van der
              Poel debido al pichazo en el neumático de su bicicleta, por lo
              tanto se quedó atrás y dejó solo a Van der Poel. El ciclista
              neerlandés se proclamó campeón con un tiempo de 5 horas, 28
              minutos y 41 segundos.
            </p>
          </div>
        </div>
      ) : (
        store.contacto.Datos_de_Comunicacion.map((element) => (
          <div className="row justify-content-center">
            <Estructura1
              titulo={element.titulo}
              descripcion={element.descripcion}
              created_at={element.created_at}
              imagen={element.imagen}
            />
          </div>
        ))
      )}
    </div>
  );
};
