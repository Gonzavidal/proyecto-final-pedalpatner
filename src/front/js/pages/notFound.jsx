export default function notFound() {
    return (
        <div className="container-fluid text-center">
                <div className="col-12 mb-5">
                    <h3 className="display-6 ">¿No puedes visualizar esta página?</h3>
                    <h5 className="text-danger" href="/">Esta página no está disponible </h5>
                </div>
                <div className="col-12 mt-5">
                    <h3 className="display-6 ">Para más información, haz click
                    <a className="text-danger" href="/"> acá</a>.</h3>
                </div>
            </div>
    );
};