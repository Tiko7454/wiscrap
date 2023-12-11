class PageContent:
    def __init__(self):
        self._sentences = []
        self._words = []

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
