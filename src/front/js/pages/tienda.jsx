import React, { useState } from "react"
import Maps from './Maps.jsx';

export const Tienda = () => {
  const [name, setName] = useState("")
  const [jefe, setJefe] = useState("")
  const [contacto, setContacto] = useState("")
  const [mant, setMant] = useState("")
  const [indum, setIndum] = useState("")
  const [bici, setBici] = useState("")
  const [efect, setEfect] = useState("")
  const [transf, setTransf] = useState("")
  const [tarjetas, setTarjetas] = useState("")

  return (
    <div className="container-fluid text-center mb-5 position-relative d-inline-block p-3" id="mainView">
      <h1>Encuentra tu tienda</h1>
      <hr className="hr" />
      <div className="row">
        <div className="col-6">

          <Maps
            setName={setName}
            setJefe={setJefe}
            setContacto={setContacto}
            setMant={setMant}
            setIndum={setIndum}
            setBici={setBici}
            setEfect={setEfect}
            setTransf={setTransf}
            setTarjetas={setTarjetas} />

        </div>
        <div className="col-5">
          {/*exclusive div 4 text inputs*/}
          <div className="row mx-3">
            <div className="col-12 input-group">
              <span className="input-group-text" id="inputGroup">Nombre Tienda</span>
              <input type="text" className="form-control bg-white" id="txtTienda" aria-label="searchInput" aria-describedby="inputGroup" defaultValue={name} disabled />
            </div>
            <div className="col-12 input-group my-2">
              <span className="input-group-text" id="inputGroup">Jefe Tienda</span>
              <input type="text" className="form-control bg-white" id="txtJefe" aria-label="searchInput" aria-describedby="inputGroup" defaultValue={jefe} disabled />
            </div>
            <div className="col-12 input-group">
              <span className="input-group-text" id="inputGroup">Contacto</span>
              <input type="text" className="form-control bg-white" id="txtContacto" placeholder="+56 9 XXXX XXXX" aria-label="searchInput" aria-describedby="inputGroup"
                defaultValue={contacto} disabled />
            </div>
          </div>

          {/*rest of info*/}
          <div className='row mx-3 mt-2'>
            <div className="col-12 input-group">
              <span className="input-group-text" id="inputGroup">Mantención desde</span>
              <span class="input-group-text">$</span>
              <input type="text" className="form-control bg-white" id="txtMant" aria-label="searchInput" aria-describedby="inputGroup"
                defaultValue={mant} disabled />
            </div>
            <div className="col-12 input-group my-2">
              <span className="input-group-text" id="inputGroup">Indumentaria desde</span>
              <span class="input-group-text">$</span>
              <input type="text" className="form-control bg-white" id="txtIndum" aria-label="searchInput" aria-describedby="inputGroup"
                defaultValue={indum} disabled />
            </div>
            <div className="col-12 input-group">
              <span className="input-group-text" id="inputGroup">Bicicletas desde</span>
              <span class="input-group-text">$</span>
              <input type="text" className="form-control bg-white" id="txtBici" aria-label="searchInput" aria-describedby="inputGroup"
                defaultValue={bici} disabled />
            </div>
          </div>

          {/*div 4 checks + inputs*/}
          <div className="row mx-3 mt-2">
            {/*<h4 className="col-12">Medios de Pago Disponibles</h4>*/}
            <div className="col-12 input-group">
              <span className="input-group-text" id="inputGroup">Efectivo</span>
              <input type="text" className="form-control bg-white" id="txtMant" aria-label="searchInput" aria-describedby="inputGroup"
                defaultValue={efect} disabled />
            </div>
            <div className="col-12 input-group my-2">
              <span className="input-group-text" id="inputGroup">Transferencias</span>
              <input type="text" className="form-control bg-white" id="txtIndum" aria-label="searchInput" aria-describedby="inputGroup"
                defaultValue={transf} disabled />
            </div>
            <div className="col-12 input-group">
              <span className="input-group-text" id="inputGroup">Tarjetas</span>
              <input type="text" className="form-control bg-white" id="txtBici" aria-label="searchInput" aria-describedby="inputGroup"
                defaultValue={tarjetas} disabled />
            </div>
          </div>

        </div>
      </div>
    </div>
  );
}
