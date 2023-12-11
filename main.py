from typing import Optional
import requests
from bs4 import BeautifulSoup
import pandas as pd


class UrlError(Exception):
    def __init__(self, url: str):
        self._url = url
        super().__init__(url)

    def __str__(self) -> str:
        return self._url


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


class Extractor:
    @staticmethod
    def _extract_content(raw_page: RawPage):
        soup = BeautifulSoup(raw_page.data, "html.parser")
        data_block = soup.select_one(".mw-content-ltr")
        assert data_block
        text_content = []

        # first item is always a metadata
        for word_chunk in list(data_block.stripped_strings)[1:]:
            text_content += word_chunk.split()
        return text_content

    @classmethod
    def extract_sentences(cls, raw_page: RawPage, page_content: PageContent):
        sentences = []
        sentence = ""
        for word in cls._extract_content(raw_page):
            if "." in word:
                dot_index = word.find(".")
                sentence += word[: dot_index + 1]
                sentences.append(sentence)
                sentence = word[dot_index + 1 :]
                continue
            sentence += word
            sentence += " "
        if sentence:
            sentences.append(sentence + ".")
        sentences_fixed = []
        for sentence in sentences:
            s = sentence.split()
            last_part = s[-1]
            sentence_fixed = " ".join(s[:-1])
            if last_part == ".":
                sentence_fixed += "."
            else:
                sentence_fixed += " "
                sentence_fixed += last_part
            sentences_fixed.append(sentence_fixed)
        page_content.sentences = sentences_fixed

    @classmethod
    def extract_words(cls, raw_page: RawPage, page_content: PageContent):
        words = []
        word = ""
        raw_data = " ".join(cls._extract_content(raw_page))
        for char in raw_data:
            if char.isspace():
                if word:
                    words.append(word.lower())
                    word = ""
            if char.isalpha():
                word += char
        if word:
            words.append(word.lower())
        page_content.words = words


class PageAnalytics:
    def __init__(self, page_content: PageContent):
        self._page_content = page_content
        self._CONJECTIONS = {
            "and",
            "but",
            "or",
            "nor",
            "for",
            "yet",
            "so",
            "although",
            "because",
            "since",
            "unless",
            "until",
            "when",
            "while",
            "after",
            "before",
            "as",
            "if",
            "whether",
            "since",
            "though",
            "even though",
            "whereas",
            "while",
        }

    def _analyze(self, data):
        data_series = pd.Series(data)
        data_counts = data_series.value_counts()
        return data_counts.head(10)

    def make_analytics(self):
        words = self._page_content.words
        word_series = pd.Series(words)
        word_counts = word_series.value_counts()
        self._top_10_words = word_counts.head(10)
        words_without_conjections = [
            word for word in words if word not in self._CONJECTIONS
        ]
        word_series_without_conjections = pd.Series(words_without_conjections)
        word_counts_without_conjections = word_series_without_conjections.value_counts()
        self._top_10_words_without_conjections = word_counts_without_conjections.head(
            10
        )
        word_lengths = word_series.apply(len)
        self._avarage_word_length = word_lengths.mean()
        self._median_word_length = word_lengths.median()
        word_lengths
        word_with_lengths = pd.to_numeric(word_lengths)
        # self._top_10_longest_words = word_with_lengths.sort_values()
        print(word_with_lengths)

    def save_to_json(self, filename: str):
        pass

    def __str__(self):
        pass


if __name__ == "__main__":
    rp = RawPage("https://en.wikipedia.org/wiki/Banana")
    pc = PageContent()
    Extractor().extract_sentences(rp, pc)
    Extractor().extract_words(rp, pc)
    pa = PageAnalytics(pc)
    pa.make_analytics()
