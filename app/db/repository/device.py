from sqlalchemy.orm import Session

from app.db.models.device import Device
from typing import Type


class DeviceRepository:
    def __init__(self, db: Session):
        self._db = db

    def get_device(self, name: str) -> Type[Device] | None:
        device = self._db.query(Device).filter(Device.name == name).first()

        if device:
            return device

    def post_device(self, name: str) -> Device:
        device = Device(name=name)

        self._db.add(device)
        self._db.commit()
        self._db.flush()

        return device

    def delete_device(self, name: str) -> Type[Device] | None:
        device = self._db.query(Device).filter(Device.name == name).first()

        if device:
            self._db.delete(device)
            self._db.commit()
            self._db.flush()

            return device
