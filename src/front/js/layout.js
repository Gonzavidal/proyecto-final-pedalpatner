import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";
import { BackendURL } from "./component/backendURL";

import { Home } from "./pages/home";
import { Demo } from "./pages/demo";
//import { Contacto } from "./component/Pagescontacto";
import { Contacto } from "./pages/contacto";
import { Tienda } from "./pages/Tienda";
import { Noticias } from "./pages/Noticias";
import { Eventos } from "./pages/Eventos";
import { Ayuda } from "./pages/Ayuda";
import { Single } from "./pages/single";
import injectContext from "./store/AppContext";

import { Navbar } from "./component/navbar";
import { Footer } from "./component/footer";

//create your first component
const Layout = () => {
  //the basename is used when your project is published in a subdirectory and not in the root of the domain
  // you can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
  const basename = process.env.BASENAME || "";

  if (!process.env.BACKEND_URL || process.env.BACKEND_URL == "")
    return <BackendURL />;

  return (
    <div>
      <BrowserRouter basename={basename}>
        <ScrollToTop>
          <Navbar />
          <Routes>
            <Route element={<Home />} path="/" />
            <Route element={<Home />} path="/home" />
            <Route element={<Tienda />} path="/tienda" />
            <Route element={<Noticias />} path="/noticias" />
            <Route element={<Eventos />} path="/eventos" />
            <Route element={<Contacto />} path="/contacto" />
            <Route element={<Ayuda />} path="/ayuda" />
            {<Route element={<Contacto />} path="/contacto" />}

            {/*<Route element={<Contacto />} path="/Pagescontacto" />*/}
            <Route element={<Single />} path="/single/:theid" />
            <Route element={<h1>Not found!</h1>} />
          </Routes>
          <Footer />
        </ScrollToTop>
      </BrowserRouter>
    </div>
  );
};

export default injectContext(Layout);
