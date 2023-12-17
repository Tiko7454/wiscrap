import pandas as pd
from pagecontent import PageContent
import json


class PageAnalytics:
    """
    Class which provides a PageContent instance analytics.
    """

    def __init__(self, page_content: PageContent):
        """
        Initializes a new instance of the PageAnalytics class from PageContent.

        Args:
            page_content (PageContent): The page content which will be analysed.
        """

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
            "whereas",
            "while",
        }
        self._json = None

    def _analyze(self, data):
        data_series = pd.Series(data)
        data_counts = data_series.value_counts()
        return data_counts.head(10)

    def make_analytics(self):
        """
        Does the analyses which fills self._json with:
            url: the orl of the page
            top_10_words: top 10 most frequent words
            top_10_words_without_conjections: top 10 most frequent words not counting the conjections
            avarage_word_length: the avarage of the word lengths
            median_word_length: the median of the word lengths
            top_10_longest_words: top 10 longest words
            avarage_sentence_length: the avarage of the sentence lengths
            median_sentence_length: the median of the sentence lengths
            max_length_sentence: the longest sentence.
        """
        report = {}
        report["url"] = self._page_content.url
        words = self._page_content.words
        word_series = pd.Series(words)
        word_counts = word_series.value_counts()
        report["top_10_words"] = word_counts.head(10).index.tolist()
        words_without_conjections = [
            word for word in words if word not in self._CONJECTIONS
        ]
        word_series_without_conjections = pd.Series(words_without_conjections)
        word_counts_without_conjections = word_series_without_conjections.value_counts()
        report[
            "top_10_words_without_conjections"
        ] = word_counts_without_conjections.head(10).index.tolist()
        word_lengths = word_series.apply(len)
        report["avarage_word_length"] = word_lengths.mean()
        report["median_word_length"] = word_lengths.median()
        word_with_lengths = pd.DataFrame(
            {"word": words, "length": [len(word) for word in words]}
        ).sort_values(by="length", ascending=False)
        report["top_10_longest_words"] = (
            word_with_lengths["word"].unique().tolist()[:10]
        )

        sentences = self._page_content.sentences
        sentence_series = pd.Series(sentences)
        sentence_lengths = sentence_series.apply(len)
        report["avarage_sentence_length"] = sentence_lengths.mean()
        report["median_sentence_length"] = sentence_lengths.median()
        sentence_with_lengths = pd.DataFrame(
            {"sentence": sentences, "length": [len(sentence) for sentence in sentences]}
        ).sort_values(by="length", ascending=False)
        report["max_length_sentence"] = (
            sentence_with_lengths["sentence"].head(1).tolist()[0]
        )
        self._json = json.dumps(report, indent=4)

    def save_to_json(self, filename: str):
        """
        Dumps self._json to a file with a given name.

        Args:
            filename (str): the file name.
        """
        with open(filename, "w") as file:
            json.dump(json.loads(str(self._json)), file, indent=4)

    def get_python_report(self) -> dict:
        """
        Gets self._json in python dict format.

        Returns:
            dict: the report.
        """
        return json.loads(str(self._json))

    def __str__(self):
        return str(self._json)
