# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import FileTypes

__all__ = ["DocumentUploadParams"]


class DocumentUploadParams(TypedDict, total=False):
    document_type: Required[
        Literal[
            "bank_statements",
            "liasse_fiscale",
            "amortised_loan_schedule",
            "accounting",
            "invoice",
            "receipt",
            "company_statuts",
            "rib",
            "livret_famille",
            "payslip",
            "carte_grise",
            "proof_address",
            "identity_document",
            "tax",
        ]
    ]
    """Filter by document type for upload (must be one of the allowed values)"""

    file: FileTypes
    """File to upload (required)"""

    url: str
    """URL of the file to upload (either `file` or `url` is required)"""
