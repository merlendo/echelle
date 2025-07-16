import sqlalchemy

from .config import config

url = sqlalchemy.URL.create(drivername=config.get("database.driver"),
                 username=config.get("database.username"),
                 password=config.get("database.password"),
                 host=config.get("database.host"),
                 port=config.get("database.port"),
                 database=config.get("database.database"),
                 query=config.get("database.query"))
engine = sqlalchemy.create_engine(url)

