# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ...types import individual_list_params, individual_create_params
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
from ...types.individual import Individual
from ...types.individual_list_response import IndividualListResponse

__all__ = ["IndividualsResource", "AsyncIndividualsResource"]


class IndividualsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IndividualsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/dataleon-python#accessing-raw-response-data-eg-headers
        """
        return IndividualsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndividualsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/dataleon-python#with_streaming_response
        """
        return IndividualsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        workspace_id: str,
        person: individual_create_params.Person | NotGiven = NOT_GIVEN,
        source_id: str | NotGiven = NOT_GIVEN,
        technical_data: individual_create_params.TechnicalData | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Individual:
        """
        Create a new individual

        Args:
          workspace_id: Unique identifier of the workspace where the individual is being registered.

          person: Personal information about the individual.

          source_id: Optional identifier for tracking the source system or integration from your
              system.

          technical_data: Technical metadata related to the request or processing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/individuals",
            body=maybe_transform(
                {
                    "workspace_id": workspace_id,
                    "person": person,
                    "source_id": source_id,
                    "technical_data": technical_data,
                },
                individual_create_params.IndividualCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Individual,
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
    ) -> IndividualListResponse:
        """
        Get all individuals

        Args:
          end_date: Filter individuals created before this date (format YYYY-MM-DD)

          limit: Number of results to return (between 1 and 100)

          offset: Number of results to offset (must be ≥ 0)

          source_id: Filter by source ID

          start_date: Filter individuals created after this date (format YYYY-MM-DD)

          state: Filter by individual status (must be one of the allowed values)

          status: Filter by individual status (must be one of the allowed values)

          workspace_id: Filter by workspace ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/individuals",
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
                    individual_list_params.IndividualListParams,
                ),
            ),
            cast_to=IndividualListResponse,
        )


class AsyncIndividualsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIndividualsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/dataleon-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndividualsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndividualsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/dataleon-python#with_streaming_response
        """
        return AsyncIndividualsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        workspace_id: str,
        person: individual_create_params.Person | NotGiven = NOT_GIVEN,
        source_id: str | NotGiven = NOT_GIVEN,
        technical_data: individual_create_params.TechnicalData | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Individual:
        """
        Create a new individual

        Args:
          workspace_id: Unique identifier of the workspace where the individual is being registered.

          person: Personal information about the individual.

          source_id: Optional identifier for tracking the source system or integration from your
              system.

          technical_data: Technical metadata related to the request or processing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/individuals",
            body=await async_maybe_transform(
                {
                    "workspace_id": workspace_id,
                    "person": person,
                    "source_id": source_id,
                    "technical_data": technical_data,
                },
                individual_create_params.IndividualCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Individual,
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
    ) -> IndividualListResponse:
        """
        Get all individuals

        Args:
          end_date: Filter individuals created before this date (format YYYY-MM-DD)

          limit: Number of results to return (between 1 and 100)

          offset: Number of results to offset (must be ≥ 0)

          source_id: Filter by source ID

          start_date: Filter individuals created after this date (format YYYY-MM-DD)

          state: Filter by individual status (must be one of the allowed values)

          status: Filter by individual status (must be one of the allowed values)

          workspace_id: Filter by workspace ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/individuals",
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
                    individual_list_params.IndividualListParams,
                ),
            ),
            cast_to=IndividualListResponse,
        )


class IndividualsResourceWithRawResponse:
    def __init__(self, individuals: IndividualsResource) -> None:
        self._individuals = individuals

        self.create = to_raw_response_wrapper(
            individuals.create,
        )
        self.list = to_raw_response_wrapper(
            individuals.list,
        )


class AsyncIndividualsResourceWithRawResponse:
    def __init__(self, individuals: AsyncIndividualsResource) -> None:
        self._individuals = individuals

        self.create = async_to_raw_response_wrapper(
            individuals.create,
        )
        self.list = async_to_raw_response_wrapper(
            individuals.list,
        )


class IndividualsResourceWithStreamingResponse:
    def __init__(self, individuals: IndividualsResource) -> None:
        self._individuals = individuals

        self.create = to_streamed_response_wrapper(
            individuals.create,
        )
        self.list = to_streamed_response_wrapper(
            individuals.list,
        )


class AsyncIndividualsResourceWithStreamingResponse:
    def __init__(self, individuals: AsyncIndividualsResource) -> None:
        self._individuals = individuals

        self.create = async_to_streamed_response_wrapper(
            individuals.create,
        )
        self.list = async_to_streamed_response_wrapper(
            individuals.list,
        )
