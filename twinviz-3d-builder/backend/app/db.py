import sqlalchemy
from databases import Database
from .core.config import settings

database = Database(settings.DATABASE_URL)
metadata = sqlalchemy.MetaData()

projects = sqlalchemy.Table(
    'projects',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('filename', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('content_type', sqlalchemy.String, nullable=True),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
)
engine = sqlalchemy.create_engine(str(settings.DATABASE_URL).replace('aiosqlite','sqlite'), connect_args={'check_same_thread': False} if 'sqlite' in settings.DATABASE_URL else {})
metadata.create_all(engine)
