#!/usr/bin/python3
from lxml import etree
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from tqdm import tqdm


def clean_text(text):
    """Tokenize text, converting words to lowercase, 
    removing non-alphabetic tokens and remove stop words.

    Args:
        text (str): text to be cleaned

    Returns:
        str: cleaned text
    """
    # split into tokens
    words = word_tokenize(text)
    # convert to lower case and remove non alphabetic tokens
    words = [word.lower() for word in words if word.isalpha()]
    # remove stop words
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    return " ".join(words)


def save_text(article_tree, class_tree, hyp_file, non_file):
    """Save text of hyperpartisan and non-hyperpartisan articles.

    Args:
        article_tree (xml.etree.ElementTree): articles xml document tree
        class_tree (xml.etree.ElementTree): class xml document tree
        hyp_file (TextIOWrapper): hyperarpartisan output file
        non_file (TextIOWrapper): non-hyperpartisan output file
    """
    for article in tqdm(article_tree.xpath("/articles/article")):
        ident = article.get("id")
        title = article.get("title")
        title = clean_text(title)
        text = article.xpath("string(.)")
        text = clean_text(text)
        hyperpartisan = class_tree.xpath(
            f"/articles/article[@id='{ident}']/@hyperpartisan")[0]
        if hyperpartisan == "true":
            hyp_file.write(f"{title} {text}\n")
        else:
            non_file.write(f"{title} {text}\n")


def main():
    """Main function"""
    # discard whitespace nodes
    parser = etree.XMLParser(remove_blank_text=True)

    # hyperpartisan data path
    PATH = "../../data/hyperpartisan/"

    # parse article document
    article_tree = etree.parse(
        f"{PATH}articles-validation-bypublisher-20181122.xml", parser)

    # parse class document
    class_tree = etree.parse(
        f"{PATH}ground-truth-validation-bypublisher-20181122.xml", parser)

    with open(f"{PATH}hyperpartisan.txt", 'w', encoding="utf-8") as hyp_file, \
            open(f"{PATH}non_hyperpartisan.txt", 'w', encoding="utf-8") as non_file:
        save_text(article_tree, class_tree, hyp_file, non_file)


if __name__ == "__main__":
    main()
