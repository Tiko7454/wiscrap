import requests
from typing import Optional
from .urlerror import UrlError


class RawPage:
    def __init__(self, url: str):
        self._url = url
        self._headline: Optional[str] = None
        self._data: Optional[str] = None

    def _collect_data(self):
        r = requests.get(self._url)
        if r.status_code != requests.status_codes.codes.ok:
            raise UrlError(self._url)
        self._data = r.content.decode()
        self._headline = self._url.split("/")[-1]

    @property
    def data(self) -> str:
        if self._data is None:
            self._collect_data()
        assert self._data
        return self._data

    @property
    def headline(self) -> str:
        if self._headline is None:
            self._collect_data()
        assert self._headline
        return self._headline
