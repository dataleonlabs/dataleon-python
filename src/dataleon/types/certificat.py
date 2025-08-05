# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Certificat"]


class Certificat(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the certificate."""

    created_at: Optional[datetime] = None
    """Timestamp when the certificate was created."""

    filename: Optional[str] = None
    """Name of the certificate file."""
