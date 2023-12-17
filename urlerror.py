class UrlError(Exception):
    """
    Custom exception raised for invalid or unsupported URL.

    Attributes:
        url (str): The URL that caused the error.
    """

    def __init__(self, url: str):
        """
        Initializes a new instance of the UrlError class.

        Args:
            url (str): The URL that caused the error.
        """
        self._url = url
        super().__init__(url)

    def __str__(self) -> str:
        """
        Returns a string representation of the exception containing just the URL.

        Returns:
            str: A string representation of the exception.
        """
        return self._url
