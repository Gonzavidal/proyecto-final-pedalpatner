const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      RUTA_FLASK_API:
        "https://3001-evivanco-proyectofinalp-0j2ufapbd8a.ws-eu95.gitpod.io",
      currentContacto: null,
      currenUser: null,
      username: null,
      email: null,
      password: null,
      tipos_id: null,
      destino: null,
      titulo: null,
      descripcion: null,
      data: null,
      error: null,
    },
    actions: {
      handleChange: (e) => {
        const { name, value } = e.target;
        setStore({
          [name]: value,
        });
        console.log("all", getStore());
      },

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
              sessionStorage.setItem("currentContacto", JSON.stringify(data1));
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
    },
  };
};

export default getState;
