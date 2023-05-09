import React, { useEffect, useState } from 'react'
import { GoogleMap, useJsApiLoader, Marker, InfoWindow } from '@react-google-maps/api';

const containerStyle = {
  width: '600px',
  height: '450px'
};

const center = { lat: -33.742145, lng: -70.735680 };

const position = { lat: -33.41611624894014, lng: -70.53850224009655 } // -33.41611624894014, -70.53850224009655
const position2 = { lat: -33.41692893716737, lng: -70.53828229896085 } // -33.41692893716737, -70.53828229896085
const position3 = { lat: -33.41729833839787, lng: -70.53743203871521 } // -33.41729833839787, -70.53743203871521

const divStyle = {
  background: `white`,
}

function Maps({ setName, setJefe, setContacto, setMant, setIndum, setBici, setEfect, setTransf, setTarjetas}) {

  const [currentPosition, setCurrentPosition] = useState(
    { latitud: null, longitud: null }

  )

  
  
  const [infoWindowOpen, setInfowindowOpen] = useState(false);

  const [content, setContent] = useState(
    <h1>Hola</h1>
  )

  useEffect(() => {
    navigator.geolocation.getCurrentPosition(function (position) {
      setCurrentPosition({ lat: position.coords.latitude, lng: position.coords.longitude });
    });
  }, [])

  

  function infoWindowOpenShow(position, info, name, jefe, contacto, mant, indum, bici, efect, transf, tarjetas) {
    setInfowindowOpen(true)
    setCurrentPosition({ lat: position.lat, lng: position.lng });
    setContent(<p>{info}</p>);
    setName(name);
    setJefe(jefe);
    setContacto(contacto);
    setMant(mant);
    setIndum(indum);
    setBici(bici);
    setEfect(efect);
    setTransf(transf);
    setTarjetas(tarjetas);


    console.log("hola")
  }

  console.log(currentPosition)

  const { isLoaded } = useJsApiLoader({
    id: 'google-map-script',
    googleMapsApiKey: "key=AIzaSyBACfURyt2puQfsUqji6npYqMzPKoeRdIQ"
  })

  const [map, setMap] = React.useState(null)

  const onLoad = React.useCallback(function callback(map) {
    const bounds = new window.google.maps.LatLngBounds(center);
    setMap(map)
  }, [])

  const onUnmount = React.useCallback(function callback(map) {
    setMap(null)
  }, [])

  return isLoaded ? (
    <>
      <GoogleMap
        mapContainerStyle={containerStyle}
        center={currentPosition}
        zoom={18} // 
        onUnmount={onUnmount}

      >
        <Marker
          
          onLoad={onLoad}
          position={position}
          onClick={() => infoWindowOpenShow(position, "Colon Bikes", "Colon Bikes", "Gonzalo Vidal", "+56 9 5555 5555", "10.000", "15.000", "150.000", "Si", "No", "No",)}
        />
        <Marker
          
          onLoad={onLoad}
          position={position2}
          onClick={() => infoWindowOpenShow(position2, "Francisco's Bike", "Francisco's Bike", "Francisco Krugger", "+56 9 6666 6666", "8.000", "13.000", "180.000", "Si", "No", "No",)}
        />
        <Marker
          onLoad={onLoad}
          position={position3}
          onClick={() => infoWindowOpenShow(position3, "Richard's Bike", "Richard's Bike", "Richard Tapia", "+56 9 7777 7777", "12.000", "12.000", "170.000", "Si", "Si", "Si",)}
        />

        {infoWindowOpen &&
          (<InfoWindow
            onCloseClick={() => setInfowindowOpen(false)}
            onLoad={onLoad}
            position={currentPosition}
          >
            <div style={divStyle}>
              {content}
            </div>
          </InfoWindow>)
        }
      </GoogleMap>
    </>
  ) : <></>
}

export default React.memo(Maps)