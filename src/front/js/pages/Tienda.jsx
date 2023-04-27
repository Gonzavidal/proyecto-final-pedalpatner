import Maps from './Maps';



export default function Comunidad() {
  return (
    <div className="container-fluid text-center position-relative d-inline-block">
      <h1>Encuentra tu tienda</h1>
      <hr className="hr" />

      <div className="row">
        <div className="col-6 px-5">
        <Maps/>
        </div>

        <div className="col-6 px-4">
          {/*exclusive div 4 text inputs*/}
          <div className="row">
            <div className="col-12 input-group">
              <span className="input-group-text" id="inputGroup">Nombre Tienda</span>
              <input type="text" className="form-control" aria-label="searchInput" aria-describedby="inputGroup" />
            </div>
            <div className="col-12 input-group my-3">
              <span className="input-group-text" id="inputGroup">Jefe Tienda</span>
              <input type="text" className="form-control" aria-label="searchInput" aria-describedby="inputGroup" />
            </div>
            <div className="col-12 input-group">
              <span className="input-group-text" id="inputGroup">Contacto</span>
              <input type="text" className="form-control" placeholder="+56 9 XXXX XXXX" aria-label="searchInput" aria-describedby="inputGroup" />
            </div>
          </div>

          {/*div 4 checks + inputs*/}
          <div className="row my-3">
            <h4 className="col-12">Medios de Pago Disponibles</h4>
            <div className="col-4 mx-auto fs-5">
              <div className="form-check mx-auto">
                <input className="form-check-input" type="checkbox" value="" id="pagoCheck" />
                <label className="form-check-label" for="pagoCheck">
                  Tarjetas
                </label>
              </div>
              <div className="form-check mx-auto">
                <input className="form-check-input me-3" type="checkbox" value="" id="pagoCheck" />
                <label className="form-check-label" for="pagoCheck">
                  Efectivo
                </label>
              </div>
              <div className="form-check mx-auto">
                <input className="form-check-input" type="checkbox" value="" id="pagoCheck" />
                <label className="form-check-label" for="pagoCheck">
                  Transferencias
                </label>
              </div>
            </div>
          </div>

          {/*rest of info*/}
          <div className='row'>
            <div className="col-12 input-group">
              <span className="input-group-text" id="inputGroup">Mantención desde</span>
              <input type="text" className="form-control" placeholder="$" aria-label="searchInput" aria-describedby="inputGroup" />
            </div>
            <div className="col-12 input-group my-3">
              <span className="input-group-text" id="inputGroup">Indumentaria desde</span>
              <input type="text" className="form-control" placeholder="$" aria-label="searchInput" aria-describedby="inputGroup" />
            </div>
            <div className="col-12 input-group">
              <span className="input-group-text" id="inputGroup">Bicicletas desde</span>
              <input type="text" className="form-control" placeholder="$" aria-label="searchInput" aria-describedby="inputGroup" />
            </div>
          </div>
        </div>
      </div>
    </div>



  );
}
