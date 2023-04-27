import Formulario from '../assets/formContacto.jpeg'
import Vista from '../assets/vistaTienda.jpeg'
import Comunidad from '../assets/comunidad.jpg'

export default function Ayuda() {
    return (
        <div classNameName="text-center mb-4 text-black">
            <h1 classNameName="display-3">Ayuda</h1>
            <br></br>
            <hr classNameName="hr" />

            <div className="container text-center">
                <div className="row">
                    <div className="col">
                        <h2 className="text-end my-3">Encuentra tu tienda</h2>

                        <img src={Vista} alt="MVDP" id="regPhoto" />
                    </div>
                    <div className="col">
                        <h2 className="text-end my-3">Contáctanos</h2>
                        <img src={Formulario} alt="MVDP" id="regPhoto" />
                    </div>
                </div>
                <div className="row">
                    <div className="col">
                        <h2 className="text-end my-3">Comunidad</h2>
                        <img src={Comunidad} alt="MVDP" id="regPhoto" />

                    </div>
                    <div className="col">
                        <h2 className="">Mapa de Sitio</h2>
                        <h3 className="text-end my-3">En este sitio puedes encontrar:</h3>
                        <ul className="list-group list-group-flush">
                            <li className="list-group-item">Buscar Taller/Tienda</li>
                            <li className="list-group-item">Eventos</li>
                            <li className="list-group-item">Noticias</li>
                            <li className="list-group-item">Contacto</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

    );
}