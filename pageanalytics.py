import pandas as pd
from .pagecontent import PageContent


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
