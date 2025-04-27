from pydantic import BaseModel
import uuid


class GetWidgetResponse(BaseModel):
    widget_id: uuid.UUID
    device_id: uuid.UUID | None
    name: str
    type_widget: str


class PostWidgetRequest(BaseModel):
    device_id: uuid.UUID | None
    name: str
    type_widget: str


class PostWidgetResponse(BaseModel):
    widget_id: uuid.UUID
    device_id: uuid.UUID
    name: str
    type_widget: str
