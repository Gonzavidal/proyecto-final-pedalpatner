import React, { useState, useContext } from "react";
import { Context } from "../store/AppContext";
import { useNavigate } from "react-router-dom";

export const Login = () => {
  const { store, actions } = useContext(Context);
  // const [email, setEmail] = useState("")
  // const [password,setPassword] = useState("")

  const navigate = useNavigate();

  return (
    <div
      className="container-fluid position-relative d-inline-block my-2 px-0"
      id="mainView"
    >
      <h1 className="col-12 text-center">Login</h1>
      <hr className="col-12 hr my-2" />
      <form
        className="col-12 mt-1 px-5 position-relative fs-4"
        onSubmit={(e) => actions.login(e, navigate)}
      >
        <div className="container-fluid mx-5 px-5">
          <div className="row row-cols-1 justify-content-center mt-3 px-5">
            <div className="col-8 form-group my-3 d-flex">
              <label className="pt-2 mx-3" htmlFor="#inputEmail">
                Email
              </label>
              <input
                type="email"
                className="form-control"
                name="email"
                id="inputEmail"
                aria-label="emailInput"
                aria-describedby="inputGroup"
                value={store.email}
                onChange={actions.handleChange}
              />
            </div>
            <div className="col-8 form-group my-3 d-flex">
              <label className="pt-2 mx-3" htmlFor="#inputPassword">
                Password
              </label>
              <input
                type="password"
                className="form-control"
                name="password"
                id="inputPassword"
                aria-label="searchInput"
                aria-describedby="inputGroup"
                value={store.password}
                onChange={actions.handleChange}
              />
            </div>
          </div>
          <div className="row mt-3">
            <button
              type="submit"
              className="col-sm-1 mx-auto btn btn-danger fs-5 px-2"
            >
              Entrar
            </button>
          </div>
        </div>
      </form>
    </div>
  );
};
