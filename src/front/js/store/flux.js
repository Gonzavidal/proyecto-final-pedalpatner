const getState = ({ getStore, getActions, setStore }) => {
  return {
    // almacen de todas la variables a utilizar en la app
    store: {
      RUTA_FLASK_API:
        "https://3001-evivanco-proyectofinalp-0j2ufapbd8a.ws-eu96b.gitpod.io",
      currentContacto: "",
      currentRegister: "",
      currentRegisterM: "",
      currenUser: "",
      username: "",
      email: "",
      password: "",
      tipos_id: "",
      roles_id: "",
      destino: "",
      direccion: "",
      titulo: "",
      descripcion: "",
      tallernom: "",
      regiontall: "",
      direcciontall: "",
      users_id: "",
      data: "",
      file: "",
      contacto: "",
      error: "",
    },
    actions: {
      //funcion generica que captura la info desde inputs
      handleChange: (e) => {
        const { name, value } = e.target;
        setStore({
          [name]: value,
        });
        console.log("all", getStore());
      },
      //funcion unica para el form de contacto
      handleSubmitContacto: (e, navigate) => {
        e.preventDefault();
        const { tipos_id, roles_id, titulo, descripcion, email, data } =
          getStore();
        if (email !== "") {
          getActions().registercomunicacion(
            {
              tipos_id,
              roles_id,
              titulo,
              email,
              descripcion,
              data,
            },
            navigate
          );
        }
      },
      registercomunicacion: (dataUser1, navigate) => {
        const { RUTA_FLASK_API } = getStore();
        const options = {
          method: "POST",
          body: JSON.stringify(dataUser1),
          headers: {
            "Content-Type": "application/json",
          },
        };
        console.log("soy body desde flux", dataUser1);
        fetch(`${RUTA_FLASK_API}/api/register_comunicacion`, options)
          .then((response) => response.json())
          .then((data1) => {
            console.log("reg de comunicacion desde flux", data1);
            if (data1) {
              setStore({
                currentContacto: data1,
                tipos_id: "",
                roles_id: "",
                titulo: "",
                email: "",
                descripcion: "",
                data: "",
                error: null,
              });
              console.log("info de contacto", getStore().currentContacto);
              navigate("/");
              sessionStorage.setItem("currentContacto", JSON.stringify(data1));
              //(data1.status == 200)
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
      //funcion formulario registro Ciclista
      handleSubmitRegister: (e, navigate) => {
        e.preventDefault();
        const { roles_id, username, email, password } = getStore();
        if (email !== "") {
          getActions().postregisteruser(
            {
              roles_id,
              username,
              email,
              password,
            },
            navigate
          );
        }
      },
      postregisteruser: (dataUser2, navigate) => {
        const { RUTA_FLASK_API } = getStore();
        const options = {
          method: "POST",
          body: JSON.stringify(dataUser2),
          headers: {
            "Content-Type": "application/json",
          },
        };
        fetch(`${RUTA_FLASK_API}/api/registeruser`, options)
          .then((response) => response.json())
          .then((data1) => {
            if (data1) {
              setStore({
                currentRegister: data1,
                roles_id: "",
                username: "",
                email: "",
                password: "",
                error: null,
              });
              console.log("registro ciclista", getStore().currentRegister);
              sessionStorage.setItem("currentRegister", JSON.stringify(data1));
              navigate("/");
            } else {
              setStore({
                currentRegister: null,
                error: data1,
              });
            }
            if (sessionStorage.getItem("currentRegister"))
              sessionStorage.removeItem("currentRegister");
          })
          .catch((error) => console.log(error));
      },
      //funcion formulario registro Mecanico
      handleSubmitRegisterM: (e, navigate) => {
        e.preventDefault();
        const {
          roles_id,
          username,
          email,
          password,
          tallernom,
          regiontall,
          direcciontall,
        } = getStore();

        if (email !== "") {
          getActions().postregistermecanico(
            {
              roles_id,
              username,
              email,
              password,
              tallernom,
              regiontall,
              direcciontall,
              // users_id
            },
            navigate
          );
        }
      },
      postregistermecanico: (dataUser3, navigate) => {
        const { RUTA_FLASK_API } = getStore();
        const options = {
          method: "POST",
          body: JSON.stringify(dataUser3),
          headers: {
            "Content-Type": "application/json",
          },
        };
        fetch(`${RUTA_FLASK_API}/api/registermecanico`, options)
          .then((response) => response.json())
          .then((data1) => {
            console.log("reg de mecanico:", data1);

            if (data1) {
              setStore({
                currentRegisterM: data1,
                roles_id: "",
                username: "",
                email: "",
                password: "",
                tallernom: "",
                regiontall: "",
                direcciontall: "",
                //users_id,
                error: null,
              });
              sessionStorage.setItem("currentRegisterM", JSON.stringify(data1));
              navigate("/");
            } else {
              setStore({
                currentRegisterM: null,
                error: data1,
              });
            }
            if (sessionStorage.getItem("currentRegisterM"))
              sessionStorage.removeItem("currentRegisterM");
          })
          .catch((error) => console.log(error));
      },
      //Acceso y validacion de ususrio
      login: async (e, navigate) => {
        e.preventDefault();
        try {
          const { email, password, RUTA_FLASK_API } = getStore();

          const options = {
            method: "POST",
            body: JSON.stringify({ email, password }),
            headers: {
              "Content-Type": "application/json",
            },
          };

          const response = await fetch(`${RUTA_FLASK_API}/api/login`, options);

          const data = await response.json();

          console.log(data);

          if (data.status === 200) {
            setStore({
              currentUser: data,
              email: "",
              password: "",
              error: null,
            });
            sessionStorage.setItem("currentUser", JSON.stringify(data));
            navigate("/tienda");
          } else {
            setStore({ error: data, currentUser: null });
            navigate("/login");
          }
        } catch (error) {
          console.log(error);
        }
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
