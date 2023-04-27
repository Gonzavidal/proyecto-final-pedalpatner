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
        const { id, value } = e.target;
        setStore({
          [id]: value,
        });
        console.log("all", getStore());
      },

      handleSubmitContacto: (e) => {
        e.preventDefault();
        //tengo dudas para capturar los radios pero deben ser si o si "tipos" -> radio1 (evento,noticia,menss)
        // radio2 es rol o "destino" (mecanico,ciclista) tipos_id + destino, son las variables referenciadas en flask
        const { radio1, radio2, titulo, descripcion, email, file } = getStore();
        if (email !== "") {
          getActions().register_comunicacion({
            radio1,
            radio2,
            titulo,
            email,
            descripcion,
            file,
          });
        }
      },
    },
  };
};

export default getState;
