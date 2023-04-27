import React, { useContext } from "react";
import { Context } from "../store/AppContext";
import Contacto from "../component/contacto";

const Pagescontacto = () => {
  const { store, actions } = useContext(Context);
  return <Contacto />;
};

export default Pagescontacto;
