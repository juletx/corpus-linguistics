"""Extracts log odds ratios for words and bigrams."""
from collections import defaultdict
from math import log
from tqdm import tqdm

PATH = "../../data/hyperpartisan/"


def word_bigram_freq(filename):
    """Return two dictionaries with the word and bigram frequencies in a file.

    Args:
        filename (str): path to file

    Returns:
        defaultdict[str, int]: dictionary with word frequencies
        defaultdict[str, int]: dictionary with bigram frequencies
    """
    word_freq = defaultdict(int)
    bigram_freq = defaultdict(int)
    with open(filename, encoding='utf-8') as file:
        pbar = tqdm(total=150000)
        for line in file:
            words = line.split()
            for i in range(len(words) - 1):
                word_freq[words[i]] += 1
                bigram_freq[f"{words[i]}\t{words[i+1]}"] += 1
            word_freq[words[len(words) - 1]] += 1
            pbar.update(1)
        pbar.close()
    return word_freq, bigram_freq


def log_odd(freq, total):
    """Return the log odds for a word or bigram.

    Args:
        freq (int): word frequency
        total (int): total number of words or bigrams

    Returns:
        float: log odd for the word or bigram
    """
    prob = freq / total
    odd = prob / (1 - prob)
    return log(odd)


def log_odd_ratio(string_freq_hyp, string_freq_non, min_freq=20):
    """Return the log odd ratios for words or bigrams.

    Args:
        freq_hyp (defaultdict[str, int]): dictionary with word or bigram frequencies
            in hyperpartisan file
        freq_non (defaultdict[str, int]): dictionary with word or bigram frequencies
            in non-hyperpartisan file
        min_freq (int): minimum frequency for a word or bigram to be included

    Returns:
        defaultdict[str, float]: log odds ratios for each word or bigram
    """
    n_hyp = sum(string_freq_hyp.values())
    n_non = sum(string_freq_non.values())
    log_odds = defaultdict(float)
    strings = set(string_freq_hyp.keys())
    strings.update(string_freq_non.keys())
    for string in tqdm(strings):
        freq_hyp = string_freq_hyp[string]
        freq_non = string_freq_non[string]
        if freq_hyp < min_freq or freq_non < min_freq:
            continue
        log_odds[string] = log_odd(freq_hyp, n_hyp) - log_odd(freq_non, n_non)
    return log_odds


def write_results(log_odds, hyp_out, non_out, count=50):
    """Write the results to hyperpartisan and non-hyperpartisan files.

    Args:
        log_odds (defaultdict[str, float]): dictionary with log odds ratios
        hyp_out (file): file to write hyperpartisan results to
        non_out (file): file to write non-hyperpartisan results to
        count (int): number of results to write to each file
    """
    sorted_log_odds = sorted(
        log_odds.items(), key=lambda x: x[1], reverse=True)

    with open(hyp_out, "w", encoding="utf-8") as file:
        for string, odd in sorted_log_odds[:count]:
            file.write(f"{string}\t{odd}\n")

    with open(non_out, "w", encoding="utf-8") as file:
        for string, odd in sorted_log_odds[::-1][:count]:
            file.write(f"{string}\t{odd}\n")


def extract_log_odd_ratios():
    """Main function that extracts log odds ratios for words and bigrams."""
    hyp_inp = f"{PATH}hyperpartisan.txt"
    non_inp = f"{PATH}non-hyperpartisan.txt"
    word_freq_hyp, bigram_freq_hyp = word_bigram_freq(hyp_inp)
    word_freq_non, bigram_freq_non = word_bigram_freq(non_inp)

    log_odd_words = log_odd_ratio(word_freq_hyp, word_freq_non)
    hyp_words = "hyperpartisan_words.tsv"
    non_words = "non_hyperpartisan_words.tsv"
    write_results(log_odd_words, hyp_words, non_words)

    log_odd_bigrams = log_odd_ratio(bigram_freq_hyp, bigram_freq_non)
    hyp_bigrams = "hyperpartisan_bigrams.tsv"
    non_bigrams = "non_hyperpartisan_bigrams.tsv"
    write_results(log_odd_bigrams, hyp_bigrams, non_bigrams)


if __name__ == "__main__":
    extract_log_odd_ratios()
