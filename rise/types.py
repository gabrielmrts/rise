from dataclasses import dataclass

@dataclass
class RequestContext:

    server_software: str
    request_method: str
    query_string: str
    raw_uri: str
    server_protocol: str
    remote_addr: str
    remote_port: str
    server_name: str
    server_port: str
    path_info: str
    script_name: str
    body: str
    body_json: dict
    http_host: str
    http_connection: str
    http_cache_control: str
    http_sec_ch_ua: str
    http_sec_ch_ua_mobile: str
    http_sec_ch_ua_platform: str
    http_upgrade_insecure_requests: str
    http_user_agent: str
    http_accept: str
    http_sec_gpc: str
    http_accept_language: str
    http_sec_fetch_site: str
    http_sec_fetch_mode: str
    http_sec_fetch_user: str
    http_sec_fetch_dest: str
    http_accept_encoding: str
    http_content_type: str