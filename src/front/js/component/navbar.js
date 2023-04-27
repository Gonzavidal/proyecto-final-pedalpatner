import React from "react";
import { NavLink } from "react-router-dom";
import { FaBars } from "react-icons/fa";


export const Navbar = () => {
  return (
    <nav className="row navbar navbar-expand-lg position-relative bg-danger fs-5 mx-0 py-0">
      <div className="col-12 container-fluid py-1">
        <NavLink className="navbar-brand active text-white mx-3 mt-1" to="/home">Pedal Partner
          <button className="navbar-toggler m-2" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        </NavLink>
        <div className="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
          <ul className="navbar-nav">
            <NavLink to="/tienda" className="nav-item mx-3 text-white py-3">Encuentra tu tienda</NavLink>
            <li className="nav-item dropdown mx-3">
              <NavLink
                className="nav-link dropdown-toggle text-white py-3"
                to="#"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                Comunidad
              </NavLink>
              <ul className="dropdown-menu text-white">
                <NavLink to="/noticias" className="dropdown-item">Noticias</NavLink>
                <NavLink to="/eventos" className="dropdown-item">Eventos</NavLink>
              </ul>
            </li>
            <NavLink to="/contacto" className="nav-item mx-3 py-3 text-white">Contacto</NavLink>
            <li className="nav-item dropdown mx-3">
              <NavLink
                className="nav-link dropdown-toggle py-2"
                to="#"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                <FaBars className="fa-2x text-white" />
              </NavLink>
              <ul className="dropdown-menu dropdown-menu-lg-end text-white">
                <li>
                  <NavLink className="dropdown-item">Usuario</NavLink>
                </li>
                <li>
                  <NavLink className="dropdown-item">Mi Perfil</NavLink>
                </li>
                <li>
                  <NavLink className="dropdown-item" to="/ayuda">
                    Ayuda
                  </NavLink>
                </li>
                <hr className="dropdown-divider" />
                <li>
                  <NavLink className="dropdown-item">Salir</NavLink>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};
