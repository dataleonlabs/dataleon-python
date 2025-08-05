# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Risk"]


class Risk(BaseModel):
    code: Optional[str] = None
    """Risk category or code identifier."""

    reason: Optional[str] = None
    """Explanation or justification for the assigned risk."""

    score: Optional[float] = None
    """Numeric risk score between 0.0 and 1.0 indicating severity or confidence."""
