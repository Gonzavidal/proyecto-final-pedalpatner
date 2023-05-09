import React from "react";
import Mapa from "../../img/mapa.jpg";

const Estructura1 = (props) => {
  return (
    <div className="col-12 align-center">
      <div className="card container-fluid p-0 m-0" id="structure">
        <div className="row justify-content-center mx-0">
          <div className="col-4 object-fit-contain">
            <img
              src={props.imagen}
              alt="Mapa"
              id="regPhoto"
              className="img-fluid"
            />
          </div>
          <div className="col-8 card-body">
            <p className="card-subtitle text-secondary text-end fs-6 my-0">
              {props.created_at}
            </p>
            <h2 className="card-title my-1 text-end">{props.titulo}</h2>
            <div className="overflow-y-scroll">
              <p className="card-text text-end overflow-y-scroll">
                {props.descripcion}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Estructura1;
