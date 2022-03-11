"""Calculate log odds for each word in a file."""
from collections import defaultdict
from math import log
from tqdm import tqdm

PATH = "../../data/hyperpartisan/"


def get_word_freq(filename):
    """Return a dictionary with the word frequencies in a file.

    Args:
        filename (str): path to file

    Returns:
        defaultdict[str, int]: dictionary with word frequencies
    """
    word_freq = defaultdict(int)
    with open(filename, encoding='utf-8') as file:
        pbar = tqdm(total=150000)
        for line in file:
            for token in line.split():
                word_freq[token] += 1
            pbar.update(1)
        pbar.close()
    return word_freq


def log_odd(freq, n_words):
    """Return the log odds for a word.

    Args:
        freq (int): word frequency
        n_words (int): total number of words

    Returns:
        float: log odd for the word
    """
    prob = freq / n_words
    odd = prob / (1 - prob)
    return log(odd)


def log_odd_ratio(word_freq_hyp, word_freq_non, n_hyp, n_non):
    """Return the log odds ratio for a word.

    Args:
        word_freq_hyp (defaultdict[str, int]): dictionary with word frequencies
            in hyperpartisan file
        word_freq_non (defaultdict[str, int]): dictionary with word frequencies
            in non-hyperpartisan file
        n_hyp (int): total number of words in hyperpartisan file
        n_non (int): total number of words in non-hyperpartisan file

    Returns:
        defaultdict[str, float]: log odds ratios for each word
    """
    log_odds = defaultdict(float)
    words = set(word_freq_hyp.keys())
    words.update(word_freq_non.keys())
    for word in words:
        freq_hyp = word_freq_hyp[word]
        freq_non = word_freq_non[word]
        if freq_hyp < 20 or freq_non < 20:
            continue
        log_odds[word] = log_odd(freq_hyp, n_hyp) - log_odd(freq_non, n_non)
    return log_odds


def main():
    """Main function"""
    hyp_inp = f"{PATH}hyperpartisan.txt"
    non_inp = f"{PATH}non_hyperpartisan.txt"
    hyp_out = "hyperpartisan_words.tsv"
    non_out = "non_hyperpartisan_words.tsv"
    word_freq_hyp = get_word_freq(hyp_inp)
    word_freq_non = get_word_freq(non_inp)
    n_hyp = sum(word_freq_hyp.values())
    n_non = sum(word_freq_non.values())
    log_odds = log_odd_ratio(word_freq_hyp, word_freq_non, n_hyp, n_non)

    sorted_log_odds = sorted(
        log_odds.items(), key=lambda x: x[1], reverse=True)

    with open(hyp_out, "w", encoding="utf-8") as file:
        for word, odd in sorted_log_odds[:50]:
            file.write(f"{word}\t{odd}\n")

    with open(non_out, "w", encoding="utf-8") as file:
        for word, odd in sorted_log_odds[::-1][:50]:
            file.write(f"{word}\t{odd}\n")


if __name__ == "__main__":
    main()
