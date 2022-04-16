from dataclasses import dataclass
from stations_api.secret_manager import SecretsManager


@dataclass
class DBCredentials:
    host: str
    username: str
    password: str
    database: str


class Configuration:
    db_secret_name = "/weather-app/database-stations-api-creds"

    def __init__(self, secrets_manager: SecretsManager):
        creds = secrets_manager.get_secrets(self.db_secret_name)
        self.database_creds = DBCredentials(**creds)
