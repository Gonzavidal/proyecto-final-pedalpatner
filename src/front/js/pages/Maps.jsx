import React, { useEffect, useState } from 'react'
import { GoogleMap, useJsApiLoader, Marker, InfoWindow } from '@react-google-maps/api';



const containerStyle = {
  width: '600px',
  height: '450px'
};

const center = { lat: -33.742145, lng: -70.735680 };



const position = { lat: -33.74200819688481, lng: -70.73546492713628 }
const position2 = { lat: -33.74255488809652, lng: -70.73545760135589 } //-33.74255488809652, -70.73545760135589
const position3 = { lat: -33.48017198625467, lng: -70.55813925950957 } //-33.48017198625467, -70.55813925950957

const divStyle = {
  background: `white`,
  border: `1px solid #ccc`,
  padding: 5
}


function Maps() {

  const [currentPosition, setCurrentPosition] = useState(
    {
      latitud: null,
      longitud: null
    }
  )

    const [infoWindowOpen, setInfowindowOpen] = useState(false);
    

  
  // const [count, setCount] = useState(0);

  useEffect(() => {
    navigator.geolocation.getCurrentPosition(function (position) {
      setCurrentPosition({ lat: position.coords.latitude, lng: position.coords.longitude });
    });
  }, [])

  function infoWindowOpenShow(){
    setInfowindowOpen(true)
    console.log("hola")
  }
  
  console.log(currentPosition)

  const { isLoaded } = useJsApiLoader({
    id: 'google-map-script',
    googleMapsApiKey: "key=AIzaSyBACfURyt2puQfsUqji6npYqMzPKoeRdIQ"
  })

  const [map, setMap] = React.useState(null)

  const onLoad = React.useCallback(function callback(map) {
    // This is just an example of getting and using the map instance!!! don't just blindly copy!
    const bounds = new window.google.maps.LatLngBounds(center);

    
    /*const onLoad = infoWindow => {
  console.log('infoWindow: ', infoWindow)
}
    }*/

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
          label={"BiciBuin"}
          onLoad={onLoad}
          position={position}
          onClick={infoWindowOpenShow}
        />
        <Marker
          label={"Francisco Bike"}
          onLoad={onLoad}
          position={position2}
          onClick={infoWindowOpenShow}

        />
        <Marker
          label={"Richard's Bike"}
          onLoad={onLoad}
          position={position3}
          onClick={infoWindowOpenShow}

        />

        {infoWindowOpen && 
        (<InfoWindow
          onCloseClick={() => setInfowindowOpen(false)}
          onLoad={onLoad}
          position={position}
        >
          <div style={divStyle}>
            <h5>BiciBuin</h5>
            <p>Gonzalo Vidal</p>
            <p>+56 9 5555 5555</p>
            <p>Efectivo</p>
            <p>Mant: 10.000</p>
            <p>Indum: 20.000</p>
            <p>Bici: 200.000</p>
          </div>
        </InfoWindow>)
        }
        

      </GoogleMap>
    </>
  ) : <></>
}

export default React.memo(Maps)