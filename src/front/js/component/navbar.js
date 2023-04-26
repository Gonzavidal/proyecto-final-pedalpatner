import React from "react";
import { Link } from "react-router-dom";
import { FaBars } from "react-icons/fa";

export const Navbar = () => {
	return (
		<nav className="row navbar navbar-expand-lg position-relative bg-danger fs-5 mx-0 py-0">
      <div className="col-12 container-fluid py-1">
        <a className="navbar-brand text-white mx-3 mt-1" href="/home">Pedal Partner</a>
        <button className="navbar-toggler m-2" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
          <ul className="navbar-nav">
            <li className="nav-item mx-3">
              <Link to="/encuentraTienda" className="nav-link active text-white py-3" aria-current="page">Encuentra tu tienda</Link>
            </li>
            <li className="nav-item dropdown mx-3">
              <a className="nav-link dropdown-toggle text-white py-3" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Comunidad
              </a>
              <ul className="dropdown-menu text-white">
                <li><a className="dropdown-item" href="/noticias">Noticias</a></li>
                <li><a className="dropdown-item" href="/eventos">Eventos</a></li>
              </ul>
            </li>
            <li className="nav-item mx-3">
              <a className="nav-link text-white py-3" href="/contacto">Contacto</a>
            </li>
            <li className="nav-item dropdown mx-3">
              <a className="nav-link dropdown-toggle py-2" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              <FaBars className="fa-2x text-white"/>
              </a>
              <ul className="dropdown-menu dropdown-menu-lg-end text-white">
                <li><a className="dropdown-item">Usuario</a></li>
                <li><a className="dropdown-item">Mi Perfil</a></li>
                <li><a className="dropdown-item" href="/ayuda">Ayuda</a></li>
                <hr className="dropdown-divider" />
                <li><a className="dropdown-item">Salir</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
	)
};
