from sqlalchemy.orm import Session

from app.db.models.widget import Widget
from typing import Type, List
import uuid


class WidgetRepository:
    def __init__(self, db: Session):
        self._db = db

    def get_widget(self, widget_id: uuid.UUID) -> Type[Widget] | None:
        widget = self._db.query(Widget).filter(Widget.widget_id == widget_id).first()

        if widget:
            return widget

    def post_widget(
        self,
        user_id: uuid.UUID | str | None,
        device_id: uuid.UUID | str | None,
        type_widget: str,
        current_value: int,
        name: str,
    ) -> Widget:
        widget = Widget(
            user_id=user_id,
            device_id=device_id,
            type_widget=type_widget,
            current_value=current_value,
            name=name,
        )

        self._db.add(widget)
        self._db.commit()
        self._db.flush()

        return widget

    def delete_widget(self, widget_id: uuid.UUID) -> Type[Widget] | None:
        widget = self._db.query(Widget).filter(Widget.widget_id == widget_id).first()

        if widget:
            self._db.delete(widget)
            self._db.commit()
            self._db.flush()

            return widget

    def update_widget(
            self,
            widget_id: uuid.UUID,
            device_id: uuid.UUID | None = None,
            type_widget: str | None = None,
            current_value: int | None = None,
            name: str | None = None,
    ) -> None:
        widget = self._db.query(Widget).filter(Widget.widget_id == widget_id).first()
        if not widget:
            raise Exception(f"Widget with id {widget_id} not found")

        if device_id:
            widget.device_id = device_id
        if type_widget:
            widget.type_widget = type_widget
        if current_value:
            widget.current_value = current_value
        if name:
            widget.name = name

        self._db.commit()
        self._db.flush()
