from bs4 import BeautifulSoup
from rawpage import RawPage
from pagecontent import PageContent


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
            if char in (" ", ".", "/", "—"):
                if word:
                    words.append(word.lower())
                    word = ""
            if char.isalpha() or char in ("-", "–"):
                word += char
        if word:
            words.append(word.lower())
        page_content.words = words
