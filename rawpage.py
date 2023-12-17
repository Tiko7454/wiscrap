import requests
from typing import Optional
from urlerror import UrlError


class RawPage:
    """
    Class which extracts needed data from the webpage.

    Attributes:
        url (str): The URL of the webpage.
        headline (str): The headline of the Wikipedia article.
        data (str): The extracted data.

    Properties:
        url (str): Returns the URL associated with this instance.
        sentences (tuple): Returns a tuple of sentences extracted from the URL content.
        words (tuple): Returns a tuple of words extracted from the URL content.
    """

    def __init__(self, url: str):
        """
        Initializes a new instance of the RawPage class.

        Args:
            url (str): The URL of the webpage.
        """
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
        """
        If there is no data already extracted, extracts the data from the webpage and in both cases returns the data
        """
        if self._data is None:
            self._collect_data()
        assert self._data
        return self._data

    @property
    def headline(self) -> str:
        """
        If there is no headline already extracted, extracts the data from the webpage and in both cases returns the headline
        """
        if self._headline is None:
            self._collect_data()
        assert self._headline
        return self._headline
