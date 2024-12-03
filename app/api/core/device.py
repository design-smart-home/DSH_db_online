from app.db.models.device import Device
from app.db.repository.device import DeviceRepository
from sqlalchemy.orm import Session

from typing import Type


def get_device_by_name(name: str, session: Session) -> Type[Device] | None:
    device_repo = DeviceRepository(session)

    device = device_repo.get_device(name)

    if device:
        return device


def post_device_(name: str, session: Session) -> Device | None:
    device_repo = DeviceRepository(session)

    device = device_repo.post_device(name)

    if device:
        return device


def delete_device_by_name(name: str, session: Session) -> Type[Device] | None:
    device_repo = DeviceRepository(session)

    device = device_repo.delete_device(name)

    if device:
        return device
