from app.db.base import Base
from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column
import uuid


class Device(Base):
    __tablename__ = "devices"

    device_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(20), nullable=False)


# add types device from table...
