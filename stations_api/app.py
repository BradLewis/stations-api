from mangum import Mangum
from simple_injection import ServiceCollection
from stations_api.api import Api
from stations_api.data.database_service import DatabaseService
from stations_api.data.stations_repository import StationsRepository


def configure_services():
    collection = ServiceCollection()
    collection.add_transient(Api)
    collection.add_transient(StationsRepository)
    collection.add_singleton(DatabaseService)

    return collection


def main():
    collection = configure_services()
    return collection.resolve(Api).create_app()


app = main()
handler = Mangum(app)
