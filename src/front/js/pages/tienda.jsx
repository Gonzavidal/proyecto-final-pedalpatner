import React, { useState } from "react"
import Maps from './Maps.jsx';

export const Tienda = () => {
  const [name, setName] = useState("")
  const [jefe, setJefe] = useState("") // duplicar por cada atributo del infowindows
  const [contacto, setContacto] = useState("")
  const [mant, setMant] = useState("")
  const [indum, setIndum] = useState("")
  const [bici, setBici] = useState("")

  return (
    <div className="container-fluid text-center position-relative d-inline-block p-3" id="mainView">
      <h1>Encuentra tu tienda</h1>
      <hr className="hr" />
      <div className="row">
        <div className="col-5">
          
          <Maps 
          setName={setName}
          setJefe={setJefe}
          setContacto={setContacto}
          setMant={setMant}
          setIndum={setIndum}
          setBici={setBici}/>

        </div>
        <div className="col-7">
          {/*exclusive div 4 text inputs*/}
          <div className="row mx-3">
            <div className="col-12 input-group">
              <span className="input-group-text" id="inputGroup">Nombre Tienda</span>
              <input type="text" className="form-control" id="txtTienda" aria-label="searchInput" aria-describedby="inputGroup" defaultValue={name} />
            </div>
            <div className="col-12 input-group my-2">
              <span className="input-group-text" id="inputGroup">Jefe Tienda</span>
              <input type="text" className="form-control" id="txtJefe" aria-label="searchInput" aria-describedby="inputGroup" defaultValue={jefe}/>
            </div>
            <div className="col-12 input-group">
              <span className="input-group-text" id="inputGroup">Contacto</span>
              <input type="text" className="form-control" id="txtContacto" placeholder="+56 9 XXXX XXXX" aria-label="searchInput" aria-describedby="inputGroup"
              defaultValue={contacto} />
            </div>
          </div>

          {/*div 4 checks + inputs*/}
          <div className="row my-3 mx-3">
            <h4 className="col-12">Medios de Pago Disponibles</h4>
            <div className="col-4 mx-auto fs-5">
              <div className="form-check mx-auto">
                <input className="form-check-input" type="checkbox" value="" id="pagoCheck" />
                <label className="form-check-label" htmlFor="pagoCheck">
                  Tarjetas
                </label>
              </div>
              <div className="form-check mx-auto">
                <input className="form-check-input me-3" type="checkbox" value="" id="pagoCheck" />
                <label className="form-check-label" htmlFor="pagoCheck">
                  Efectivo
                </label>
              </div>
              <div className="form-check mx-auto">
                <input className="form-check-input" type="checkbox" value="" id="pagoCheck" />
                <label className="form-check-label" htmlFor="pagoCheck">
                  Transferencias
                </label>
              </div>
            </div>
          </div>

          {/*rest of info*/}
          <div className='row mx-3'>
            <div className="col-12 input-group">
              <span className="input-group-text" id="inputGroup">Mantención desde</span>
              <input type="text" className="form-control" id="txtMant" placeholder="$" aria-label="searchInput" aria-describedby="inputGroup" 
              defaultValue={mant}/>
            </div>
            <div className="col-12 input-group my-2">
              <span className="input-group-text" id="inputGroup">Indumentaria desde</span>
              <input type="text" className="form-control" id="txtIndum" placeholder="$" aria-label="searchInput" aria-describedby="inputGroup" 
              defaultValue={indum}/>
            </div>
            <div className="col-12 input-group">
              <span className="input-group-text" id="inputGroup">Bicicletas desde</span>
              <input type="text" className="form-control" id="txtBici" placeholder="$" aria-label="searchInput" aria-describedby="inputGroup" 
              defaultValue={bici}/>
            </div>

          </div>
        </div>
      </div>
    </div>
  );
}
