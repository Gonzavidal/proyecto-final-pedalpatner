import React, { useContext } from "react";
import { Context } from "../store/AppContext";

export default function Contacto() {
  const { store, actions } = useContext(Context);

  return (
    <div className="row container-fluid position-relative text-center mx-0">
      <h1 className="col-12">Contacto</h1>
      <hr className="col-12 hr my-2" />

      {/* form container 4 whole body */}
      <form
        className="col-12 mt-1 px-5 position-relative"
        onSubmit={actions.handleSubmiContacto}
      >
        {/* row 4 first filter: service type + event public (optional) */}
        <div className="row mx-5 px-5">
          {/* half row: service type */}
          <div className="col-6 text-start">
            <h3>Seleccione tipo de servicio</h3>
            <div className="container-fluid">
              <div className="form-check ms-2 my-1 fs-5">
                <input
                  className="form-check-input"
                  type="radio"
                  name="tipos_id"
                  id="flexRadioDefault1"
                  value={store.tipos_id}
                  onChange={actions.handleChange}
                />
                <label className="form-check-label" htmlFor="flexRadioDefault1">
                  Noticia
                </label>
              </div>
              <div className="form-check ms-2 my-1 fs-5">
                <input
                  className="form-check-input"
                  type="radio"
                  name="tipos_id"
                  id="flexRadioDefault2"
                  checked
                  value={store.tipos_id}
                  onChange={actions.handleChange}
                />
                <label
                  className="form-check-label fs-5"
                  htmlFor="flexRadioDefault2"
                >
                  Evento
                </label>
              </div>
              <div className="form-check ms-2 my-1 fs-5">
                <input
                  className="form-check-input"
                  type="radio"
                  name="tipos_id"
                  id="flexRadioDefault3"
                  value={store.tipos_id}
                  onChange={actions.handleChange}
                />
                <label
                  className="htmlForm-check-label fs-5"
                  htmlFor="flexRadioDefault3"
                >
                  Mensaje
                </label>
              </div>
            </div>
          </div>
          {/* half row : conditional formcheck for event type */}
          <div className="col-6 text-start">
            <h3>Destinatario Evento</h3>
            <div className="container-fluid">
              <div className="form-check ms-2 my-1 fs-5">
                <input
                  className="form-check-input"
                  type="checkbox"
                  name="destino"
                  id="recipientCiclista"
                  value={store.destino}
                  onChange={actions.handleChange}
                />
                <label
                  className="form-check-label"
                  htmlFor="#recipientCiclista"
                >
                  Ciclista
                </label>
              </div>
              <div className="form-check ms-2 my-1 fs-5">
                <input
                  className="form-check-input"
                  type="checkbox"
                  name="destino"
                  id="recipientMecanico"
                  value={store.destino}
                  onChange={actions.handleChange}
                />
                <label
                  className="form-check-label"
                  htmlFor="#recipientMecanico"
                >
                  Mecánico
                </label>
              </div>
            </div>
          </div>
        </div>

        {/*row 4 rest of form : title, mail, textarea, files*/}
        <div className="row mt-3 px-5">
          <div className="row d-flex mb-3 fs-5">
            <div className="col-7 form-floating d-flex">
              <input
                type="text"
                className="form-control"
                name="titulo"
                id="inputTitle"
                aria-label="searchInput"
                aria-describedby="inputGroup"
                value={store.titulo}
                onChange={actions.handleChange}
              />
              <label className="pt-2 mx-2" htmlFor="#inputTitle">
                Titulo
              </label>
            </div>
            <div className="col-5 form-floating d-flex">
              <input
                type="text"
                className="form-control"
                name="email"
                id="inputEmail"
                aria-label="searchInput"
                aria-describedby="inputGroup"
                value={store.email}
                onChange={actions.handleChange}
              />
              <label className="pt-2 mx-2" htmlFor="#inputEmail">
                Email
              </label>
            </div>
          </div>
          <div className="row d-inline px-5">
            <div className="col-10 mx-auto px-5">
              <div className="form-floating my-0">
                <textarea
                  className="form-control"
                  name="descripcion"
                  id="inputTextArea"
                  aria-label="With textarea"
                  value={store.descripcion}
                  onChange={actions.handleChange}
                  style={{ height: 200 }}
                />
                <label htmlFor="#inputTextArea" className="fs-5 pt-2 mx-1">
                  Descripción
                </label>
              </div>
            </div>
            <div className="col-5 d-flex mx-auto offset-md-3">
              <label
                className="col-sm-5 my-auto form-label px-0"
                for="customFile"
              >
                Adjuntar archivo
              </label>
              <input
                type="file"
                className="col-sm-1 form-control mt-1"
                name="data"
                id="customFile"
                value={store.data}
                onChange={actions.handleChange} //aqui se debe cambiar la forma de capturar el file
                //habria que probar si 1° esto resulta
              />
            </div>
          </div>
          <div className="row mt-3">
            <button
              type="submit"
              className="col-sm-1 mx-auto btn btn-danger fs-5 px-2"
            >
              Enviar
            </button>
          </div>
        </div>
      </form>
    </div>
  );
}
