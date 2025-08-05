# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["TechnicalData"]


class TechnicalData(BaseModel):
    api_version: Optional[int] = None
    """Version number of the API used."""

    approved_at: Optional[datetime] = None
    """Timestamp when the request or process was approved."""

    callback_url: Optional[str] = None
    """URL to receive callback data from the AML system."""

    callback_url_notification: Optional[str] = None
    """URL to receive notification updates about the processing status."""

    disable_notification: Optional[bool] = None
    """Flag to indicate if notifications are disabled."""

    disable_notification_date: Optional[datetime] = None
    """Timestamp when notifications were disabled; null if never disabled."""

    export_type: Optional[str] = None
    """Export format defined by the API (e.g., "json", "xml")."""

    finished_at: Optional[datetime] = None
    """Timestamp when the process finished."""

    ip: Optional[str] = None
    """IP address of the our system handling the request."""

    language: Optional[str] = None
    """Language preference used in the client workspace (e.g., "fra")."""

    location_ip: Optional[str] = None
    """IP address of the end client (final user) captured."""

    need_review_at: Optional[datetime] = None
    """Timestamp indicating when the request or process needs review; null if none."""

    notification_confirmation: Optional[bool] = None
    """Flag indicating if notification confirmation is required or received."""

    qr_code: Optional[str] = None
    """Indicates whether QR code is enabled ("true" or "false")."""

    raw_data: Optional[bool] = None
    """Flag indicating whether to include raw data in the response."""

    rejected_at: Optional[datetime] = None
    """Timestamp when the request or process was rejected; null if not rejected."""

    started_at: Optional[datetime] = None
    """Timestamp when the process started."""

    transfer_at: Optional[datetime] = None
    """Date/time of data transfer."""

    transfer_mode: Optional[str] = None
    """Mode of data transfer."""
