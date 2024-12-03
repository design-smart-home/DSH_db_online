from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.schemas.device import (
    GetDeviceResponse,
    PostDeviceRequest,
    PostDeviceResponse,
    DeleteDeviceRequest,
    DeleteDeviceResponse,
)
from app.api.core.device import (
    delete_device_by_name,
    get_device_by_name,
    post_device_,
)


device_router = APIRouter()


@device_router.get("/")
def get_device(name: str, db: Session = Depends(get_db)) -> GetDeviceResponse:
    device = get_device_by_name(name, session=db)

    if not device:
        raise HTTPException(status_code=404, detail=f"Device by name {name} not found")

    return GetDeviceResponse(
        device_id=device.device_id,
        name=device.name,
    )


@device_router.post("/")
def post_device(
    body: PostDeviceRequest, db: Session = Depends(get_db)
) -> PostDeviceResponse:
    device = post_device_(body.name, session=db)

    if not device:
        raise HTTPException(status_code=400, detail="Unknown error")

    return PostDeviceResponse(
        device_id=device.device_id,
        name=device.name,
    )


@device_router.delete("/")
def delete_device(
    body: DeleteDeviceRequest, db: Session = Depends(get_db)
) -> DeleteDeviceResponse:
    device = delete_device_by_name(body.name, session=db)

    if not device:
        raise HTTPException(
            status_code=404, detail=f"Device with {body.name} not found"
        )

    return DeleteDeviceResponse(
        device_id=device.device_id,
        name=device.name,
    )
