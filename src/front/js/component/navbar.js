import React, { useState, useContext } from "react";
import { Context } from "../store/AppContext";
import { Link } from "react-router-dom";
import { FaAcquisitionsIncorporated, FaBars } from "react-icons/fa";
import logo from "../../img/logo.png";

export const Navbar = () => {
  const { store, actions } = useContext(Context);
  return (
    <nav className="row navbar navbar-expand-lg position-relative bg-danger fs-5 mx-0 py-0">
      <div className="col-12 container-fluid">
        <Link className="navbar-brand active text-white mx-3 p-1" to="/home">
          <img src={logo} id="logo" />
        </Link>
        <button
          className="navbar-toggler m-2"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div
          className="collapse navbar-collapse justify-content-end"
          id="navbarSupportedContent"
        >
          <ul className="navbar-nav">
            <Link to="/tienda" className="nav-item mx-2 text-white py-3">
              Encuentra tu tienda
            </Link>
            <li className="nav-item dropdown d-flex align-items-center fs-4">
              <Link
                className="nav-link text-white py-3"
                to="#"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                Comunidad
              </Link>
              <ul className="dropdown-menu text-white">
                <Link to="/noticias" className="dropdown-item">
                  Noticias
                </Link>
                <Link to="/eventos" className="dropdown-item">
                  Eventos
                </Link>
              </ul>
            </li>
            <Link to="/contacto" className="nav-item mx-2 py-3 text-white">
              Contacto
            </Link>
            <Link to="/ayuda" className="nav-item mx-2 py-3 text-white">
              Ayuda
            </Link>
            <li className="nav-item dropdown mx-2">
              <Link
                className="nav-link py-2 my-auto"
                to="#"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                <FaBars className="fa-2x text-white my-auto" />
              </Link>
              <ul className="dropdown-menu dropdown-menu-lg-end text-white">
                <li>
                  {store.token != "" ? (
                    <Link className="dropdown-item">Usuario</Link>
                  ) : (
                    <Link to="/login" className="dropdown-item">
                      Login
                    </Link>
                  )}
                </li>
                <li>
                  <Link className="dropdown-item">Mi Perfil</Link>
                </li>
                <li>
                  <Link to="/registro" className="dropdown-item">
                    Registro
                  </Link>
                </li>
                <hr className="dropdown-divider" />
                <li>
                  <Link className="dropdown-item" onClick={actions.logout}>
                    Salir
                  </Link>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};
