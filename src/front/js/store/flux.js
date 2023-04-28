const getState = ({ getStore, getActions, setStore }) => {
  return {
    // almacen de todas la variables a utilizar en la app
    store: {
      RUTA_FLASK_API:
        "https://3001-evivanco-proyectofinalp-0j2ufapbd8a.ws-eu96.gitpod.io",
      currentContacto: "",
      currenUser: "",
      username: "",
      email: "",
      password: "",
      tipos_id: "",
      destino: "",
      titulo: "",
      descripcion: "",
      data: "",
      contacto: "",
      error: "",
    },
    actions: {
      //funcion generica que captura la info desde inputs
      handleChange: (e) => {
        const { value } = e.target;
        setStore({
          value,
        });
        console.log("all", getStore());
      },
      //funcion unica para el form de contacto
      handleSubmitContacto: (e) => {
        e.preventDefault();
        //tengo dudas para capturar los radios pero deben ser si o si "tipos" -> radio1 (evento,noticia,menss)
        // radio2 es rol o "destino" (mecanico,ciclista) tipos_id + destino, son las variables referenciadas en flask
        const { tipos_id, destino, titulo, descripcion, email, data } =
          getStore();
        if (email !== "") {
          getActions().register_comunicacion({
            tipos_id,
            destino,
            titulo,
            email,
            descripcion,
            data,
          });
        }
      },
      //function 4 login
      handleSubmitLogin: (e) => {
        e.preventDefault();
        const { email, password } = getStore();
        if (email != "" && password != "") {
          getActions().register_login({
            email,
            password,
          });
        }
      },
      register_login: (dataUser, navigate) => {
        const { RUTA_FLASK_API } = getStore();
        const options = {
          method: "POST",
          body: JSON.stringify(dataUser),
          headers: {
            "Content-Type": "application/json",
          },
        };
        fetch(`${RUTA_FLASK_API}/api/login`, options)
          .then((response) => response.json())
          .then((data1) => {
            console.log(data1);
            if (data1) {
              setStore({ data1 });
              sessionStorage.setItem("token", "access-token");
              navigate("/");
            }
          });
      },
      // esta funcion registra la data desde el formulario y la agrega a la BD
      register_comunicacion: (dataUser, navigate) => {
        const { RUTA_FLASK_API } = getStore();
        const options = {
          method: "POST",
          body: JSON.stringify(dataUser),
          headers: {
            "Content-Type": "application/json",
          },
        };
        fetch(`${RUTA_FLASK_API}/api/register_comunicacion`, options)
          .then((response) => response.json())
          .then((data1) => {
            console.log(data1);

            if (data1) {
              setStore({
                currentContacto: data1,
                tipos_id: "",
                destino: "",
                titulo: "",
                email: "",
                descripcion: "",
                data: "",
                error: null,
              });
              sessionStorage.setItem("token", "access-token");
              navigate("/");
            } else {
              setStore({
                currentContacto: null,
                error: data1,
              });
              if (sessionStorage.getItem("currentContacto"))
                sessionStorage.removeItem("currentContacto");
            }
          })
          .catch((error) => console.log(error));
      },
      // Con esta funcion logramos mostrar al user la info de Contacto
      getComunicacion: () => {
        const { currentContacto, REACT_APP_URI } = getStore();

        fetch(`${REACT_APP_URI}/api/getcomunicacion`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${currentContacto?.access_token}`,
          },
        })
          .then((response) => response.json())
          .then((dataCont) => {
            setStore({
              contacto: dataCont,
            });
          });
      },

      logout: () => {
        sessionStorage.removeItem("token");
        setStore({ token: "" });
      },
    },
  };
};

export default getState;
