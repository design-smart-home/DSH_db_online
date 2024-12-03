from pydantic import BaseModel
import uuid


class GetDeviceRequest(BaseModel):
    name: str


class GetDeviceResponse(BaseModel):
    device_id: uuid.UUID
    name: str


class PostDeviceRequest(BaseModel):
    name: str


class PostDeviceResponse(BaseModel):
    device_id: uuid.UUID
    name: str


class DeleteDeviceRequest(BaseModel):
    name: str


class DeleteDeviceResponse(BaseModel):
    device_id: uuid.UUID
    name: str
