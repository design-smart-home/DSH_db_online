from typing import Generator

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql://postgres:postgres@localhost:5435/shm_db_api_devices"
)
_session = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)


def get_db() -> Generator[Session]:
    try:
        session: Session = _session()
        yield session
    finally:
        session.close()
