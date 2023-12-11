from .rawpage import RawPage
from .pagecontent import PageContent
from .extractor import Extractor
from .pageanalytics import PageAnalytics


if __name__ == "__main__":
    rp = RawPage("https://en.wikipedia.org/wiki/Banana")
    pc = PageContent()
    Extractor().extract_sentences(rp, pc)
    Extractor().extract_words(rp, pc)
    pa = PageAnalytics(pc)
    pa.make_analytics()
