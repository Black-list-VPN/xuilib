from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_panel_api_inbounds_all_links_response_200 import GetPanelApiInboundsAllLinksResponse200
from ...xui_types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/panel/api/inbounds/allLinks",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPanelApiInboundsAllLinksResponse200 | None:
    if response.status_code == 200:
        response_200 = GetPanelApiInboundsAllLinksResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPanelApiInboundsAllLinksResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPanelApiInboundsAllLinksResponse200]:
    r"""Return every protocol URL (vless://, vmess://, trojan://, ss://, hysteria://, mtproto) across all
    inbounds and all of their clients. Links are rendered through the subscription engine, so the
    configured remark template (name-only display part) is applied per client — the same output the
    client info/QR pages use. Protocols without a URL form (socks, http, mixed, wireguard, dokodemo,
    tunnel) contribute nothing. Used by the panel’s \"Export all inbound links\" action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPanelApiInboundsAllLinksResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetPanelApiInboundsAllLinksResponse200 | None:
    r"""Return every protocol URL (vless://, vmess://, trojan://, ss://, hysteria://, mtproto) across all
    inbounds and all of their clients. Links are rendered through the subscription engine, so the
    configured remark template (name-only display part) is applied per client — the same output the
    client info/QR pages use. Protocols without a URL form (socks, http, mixed, wireguard, dokodemo,
    tunnel) contribute nothing. Used by the panel’s \"Export all inbound links\" action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPanelApiInboundsAllLinksResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPanelApiInboundsAllLinksResponse200]:
    r"""Return every protocol URL (vless://, vmess://, trojan://, ss://, hysteria://, mtproto) across all
    inbounds and all of their clients. Links are rendered through the subscription engine, so the
    configured remark template (name-only display part) is applied per client — the same output the
    client info/QR pages use. Protocols without a URL form (socks, http, mixed, wireguard, dokodemo,
    tunnel) contribute nothing. Used by the panel’s \"Export all inbound links\" action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPanelApiInboundsAllLinksResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetPanelApiInboundsAllLinksResponse200 | None:
    r"""Return every protocol URL (vless://, vmess://, trojan://, ss://, hysteria://, mtproto) across all
    inbounds and all of their clients. Links are rendered through the subscription engine, so the
    configured remark template (name-only display part) is applied per client — the same output the
    client info/QR pages use. Protocols without a URL form (socks, http, mixed, wireguard, dokodemo,
    tunnel) contribute nothing. Used by the panel’s \"Export all inbound links\" action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPanelApiInboundsAllLinksResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
