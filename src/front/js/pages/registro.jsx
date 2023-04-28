import React, { useState, useContext } from "react";
import { Context } from "../store/AppContext";

export const Registro = () => {
  const { store, actions } = useContext(Context);
  const [isChecked, setIsChecked] = useState(false)
  return (
    <div className="row container-fluid position-relative text-center p-3" id="mainView">
      <h1 className="col-12">Registro</h1>
      <hr className="col-12 hr my-2" />

      {/* form container 4 whole body */}
      <form
        className="col-12 mt-1 px-5 position-relative"
        onSubmit={actions.handleSubmitContacto}
      >
        <div className="row container-fluid justify-content-center">
            <h3 className="col-12">¿Qué tipo de usuario eres?</h3>
            <div className="row container-fluid floating-label justify-content-center d-flex">
              <div className="col-3 form-check ms-2 my-1 fs-5">
                <input
                  className="form-check-input"
                  type="radio"
                  name="tipos_id"
                  id="flexRadioDefault1"
                  value={store.tipos_id}
                  onChange={actions.handleChange}
                />
                <label className="form-check-label" htmlFor="flexRadioDefault1">
                  Ciclista
                </label>
              </div>
              <div className="col-3 form-check ms-2 my-1 fs-5">
                <input
                  className="form-check-input"
                  type="radio"
                  name="tipos_id"
                  id="flexRadioDefault2"
                  checked={isChecked}
                  value={store.tipos_id}
                  onChange={actions.handleChange}
                />
                <label
                  className="form-check-label fs-5"
                  htmlFor="flexRadioDefault2"
                >
                  Mecánico
                </label>
              </div>
            </div>
        </div>
        <div className="row d-inline justify-content-center mb-3 fs-5">
            <div className="col-7 my-2 form-floating d-flex mx-auto">
              <input
                type="text"
                className="form-control"
                name="username"
                id="inputUsername"
                aria-label="searchInput"
                aria-describedby="inputGroup"
                value={store.username}
                onChange={actions.handleChange}
              />
              <label className="pt-2 mx-2" htmlFor="#inputUsername">
                Username
              </label>
            </div>
            <div className="col-7 my-2 form-floating d-flex mx-auto">
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
            <div className="col-7 my-2 form-floating d-flex mx-auto">
              <input
                type="password"
                className="form-control"
                name="password"
                id="inputPassword"
                aria-label="passwordInput"
                aria-describedby="inputGroup"
                value={store.password}
                onChange={actions.handleChange}
              />
              <label className="pt-2 mx-2" htmlFor="#inputPassword">
                Password
              </label>
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
      </form>
    </div>
  );
}
