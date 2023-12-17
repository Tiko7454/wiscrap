class PageContent:
    def __init__(self, url: str):
        self._url = url
        self._sentences = []
        self._words = []

    @property
    def url(self):
        return self._url

    @property
    def sentences(self):
        return tuple(self._sentences)

    @sentences.setter
    def sentences(self, value: list[str]):
        self._sentences = value

    @property
    def words(self):
        return tuple(self._words)

    @words.setter
    def words(self, value: list[str]):
        self._words = value
