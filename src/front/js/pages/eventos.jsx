import React, { useContext, useEffect } from "react";
import { Context } from "../store/AppContext";
import Estructura1 from "./evento1.jsx";
import Estructura2 from "./evento2.jsx";

export const Eventos = () => {
  const { store, actions } = useContext(Context);
  console.log("que trae", store.contacto);
  useEffect(() => actions.getComunicacion(), []);
  return (
    <div
      className="container-fluid position-relative d-inline-block p-2"
      id="mainView"
    >
      <h1 className="text-center my-1">Eventos</h1>
      <hr className="hr" />
      {store.contacto?.length <= 0 ? (
        <div className="row row-cols-1 container-fluid m-0 p-2">
          <Estructura1 />
          {/* <br/>
                <Estructura2 /> */}
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
