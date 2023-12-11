class UrlError(Exception):
    def __init__(self, url: str):
        self._url = url
        super().__init__(url)

    def __str__(self) -> str:
        return self._url
