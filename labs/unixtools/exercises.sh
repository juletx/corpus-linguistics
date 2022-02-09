# How many tokens in word.txt?
wc -w word.txt
# Sort words.txt file.
sort word.txt
# Sort words.txt file words according to word’s last character.
rev word.txt | sort | rev
# How many different words in word.txt?
sort word.txt | uniq | wc -l
# Sort word types according to their frequency.
sort word.txt | uniq -c | sort -n
# 20 most frequent word types?
sort word.txt | uniq -c | sort -nr | head -n 20
# which is the 100 most frequent word?
sort word.txt | uniq -c | sort -nr | head -n 100 | tail -n 1
sort word.txt | uniq -c | sort -nr | tail -n +100 | head -n 1
# how many different POS values?
cut -f 2 word_pos.txt | sort | uniq -c | sort -nr
# what are the possible POS values in wsj_0020.v2_gold_skel
cut -f 5 wsj_0020.v2_gold_skel | sort | uniq -c | sort -nr
# how many times does the brand audi appear?
grep AUDI word.txt
# Words starting with letter ’a’ or ’A’
egrep "^[aA].*\$" word.txt | sort | uniq -c | sort -nr | head -n 20
# Lines containing a digit
egrep "^[[:digit:]]+\$" word.txt | sort | uniq -c | sort -nr | head -n 20
# How many words in word.txt, excluding punctuation marks? (use character classes)
egrep -v "^[[:punct:]]+\$" word.txt | wc -l
# How many punctuation marks? (use character classes)
egrep "^[[:punct:]]+\$" word.txt | wc -l
# How many nouns (starting with N) in wsj_0020.v2_gold_skel?
cut -f 5 wsj_0020.v2_gold_skel | egrep "^N" | wc -l
# convert all numbers to special token NUM
sed -e 's/[[:digit:]]\+/NUM/g' word.txt
# Tokenize austen-emma.txt
./tokenize.sh austen-emma.txt | sort | uniq -c | sort -nr | head -n 20
# given word.txt create a bigram.txt document with bigrams.
tail -n +2 word.txt > word2.txt
paste word.txt word2.txt > bigram.txt
# how many different bigrams? how frequent are they?
sort bigrams.txt | uniq -c | sort -nr | head -n 20