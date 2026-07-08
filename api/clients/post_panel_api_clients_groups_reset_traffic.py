from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_panel_api_clients_groups_reset_traffic_body import PostPanelApiClientsGroupsResetTrafficBody
from ...models.post_panel_api_clients_groups_reset_traffic_response_200 import (
    PostPanelApiClientsGroupsResetTrafficResponse200,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PostPanelApiClientsGroupsResetTrafficBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/panel/api/clients/groups/resetTraffic",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostPanelApiClientsGroupsResetTrafficResponse200 | None:
    if response.status_code == 200:
        response_200 = PostPanelApiClientsGroupsResetTrafficResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostPanelApiClientsGroupsResetTrafficResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiClientsGroupsResetTrafficBody,
) -> Response[PostPanelApiClientsGroupsResetTrafficResponse200]:
    """Reset only the group-level traffic counter shown on the groups page. Snapshots the current up/down
    sum of the group's members as a baseline so the group total reads zero, while leaving each client's
    own counters (and their quotas) untouched. No Xray restart is triggered. Creates the client_groups
    row if the group exists only as a derived label.

    Args:
        body (PostPanelApiClientsGroupsResetTrafficBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPanelApiClientsGroupsResetTrafficResponse200]
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
    body: PostPanelApiClientsGroupsResetTrafficBody,
) -> PostPanelApiClientsGroupsResetTrafficResponse200 | None:
    """Reset only the group-level traffic counter shown on the groups page. Snapshots the current up/down
    sum of the group's members as a baseline so the group total reads zero, while leaving each client's
    own counters (and their quotas) untouched. No Xray restart is triggered. Creates the client_groups
    row if the group exists only as a derived label.

    Args:
        body (PostPanelApiClientsGroupsResetTrafficBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPanelApiClientsGroupsResetTrafficResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiClientsGroupsResetTrafficBody,
) -> Response[PostPanelApiClientsGroupsResetTrafficResponse200]:
    """Reset only the group-level traffic counter shown on the groups page. Snapshots the current up/down
    sum of the group's members as a baseline so the group total reads zero, while leaving each client's
    own counters (and their quotas) untouched. No Xray restart is triggered. Creates the client_groups
    row if the group exists only as a derived label.

    Args:
        body (PostPanelApiClientsGroupsResetTrafficBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPanelApiClientsGroupsResetTrafficResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiClientsGroupsResetTrafficBody,
) -> PostPanelApiClientsGroupsResetTrafficResponse200 | None:
    """Reset only the group-level traffic counter shown on the groups page. Snapshots the current up/down
    sum of the group's members as a baseline so the group total reads zero, while leaving each client's
    own counters (and their quotas) untouched. No Xray restart is triggered. Creates the client_groups
    row if the group exists only as a derived label.

    Args:
        body (PostPanelApiClientsGroupsResetTrafficBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPanelApiClientsGroupsResetTrafficResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
