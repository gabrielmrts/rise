from dataclasses import dataclass

@dataclass
class HTTPHeaders:
    
    HTTP_HOST: str
    HTTP_CONNECTION: str
    HTTP_CACHE_CONTROL: str
    HTTP_SEC_CH_UA: str
    HTTP_SEC_CH_UA_MOBILE: str
    HTTP_SEC_CH_UA_PLATFORM: str
    HTTP_UPGRADE_INSECURE_REQUESTS: str
    HTTP_USER_AGENT: str
    HTTP_ACCEPT: str
    HTTP_SEC_GPC: str
    HTTP_ACCEPT_LANGUAGE: str
    HTTP_SEC_FETCH_SITE: str
    HTTP_SEC_FETCH_MODE: str
    HTTP_SEC_FETCH_USER: str
    HTTP_SEC_FETCH_DEST: str
    HTTP_ACCEPT_ENCODING: str

@dataclass
class RequestContext:

    SERVER_SOFTWARE: str
    REQUEST_METHOD: str
    QUERY_STRING: str
    RAW_URI: str
    SERVER_PROTOCOL: str
    HTTP_HEADERS: HTTPHeaders
    REMOTE_ADDR: str
    REMOTE_PORT: str
    SERVER_NAME: str
    SERVER_PORT: str
    PATH_INFO: str
    SCRIPT_NAME: str