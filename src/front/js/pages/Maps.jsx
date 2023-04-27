import React, { useEffect, useState } from 'react'
import { GoogleMap, useJsApiLoader, Marker } from '@react-google-maps/api';


const containerStyle = {
  width: '400px',
  height: '400px'
};

const center = { lat: -33.742145, lng: -70.735680 };


const position = { lat: -33.74200819688481, lng: -70.73546492713628 }
const position2 = { lat: -33.74255488809652, lng: -70.73545760135589 } //-33.74255488809652, -70.73545760135589


function Maps() {

  const [currentPosition, setCurrentPosition] = useState(
    {
      latitud: null ,
      longitud: null
    }
  )

  // const [count, setCount] = useState(0);

  useEffect(()=>{
    navigator.geolocation.getCurrentPosition(function(position) {
      setCurrentPosition({lat:position.coords.latitude, lng:position.coords.longitude});
    });
  },[])
  
  console.log(currentPosition)

  const { isLoaded } = useJsApiLoader({
    id: 'google-map-script',
    googleMapsApiKey: "key=AIzaSyBACfURyt2puQfsUqji6npYqMzPKoeRdIQ"
  })

  const [map, setMap] = React.useState(null)

  const onLoad = React.useCallback(function callback(map) {
    // This is just an example of getting and using the map instance!!! don't just blindly copy!
    const bounds = new window.google.maps.LatLngBounds(center);

    /*map.fitBounds(bounds);*/

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
        label= {"BiciBuin"}
        onLoad={onLoad}
        position={position}
      />
      <Marker
        label= {"BiciBuin"}
        onLoad={onLoad}
        position={position2}
      />
    </GoogleMap>
    </>
  ) : <></>
}

export default React.memo(Maps)