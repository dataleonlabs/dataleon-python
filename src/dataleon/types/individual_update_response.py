# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .risk import Risk
from .check import Check
from .._models import BaseModel
from .property import Property
from .certificat import Certificat
from .aml_suspicion import AmlSuspicion
from .technical_data import TechnicalData
from .individuals.generic_document import GenericDocument

__all__ = ["IndividualUpdateResponse", "IdentityCard", "Person", "Tag"]


class IdentityCard(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the document."""

    back_document_signed_url: Optional[str] = None
    """Signed URL linking to the back image of the document."""

    birth_place: Optional[str] = None
    """Place of birth as indicated on the document."""

    birthday: Optional[str] = None
    """Date of birth in DD/MM/YYYY format as shown on the document."""

    country: Optional[str] = None
    """Country code issuing the document (ISO 3166-1 alpha-2)."""

    expiration_date: Optional[str] = None
    """Expiration date of the document, in YYYY-MM-DD format."""

    first_name: Optional[str] = None
    """First name as shown on the document."""

    front_document_signed_url: Optional[str] = None
    """Signed URL linking to the front image of the document."""

    gender: Optional[str] = None
    """Gender indicated on the document (e.g., "M" or "F")."""

    issue_date: Optional[str] = None
    """Date when the document was issued, in YYYY-MM-DD format."""

    last_name: Optional[str] = None
    """Last name as shown on the document."""

    mrz_line_1: Optional[str] = None
    """First line of the Machine Readable Zone (MRZ) on the document."""

    mrz_line_2: Optional[str] = None
    """Second line of the MRZ on the document."""

    mrz_line_3: Optional[str] = None
    """Third line of the MRZ if applicable; otherwise null."""

    type: Optional[str] = None
    """Type of document (e.g., passport, identity card)."""


class Person(BaseModel):
    birthday: Optional[str] = None
    """Date of birth, formatted as DD/MM/YYYY."""

    email: Optional[str] = None
    """Email address of the individual."""

    face_image_signed_url: Optional[str] = None
    """Signed URL linking to the person’s face image."""

    first_name: Optional[str] = None
    """First (given) name of the person."""

    full_name: Optional[str] = None
    """Full name of the person, typically concatenation of first and last names."""

    gender: Optional[str] = None
    """Gender of the individual (e.g., "M" for male, "F" for female)."""

    last_name: Optional[str] = None
    """Last (family) name of the person."""

    maiden_name: Optional[str] = None
    """Maiden name of the person, if applicable."""

    phone_number: Optional[str] = None
    """Contact phone number including country code."""


class Tag(BaseModel):
    key: Optional[str] = None
    """Name of the tag used to identify the metadata field."""

    private: Optional[bool] = None
    """Indicates whether the tag is private (not visible to external users)."""

    type: Optional[str] = None
    """Data type of the tag value (e.g., "string", "number", "boolean")."""

    value: Optional[str] = None
    """Value assigned to the tag."""


class IndividualUpdateResponse(BaseModel):
    id: Optional[str] = None
    """Unique identifier of the individual."""

    aml_suspicions: Optional[List[AmlSuspicion]] = None
    """List of AML (Anti-Money Laundering) suspicion entries linked to the individual."""

    auth_url: Optional[str] = None
    """URL to authenticate the individual, usually for document signing or onboarding."""

    certificat: Optional[Certificat] = None
    """Digital certificate associated with the individual, if any."""

    checks: Optional[List[Check]] = None
    """List of verification or validation checks applied to the individual."""

    created_at: Optional[datetime] = None
    """Timestamp of the individual's creation in ISO 8601 format."""

    documents: Optional[List[GenericDocument]] = None
    """All documents submitted or associated with the individual."""

    identity_card: Optional[IdentityCard] = None
    """Reference to the individual's identity document."""

    number: Optional[int] = None
    """Internal sequential number or reference for the individual."""

    person: Optional[Person] = None
    """
    Personal details of the individual, such as name, date of birth, and contact
    info.
    """

    portal_url: Optional[str] = None
    """Admin or internal portal URL for viewing the individual's details."""

    properties: Optional[List[Property]] = None
    """Custom key-value metadata fields associated with the individual."""

    risk: Optional[Risk] = None
    """Risk assessment associated with the individual."""

    source_id: Optional[str] = None
    """Optional identifier indicating the source of the individual record."""

    state: Optional[str] = None
    """
    Current operational state in the workflow (e.g., WAITING, IN_PROGRESS,
    COMPLETED).
    """

    status: Optional[str] = None
    """
    Overall processing status of the individual (e.g., rejected, need_review,
    approved).
    """

    tags: Optional[List[Tag]] = None
    """
    List of tags assigned to the individual for categorization or metadata purposes.
    """

    technical_data: Optional[TechnicalData] = None
    """Technical metadata related to the request (e.g., QR code settings, language)."""

    webview_url: Optional[str] = None
    """Public-facing webview URL for the individual’s identification process."""

    workspace_id: Optional[str] = None
    """Identifier of the workspace to which the individual belongs."""
