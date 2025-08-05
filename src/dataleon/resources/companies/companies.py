# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ...types import company_list_params, company_create_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.company_registration import CompanyRegistration
from ...types.company_list_response import CompanyListResponse

__all__ = ["CompaniesResource", "AsyncCompaniesResource"]


class CompaniesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/dataleon-python#accessing-raw-response-data-eg-headers
        """
        return CompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/dataleon-python#with_streaming_response
        """
        return CompaniesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company: company_create_params.Company,
        workspace_id: str,
        source_id: str | NotGiven = NOT_GIVEN,
        technical_data: company_create_params.TechnicalData | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyRegistration:
        """
        Create a new company

        Args:
          company: Main information about the company being registered.

          workspace_id: Unique identifier of the workspace in which the company is being created.

          source_id: Optional identifier to track the origin of the request or integration from your
              system.

          technical_data: Technical metadata and callback configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/companies",
            body=maybe_transform(
                {
                    "company": company,
                    "workspace_id": workspace_id,
                    "source_id": source_id,
                    "technical_data": technical_data,
                },
                company_create_params.CompanyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyRegistration,
        )

    def list(
        self,
        *,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        source_id: str | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        state: Literal["VOID", "WAITING", "STARTED", "RUNNING", "PROCESSED", "FAILED", "ABORTED", "EXPIRED", "DELETED"]
        | NotGiven = NOT_GIVEN,
        status: Literal["rejected", "need_review", "approved"] | NotGiven = NOT_GIVEN,
        workspace_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyListResponse:
        """
        Get all companies

        Args:
          end_date: Filter companies created before this date (format YYYY-MM-DD)

          limit: Number of results to return (between 1 and 100)

          offset: Number of results to skip (must be ≥ 0)

          source_id: Filter by source ID

          start_date: Filter companies created after this date (format YYYY-MM-DD)

          state: Filter by company state (must be one of the allowed values)

          status: Filter by individual status (must be one of the allowed values)

          workspace_id: Filter by workspace ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/companies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "limit": limit,
                        "offset": offset,
                        "source_id": source_id,
                        "start_date": start_date,
                        "state": state,
                        "status": status,
                        "workspace_id": workspace_id,
                    },
                    company_list_params.CompanyListParams,
                ),
            ),
            cast_to=CompanyListResponse,
        )


class AsyncCompaniesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/dataleon-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/dataleon-python#with_streaming_response
        """
        return AsyncCompaniesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company: company_create_params.Company,
        workspace_id: str,
        source_id: str | NotGiven = NOT_GIVEN,
        technical_data: company_create_params.TechnicalData | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyRegistration:
        """
        Create a new company

        Args:
          company: Main information about the company being registered.

          workspace_id: Unique identifier of the workspace in which the company is being created.

          source_id: Optional identifier to track the origin of the request or integration from your
              system.

          technical_data: Technical metadata and callback configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/companies",
            body=await async_maybe_transform(
                {
                    "company": company,
                    "workspace_id": workspace_id,
                    "source_id": source_id,
                    "technical_data": technical_data,
                },
                company_create_params.CompanyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyRegistration,
        )

    async def list(
        self,
        *,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        source_id: str | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        state: Literal["VOID", "WAITING", "STARTED", "RUNNING", "PROCESSED", "FAILED", "ABORTED", "EXPIRED", "DELETED"]
        | NotGiven = NOT_GIVEN,
        status: Literal["rejected", "need_review", "approved"] | NotGiven = NOT_GIVEN,
        workspace_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyListResponse:
        """
        Get all companies

        Args:
          end_date: Filter companies created before this date (format YYYY-MM-DD)

          limit: Number of results to return (between 1 and 100)

          offset: Number of results to skip (must be ≥ 0)

          source_id: Filter by source ID

          start_date: Filter companies created after this date (format YYYY-MM-DD)

          state: Filter by company state (must be one of the allowed values)

          status: Filter by individual status (must be one of the allowed values)

          workspace_id: Filter by workspace ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/companies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "limit": limit,
                        "offset": offset,
                        "source_id": source_id,
                        "start_date": start_date,
                        "state": state,
                        "status": status,
                        "workspace_id": workspace_id,
                    },
                    company_list_params.CompanyListParams,
                ),
            ),
            cast_to=CompanyListResponse,
        )


class CompaniesResourceWithRawResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.create = to_raw_response_wrapper(
            companies.create,
        )
        self.list = to_raw_response_wrapper(
            companies.list,
        )


class AsyncCompaniesResourceWithRawResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.create = async_to_raw_response_wrapper(
            companies.create,
        )
        self.list = async_to_raw_response_wrapper(
            companies.list,
        )


class CompaniesResourceWithStreamingResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.create = to_streamed_response_wrapper(
            companies.create,
        )
        self.list = to_streamed_response_wrapper(
            companies.list,
        )


class AsyncCompaniesResourceWithStreamingResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.create = async_to_streamed_response_wrapper(
            companies.create,
        )
        self.list = async_to_streamed_response_wrapper(
            companies.list,
        )
