from stations_api.api import Api
from mangum import Mangum


def main():
    app = Api().create_app()
    return app


app = main()
handler = Mangum(app)
