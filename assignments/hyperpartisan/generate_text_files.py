"""Generate two text files for hyperpartisan and non-hyperpartisan
news articles."""
import string
from lxml import etree
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from tqdm import tqdm


PATH = "../../data/hyperpartisan/"
PUNCTUATION = string.punctuation + "‘’“”«»–…•"
STOPWORDS = set(stopwords.words('english'))
ENTITIES = set(["lt", "amp", "gt", "quot", "apos"])
IMAGE = set(["img", "alt", "src", "width", "height", "https", "datarecalcdims", "aligncenter"])


def clean_text(text):
    """Tokenize text, convert words to lowercase, remove puntuation,
    numbers, stop words, xml entities and image tags.

    Args:
        text (str): text to be cleaned

    Returns:
        str: cleaned text
    """
    # split into tokens
    words = word_tokenize(text)
    # convert to lower case and remove punctuation
    table = str.maketrans('', '', PUNCTUATION)
    words = [str.lower(word.translate(table)) for word in words]
    # remove numbers, stop words, xml entities and image tags
    words = [word for word in words if word.isalpha() and word not in STOPWORDS | ENTITIES | IMAGE]
    # join words to string
    text = " ".join(words)
    # remove extra whitespace
    text = " ".join(text.split())
    # strip whitespace at start and end
    text = text.strip()
    return text


def save_text(article_tree, class_dict, hyp_file, non_file):
    """Save text of hyperpartisan and non-hyperpartisan articles.

    Args:
        article_tree (xml.etree.ElementTree): articles xml document tree
        class_dict (dict): dictionary of article ids and their hyperpartisan class
        hyp_file (TextIOWrapper): hyperarpartisan output file
        non_file (TextIOWrapper): non-hyperpartisan output file
    """
    for article in tqdm(article_tree.xpath("/articles/article")):
        ident = article.get("id")
        title = article.get("title")
        title = clean_text(title)
        text = article.xpath("string(.)")
        text = clean_text(text)
        line = f"{title} {text}".strip()
        if class_dict[ident] == "true":
            hyp_file.write(f"{line}\n")
        else:
            non_file.write(f"{line}\n")


def get_class_dict(class_tree):
    """Get dictionary of article ids and their hyperpartisan class.

    Args:
        class_tree (xml.etree.ElementTree): class xml document tree

    Returns:
        dict: dictionary of article ids and their hyperpartisan class
    """
    class_dict = {}
    for article in class_tree.xpath("/articles/article"):
        class_dict[article.get("id")] = article.get("hyperpartisan")
    return class_dict


def generate_text_files():
    """Main function that generates hyperpartisan and non-hyperpartisan text files."""
    # discard whitespace nodes
    parser = etree.XMLParser(remove_blank_text=True)

    # parse article document
    article_tree = etree.parse(
        f"{PATH}articles-validation-bypublisher-20181122.xml", parser)

    # parse class document
    class_tree = etree.parse(
        f"{PATH}ground-truth-validation-bypublisher-20181122.xml", parser)

    class_dict = get_class_dict(class_tree)

    with open(f"{PATH}hyperpartisan.txt", 'w', encoding="utf-8") as hyp_file, \
            open(f"{PATH}non-hyperpartisan.txt", 'w', encoding="utf-8") as non_file:
        save_text(article_tree, class_dict, hyp_file, non_file)


if __name__ == "__main__":
    generate_text_files()
