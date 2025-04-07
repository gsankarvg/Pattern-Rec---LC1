import pandas as pd
from collections import Counter, defaultdict
from itertools import combinations
from nltk.util import bigrams, trigrams
# from nltk.corpus import words, cmudict
from nltk.tokenize import word_tokenize
import pronouncing as pr
from nltk.corpus import gutenberg

def most_common_words(words):
  word_count = Counter(words)
  most_common = word_count.most_common(3)
  print(f"most common words are: {most_common}")

def bigram_trigram(words):
  bgram = list(bigrams(words))
  tgram = list(trigrams(words))
  bgram_count = Counter(bgram).most_common(3)
  tgram_count = Counter(tgram).most_common(3)
  print(f"bigrams are: {bgram_count} \n\ntrigrams are {tgram_count}")

def paldroms(words):
  palindromes = set()
  for w in words:
      if w == w[::-1] and len(w)>2:
          palindromes.add(w)
  print(f"Palindromes: {palindromes}")

def anagrams(words):
  anagram_groups = defaultdict(set)
  for w in words:
      sorted_word = ''.join(sorted(w))
      anagram_groups[sorted_word].add(w)
  anagram_list = [list(group)
                  for group in anagram_groups.values()
                  if len(group) > 1]
  print(f"Anagrams: {anagram_list}")


def rhyming_words(words):
    rhym = set()
    for w1, w2 in combinations(words,2):
        if w2 in pr.rhymes(w1) and w1 != w2:
            rhym.add((w1,w2))
    print(f"rhyming words are : {rhym}")





df = pd.read_csv("textdata.csv")
all_text = " ".join(df["Sentences"]).lower()
words_list = word_tokenize(all_text)
words_list = [word for word in words_list if word.isalpha()]

most_common_words(words_list)
bigram_trigram(words_list)
paldroms(words_list)
anagrams(words_list)
rhyming_words(words_list)

print("-----------------------------------------------------------------------------")

emma = gutenberg.words('austen-emma.txt')
emma_150 = emma[:250]
emma_150 = [word for word in emma_150 if word.isalpha()]
words_list1 = [w.lower() for w in emma_150]

most_common_words(words_list1)
bigram_trigram(words_list1)
paldroms(words_list1)
anagrams(words_list1)
rhyming_words(words_list1)

print("-----------------------------------------------------------------------------")

alice = gutenberg.words('carroll-alice.txt')
alice_250 = alice[:250]
alice_250 = [word for word in alice_250 if word.isalpha()]
words_list2 = [w.lower() for w in alice_250]

most_common_words(words_list2)
bigram_trigram(words_list2)
paldroms(words_list2)
anagrams(words_list2)
rhyming_words(words_list2)

print("-----------------------------------------------------------------------------")
