# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AmlSuspicion"]


class AmlSuspicion(BaseModel):
    caption: Optional[str] = None
    """Human-readable description or title for the suspicious finding."""

    checked: Optional[bool] = None
    """Indicates whether this suspicion has been manually reviewed or confirmed."""

    relation: Optional[str] = None
    """
    Nature of the relationship between the entity and the suspicious activity (e.g.,
    "linked", "associated").
    """

    schema_: Optional[str] = FieldInfo(alias="schema", default=None)
    """Version of the evaluation schema or rule engine used."""

    score: Optional[float] = None
    """Risk score between 0.0 and 1.0 indicating the severity of the suspicion."""

    source: Optional[str] = None
    """URL identifying the source system or service providing this suspicion."""

    type: Optional[Literal["Watchlist", "PEP", "Sanctions", "RiskyEntity", "Crime"]] = None
    """Watchlist category associated with the suspicion.

    Possible values include Watchlist types like "PEP", "Sanctions", "RiskyEntity",
    or "Crime".
    """
