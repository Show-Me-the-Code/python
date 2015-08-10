# 检索出文章中的关键词
import os
from pprint import pprint
import sys
sys.path.append('..')
from q0004.q0004 import count_words
from q0005.q0005 import find_suffix


def find_unmatched_words(data, match_level, verbose=False):
    copy = data.copy()
    for key in data.keys():
        local_copy = copy.copy()
        del local_copy[key]
        other_keys = local_copy.keys()
        for word in data[key]:
            word_flag = False
            for other_key in other_keys:
                if word in data[other_key][:match_level]:
                    if word_flag is False:
                        if verbose:
                            print('- *%s* found in %s' % (word, key))
                        data[key].pop(data[key].index(word))
                        word_flag = True
                    if verbose:
                        print('- *%s* found in %s' % (word, other_key))
                    data[other_key].pop(data[other_key].index(word))
    return data


if __name__ == '__main__':
    CATCH_LEVEL = 40
    MATCH_LEVEL = 40

    wl = {}
    file_list = find_suffix('.', '.txt')

    for fn in file_list:
        try:
            with open(fn) as fp:
                print('- opening %s' % fn)
                key = os.path.splitext(os.path.basename(fn))[0]
                wl[key] = []
                for common_word in count_words(fp.read()).most_common()[:CATCH_LEVEL]:
                    wl[key].append(common_word[0])
        except FileNotFoundError as e:
            print(e)
    wl = find_unmatched_words(wl, match_level=MATCH_LEVEL)
    pprint(wl)
