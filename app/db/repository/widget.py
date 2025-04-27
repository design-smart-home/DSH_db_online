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
        device_id: uuid.UUID,
        type_widget: str,
        name: str,
    ) -> Widget:
        widget = Widget(
            device_id=device_id,
            type_widget=type_widget,
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
