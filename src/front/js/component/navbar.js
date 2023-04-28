import React from "react";
import { FaBars } from "react-icons/fa";
import Logo from "/workspaces/finalPedalPartner.com/src/front/img/logo.png";


export const Navbar = () => {
  return (
    <nav className="row navbar navbar-expand-lg position-relative bg-danger fs-5 mx-0 py-0">
      <div className="col-12 container-fluid">
        <a className="navbar-brand active text-white mx-3 p-1" href="/home">
          <img src={Logo} id="logo"/>
        </a>
        <button className="navbar-toggler m-2" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
          <ul className="navbar-nav">
            <a href="/tienda" className="nav-item mx-2 text-white py-3">Encuentra tu tienda</a>
            <li className="nav-item dropdown mx-2">
              <a
                className="nav-link text-white py-3"
                href="#"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                Comunidad
              </a>
              <ul className="dropdown-menu text-white">
                <a href="/noticias" className="dropdown-item">Noticias</a>
                <a href="/eventos" className="dropdown-item">Eventos</a>
              </ul>
            </li>
            <a href="/contacto" className="nav-item mx-2 py-3 text-white">Contacto</a>
            <a href="/ayuda" className="nav-item mx-2 py-3 text-white">Ayuda</a>
            <li className="nav-item dropdown mx-2">
              <a
                className="nav-link py-2 my-auto"
                to="#"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                <FaBars className="fa-2x text-white my-auto" />
              </a>
              <ul className="dropdown-menu dropdown-menu-lg-end text-white">
                <li>
                  <a className="dropdown-item">Usuario</a>
                </li>
                <li>
                  <a className="dropdown-item">Mi Perfil</a>
                </li>
                <hr className="dropdown-divider" />
                <li>
                  <a className="dropdown-item">Salir</a>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};
