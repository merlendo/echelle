import sqlalchemy

from .config import config


def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


if __debug__:
    sqlalchemy.event.listens_for(sqlalchemy.Engine, "connect")(set_sqlite_pragma)


url = sqlalchemy.URL.create(
    drivername=config.get("database.driver"),
    username=config.get("database.username"),
    password=config.get("database.password"),
    host=config.get("database.host"),
    port=config.get("database.port"),
    database=config.get("database.database"),
    query=config.get("database.query"),
)
engine = sqlalchemy.create_engine(url)
