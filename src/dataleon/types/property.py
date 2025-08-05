# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Property"]


class Property(BaseModel):
    name: Optional[str] = None
    """Name/key of the property."""

    type: Optional[str] = None
    """Data type of the property value."""

    value: Optional[str] = None
    """Value associated with the property name."""
