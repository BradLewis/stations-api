import json
from typing import Dict
from botocore.client import Config
import boto3


class SecretsManager:
    def get_secrets(self, secret_name: str) -> Dict:
        config = Config(connect_timeout=5, retries={"max_attempts": 0})
        client = boto3.client("secretsmanager", config=config)
        secret = json.loads(
            client.get_secret_value(SecretId=secret_name)["SecretString"]
        )
        return secret
