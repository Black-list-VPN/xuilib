from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RealityScanResult")


@_attrs_define
class RealityScanResult:
    """
    Attributes:
        alpn (str):  Example: h2.
        cert_issuer (str):  Example: Google Trust Services.
        cert_subject (str):  Example: cloudflare.com.
        cert_valid (bool):  Example: True.
        curve_id (str):  Example: X25519.
        feasible (bool):  Example: True.
        h2 (bool):  Example: True.
        host (str):  Example: www.cloudflare.com.
        ip (str):  Example: 104.16.124.96.
        latency_ms (int):  Example: 180.
        not_after (str):  Example: 2026-08-01T00:00:00Z.
        port (int):  Example: 443.
        reason (str):
        server_names (list[str]):
        target (str):  Example: www.cloudflare.com:443.
        tls13 (bool):  Example: True.
        tls_version (str):  Example: 1.3.
        x25519 (bool):  Example: True.
    """

    alpn: str
    cert_issuer: str
    cert_subject: str
    cert_valid: bool
    curve_id: str
    feasible: bool
    h2: bool
    host: str
    ip: str
    latency_ms: int
    not_after: str
    port: int
    reason: str
    server_names: list[str]
    target: str
    tls13: bool
    tls_version: str
    x25519: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alpn = self.alpn

        cert_issuer = self.cert_issuer

        cert_subject = self.cert_subject

        cert_valid = self.cert_valid

        curve_id = self.curve_id

        feasible = self.feasible

        h2 = self.h2

        host = self.host

        ip = self.ip

        latency_ms = self.latency_ms

        not_after = self.not_after

        port = self.port

        reason = self.reason

        server_names = self.server_names

        target = self.target

        tls13 = self.tls13

        tls_version = self.tls_version

        x25519 = self.x25519

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alpn": alpn,
                "certIssuer": cert_issuer,
                "certSubject": cert_subject,
                "certValid": cert_valid,
                "curveID": curve_id,
                "feasible": feasible,
                "h2": h2,
                "host": host,
                "ip": ip,
                "latencyMs": latency_ms,
                "notAfter": not_after,
                "port": port,
                "reason": reason,
                "serverNames": server_names,
                "target": target,
                "tls13": tls13,
                "tlsVersion": tls_version,
                "x25519": x25519,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alpn = d.pop("alpn")

        cert_issuer = d.pop("certIssuer")

        cert_subject = d.pop("certSubject")

        cert_valid = d.pop("certValid")

        curve_id = d.pop("curveID")

        feasible = d.pop("feasible")

        h2 = d.pop("h2")

        host = d.pop("host")

        ip = d.pop("ip")

        latency_ms = d.pop("latencyMs")

        not_after = d.pop("notAfter")

        port = d.pop("port")

        reason = d.pop("reason")

        server_names = cast(list[str], d.pop("serverNames"))

        target = d.pop("target")

        tls13 = d.pop("tls13")

        tls_version = d.pop("tlsVersion")

        x25519 = d.pop("x25519")

        reality_scan_result = cls(
            alpn=alpn,
            cert_issuer=cert_issuer,
            cert_subject=cert_subject,
            cert_valid=cert_valid,
            curve_id=curve_id,
            feasible=feasible,
            h2=h2,
            host=host,
            ip=ip,
            latency_ms=latency_ms,
            not_after=not_after,
            port=port,
            reason=reason,
            server_names=server_names,
            target=target,
            tls13=tls13,
            tls_version=tls_version,
            x25519=x25519,
        )

        reality_scan_result.additional_properties = d
        return reality_scan_result

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
