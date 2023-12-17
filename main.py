from rawpage import RawPage
from pagecontent import PageContent
from extractor import Extractor
from pageanalytics import PageAnalytics


def make_full_analysis(url: str) -> tuple[dict, PageContent]:
    rp = RawPage(url)
    pc = PageContent(url)
    Extractor().extract_sentences(rp, pc)
    Extractor().extract_words(rp, pc)
    pa = PageAnalytics(pc)
    pa.make_analytics()
    pa.save_to_json(f"{rp.headline}.json")
    return pa.get_python_report(), pc


if __name__ == "__main__":
    oppenheimer, oppenheimer_pc = make_full_analysis(
        "https://en.wikipedia.org/wiki/J._Robert_Oppenheimer"
    )
    ritchie, ritchie_pc = make_full_analysis(
        "https://en.wikipedia.org/wiki/Dennis_Ritchie"
    )
    alan_wake, alan_wake_pc = make_full_analysis(
        "https://en.wikipedia.org/wiki/Alan_Wake"
    )
    max_length_sentence_article, _ = max(
        [
            ("oppenheimer", oppenheimer["max_length_sentence"]),
            ("ritchie", ritchie["max_length_sentence"]),
            ("alan_wake", alan_wake["max_length_sentence"]),
        ],
        key=lambda x: len(x[1]),
    )
    max_length_word_article, _ = max(
        [
            ("oppenheimer", oppenheimer["top_10_longest_words"][0]),
            ("ritchie", ritchie["top_10_longest_words"][0]),
            ("alan_wake", alan_wake["top_10_longest_words"][0]),
        ],
        key=lambda x: len(x[1]),
    )
    max_sentence_count_article, _ = max(
        [
            ("oppenheimer", len(oppenheimer_pc.sentences)),
            ("ritchie", len(ritchie_pc.sentences)),
            ("alan_wake", len(alan_wake_pc.sentences)),
        ],
        key=lambda x: x[1],
    )
    max_word_count_article, _ = max(
        [
            ("oppenheimer", len(oppenheimer_pc.words)),
            ("ritchie", len(ritchie_pc.words)),
            ("alan_wake", len(alan_wake_pc.words)),
        ],
        key=lambda x: x[1],
    )
    print(max_length_sentence_article)
    print(max_length_word_article)
    print(max_sentence_count_article)
    print(max_word_count_article)
