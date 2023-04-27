const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      RUTA_FLASK_API:
        "https://3001-evivanco-proyectofinalp-0j2ufapbd8a.ws-eu95.gitpod.io",
      currenUser: null,
      username: null,
      email: null,
      password: null,
      radio1: null,
      radio2: null,
      titulo: null,
      descripcion: null,
      file: null,
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
    },
  };
};

export default getState;
