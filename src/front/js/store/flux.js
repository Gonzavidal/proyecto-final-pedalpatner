const getState = ({ getStore, getActions, setStore }) => {
  return {
    // almacen de todas la variables a utilizar en la app
    store: {
      RUTA_FLASK_API:
        "https://3001-gonzavidal-proyectofina-7qx28lckkka.ws-us96b.gitpod.io",
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
      archivo: null,
    },
    actions: {
      //funcion generica que captura la info desde inputs
      handleChange: (e) => {
        const { name, value, type } = e.target;
        if (type == "file") {
          let archivo = e.target.files[0];
          setStore({
            data: value,
            archivo: archivo,
          });
        } else {
          setStore({
            [name]: value,
          });
        }
        console.log(getStore()[name]);
      },
      //funcion form de contacto
      handleSubmitContacto: (e, navigate) => {
        e.preventDefault();
        const {
          tipos_id,
          roles_id,
          titulo,
          descripcion,
          email,
          users_id,
          data,
        } = getStore();
        /**
         * Si el email es igual a vacio, no se envia la comuncación, el campo email
         * es neceario para la ejecución de la fucion
         **/
        if (email !== "") {
          getActions().registercomunicacion(navigate);
        }
      },
      registercomunicacion: async (navigate) => {
        try {
          const {
            tipos_id,
            roles_id,
            titulo,
            email,
            descripcion,
            archivo,
            users_id,
            currentContacto,
            RUTA_FLASK_API,
          } = getStore();

          const formData = new FormData();
          formData.append("avatar", archivo);
          formData.append("tipos_id", tipos_id);
          formData.append("roles_id", roles_id);
          formData.append("titulo", titulo);
          formData.append("email", email);
          formData.append("descripcion", descripcion);
          formData.append("users_id", users_id); //

          const options = {
            method: "POST",
            body: formData,
            headers: {
              //"Content-Type": "application/json",
              Authorization: `Bearer ${currentContacto?.data?.access_token}`,
            },
          };

          const response = await fetch(
            `${RUTA_FLASK_API}/api/register_comunicacion`,
            options
          );

          const data = await response.json();

          const { result } = data;

          console.log("soy result", result);
          console.log("soy currentcotacto", currentContacto);

          //currentUser.data.user = result // actualizamos currentUser con la nueva informacion del usuario
          setStore({ currentContacto }); // guardamos la informacion en el store
          sessionStorage.setItem(
            "currentContacto",
            JSON.stringify(currentContacto)
          ); // actualizamos la informacion en el sessionStorage
          navigate("/ayuda");
        } catch (error) {
          console.log(error);
        }
      },

      //funcion formulario registro Ciclista
      handleSubmitRegister: (e, navigate) => {
        e.preventDefault();
        const { roles_id, username, email, password, direccion } = getStore();
        if (email !== "") {
          getActions().postregisteruser(
            {
              roles_id,
              username,
              email,
              password,
              direccion,
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
                direccion: "",
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
          direccion,
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
              direccion,
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
        const { RUTA_FLASK_API, currentRegisterM } = getStore();
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
                direccion: "",
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

      //Admin con esta funcion logramos mostrar al user la info de contacto
      getComunicacion: () => {
        const { currentContacto, RUTA_FLASK_API } = getStore();
        console.log(getStore().contacto);
        fetch(`${RUTA_FLASK_API}/api/getcomunicacion`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${currentContacto?.access_token}`,
          },
        })
          .then((response) => response.json())
          .then((dataCont) => {
            console.log("getcomunicacion_", dataCont);
            setStore({
              contacto: dataCont,
            });
          })
          .catch((e) => {
            console.log(e);
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
