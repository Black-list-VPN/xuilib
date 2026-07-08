from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_panel_api_server_scan_reality_target_body import PostPanelApiServerScanRealityTargetBody
from ...models.post_panel_api_server_scan_reality_target_response_200 import (
    PostPanelApiServerScanRealityTargetResponse200,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PostPanelApiServerScanRealityTargetBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/panel/api/server/scanRealityTarget",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostPanelApiServerScanRealityTargetResponse200 | None:
    if response.status_code == 200:
        response_200 = PostPanelApiServerScanRealityTargetResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostPanelApiServerScanRealityTargetResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiServerScanRealityTargetBody,
) -> Response[PostPanelApiServerScanRealityTargetResponse200]:
    """Run a live TLS 1.3 probe against a candidate REALITY target and return a feasibility verdict (TLS
    1.3 + h2 + X25519 + trusted certificate) plus the certificate SAN DNS names.

    Args:
        body (PostPanelApiServerScanRealityTargetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPanelApiServerScanRealityTargetResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiServerScanRealityTargetBody,
) -> PostPanelApiServerScanRealityTargetResponse200 | None:
    """Run a live TLS 1.3 probe against a candidate REALITY target and return a feasibility verdict (TLS
    1.3 + h2 + X25519 + trusted certificate) plus the certificate SAN DNS names.

    Args:
        body (PostPanelApiServerScanRealityTargetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPanelApiServerScanRealityTargetResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiServerScanRealityTargetBody,
) -> Response[PostPanelApiServerScanRealityTargetResponse200]:
    """Run a live TLS 1.3 probe against a candidate REALITY target and return a feasibility verdict (TLS
    1.3 + h2 + X25519 + trusted certificate) plus the certificate SAN DNS names.

    Args:
        body (PostPanelApiServerScanRealityTargetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPanelApiServerScanRealityTargetResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiServerScanRealityTargetBody,
) -> PostPanelApiServerScanRealityTargetResponse200 | None:
    """Run a live TLS 1.3 probe against a candidate REALITY target and return a feasibility verdict (TLS
    1.3 + h2 + X25519 + trusted certificate) plus the certificate SAN DNS names.

    Args:
        body (PostPanelApiServerScanRealityTargetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPanelApiServerScanRealityTargetResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
