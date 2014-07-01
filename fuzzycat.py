from itertools import groupby
from collections import defaultdict

#todo:
#calculate similarity of two lists (find proportion of words in each that are shared) take average of the two proportions
#calculate threshold to be categorised together based on total number of lists
#extract words from html
#find way to prioritise/give greater weigthing to words which are within page topic/title/heading tags,

#i'm thinking objects for each word list, each with an attribute that's a namedtuple representing similarity with all other word lists

def filter_common_words(wordlist, common_words):
    '''would it be faster to have common words as a defaultdict? are hash lookups
    faster than searching through a list? Or maybe set. sets are hashable, right?'''

    return (w for w in wordlist if not w in common_words)
    #return [w for w in wordlist if not common_words[w]]

def countwords(wordlist):

    g = groupby(sorted(wordlist))
    d = dict( (k, len(list(v)) ) for k,v in g )
    
    #should make it a defaultdict
    return d


def compare(words_1, words_2): #todo: improve variable naming
    '''take 2 dicts k,v = 'word',num_occurences. return similarity ranking
    common words should be removed before using this function
    '''

    w1_len = sum(v for v in words_1.values())
    w2_len = sum(v for v in words_2.values())

    wic_dict = {}
    # we want the intersection

    #for word in set(words_1).intersection(set(words_2)):
    for word in set.intersection( set(words_1), set(words_2) ):
        wic_dict[word] = (words_1[word], words_2[word])
    
    #wic means words in common
    w1_wic = sum(num_occurences[0] for num_occurences in wic_dict.values())
    w2_wic = sum(num_occurences[1] for num_occurences in wic_dict.values())

    w1_wic_proportion = w1_wic / w1_len
    w2_wic_proportion = w2_wic / w2_len

    return (w1_wic_proportion + w2_wic_proportion)/2

def get_test_cases():
    test_file = open('fuzzycat_tests')
    test_list = [line.strip().split() for line in test_file]

    return test_list

def run_tests(cases):
    word_counts = {}
    for i in range(len(cases)):
        word_counts[i] = countwords(cases[i])
    return word_counts

wc = run_tests(get_test_cases())



