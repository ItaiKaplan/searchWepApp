import yaml
from Databases.RedisDB import RedisDB

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)


def get_database():
    if config['database_type'] == 'redis':
        return RedisDB('localhost', 6379, 0)
    elif config['database_type'] == 'sqlalchemy':
        # Implement a SQLAlchemy based DB
        pass
    else:
        raise ValueError(f"Unknown database type: {config['database_type']}")

