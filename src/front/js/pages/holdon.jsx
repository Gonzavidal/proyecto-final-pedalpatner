import React from "react";

const HoldOn = () => {
    return (
        <div className="row container-fluid justify-content-around mx-0 px-5">
            <div className="col-8">
                <div className="card">
                    <div className="card-featured">
                        Parece que no estás conectado
                    </div>
                    <div className="card-title">Necesitamos que te autentifiques para que puedas acceder a todas las funcionalidades</div>
                    <div className="row">
                        <div className="col-6">
                            <Link to="/login" className="btn">Aquí para iniciar sesión</Link>
                            <Link to="/registro" className="btn">Aquí para registrarse</Link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}