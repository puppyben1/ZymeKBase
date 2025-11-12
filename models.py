from __future__ import annotations
from datetime import datetime
from flask import url_for
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float, DateTime, Text, JSON
from app import db
from sqlalchemy import func


class NanoEnzyme(db.Model):
    __tablename__ = "nanoenzymes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200), index=True)
    formula: Mapped[str | None] = mapped_column(String(200), index=True, nullable=True)
    activity: Mapped[str | None] = mapped_column(String(100), index=True, nullable=True)
    substrate: Mapped[str] = mapped_column(String(200), index=True, default="")
    ph: Mapped[float | None] = mapped_column(Float, nullable=True)
    temp_c: Mapped[float | None] = mapped_column(Float, nullable=True)
    km: Mapped[float] = mapped_column(Float, nullable=True)
    vmax: Mapped[float] = mapped_column(Float, nullable=True)
    doi: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    notes: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)

    def __repr__(self) -> str:
        return f"<NanoEnzyme id={self.id} name={self.name!r}>"


class Figure(db.Model):
    __tablename__ = "figures"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200), index=True)
    tags: Mapped[str] = mapped_column(String(200), index=True, default="")
    description: Mapped[str] = mapped_column(Text, default="")
    filename: Mapped[str] = mapped_column(String(300), unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)

    @property
    def url(self) -> str:
        # expects an 'upload.uploaded_file' endpoint to serve static uploads
        return url_for("upload.uploaded_file", filename=self.filename)

    def __repr__(self) -> str:
        return f"<Figure id={self.id} title={self.title!r}>"


class UploadRequest(db.Model):
    """
    Lightweight inbox for 'Offer a sample'.
    Store the raw payload and a simple status flag for review workflow.
    """
    __tablename__ = "uploads"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    payload_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="pending", index=True)  # pending/approved/rejected
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)

    def __repr__(self) -> str:
        return f"<UploadRequest id={self.id} status={self.status!r}>"

class Viz2D(db.Model):
    __tablename__ = "viz2d"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    kind = db.Column(db.String(50), nullable=True)          # 'scatter','violin','heatmap',...
    tags = db.Column(db.String(200), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    config_json = db.Column(db.Text, nullable=True)          # future: filters/config as JSON
    image_filename = db.Column(db.String(255), nullable=True) # file saved under static/plots
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


__all__ = ["NanoEnzyme", "Figure", "UploadRequest"]
