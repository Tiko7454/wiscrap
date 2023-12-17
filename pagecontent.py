class PageContent:
    """
    Class which just contains data.

    Attributes:
        url (str): The URL of the data related to it.
        sentences (list): The list of all sentences containing in the URL.
        words (list): The list of all words containing in the URL.

    Properties:
        url (str): Returns the URL associated with this instance.
        sentences (tuple): Returns a tuple of sentences extracted from the URL content.
        words (tuple): Returns a tuple of words extracted from the URL content.
    """

    def __init__(self, url: str):
        """
        Initializes a new instance of the PageContent class.

        Args:
            url (str): The URL associated with the data.
        """
        self._url = url
        self._sentences = []
        self._words = []

    @property
    def url(self):
        """
        Returns the URL associated with this instance.

        Returns:
            str: The URL of the data related to this instance.
        """
        return self._url

    @property
    def sentences(self):
        """
        Returns a tuple of sentences extracted from the URL content.

        Returns:
            tuple: A tuple of sentences.
        """
        return tuple(self._sentences)

    @sentences.setter
    def sentences(self, value: list[str]):
        """
        Sets the list of sentences for this instance.

        Args:
            value (list): The list of sentences to be set.
        """
        self._sentences = value

    @property
    def words(self):
        """
        Returns a tuple of words extracted from the URL content.

        Returns:
            tuple: A tuple of words.
        """
        return tuple(self._words)

    @words.setter
    def words(self, value: list[str]):
        """
        Sets the list of words for this instance.

        Args:
            value (list): The list of words to be set.
        """
        self._words = value
