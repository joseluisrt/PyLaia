from __future__ import absolute_import

from typing import Iterable, List, Tuple, Union


def char_to_word_seq(sequence_of_characters, delimiters):
    # type: (Iterable, Union[List,Tuple]) -> List[List]
    """Convert a sequence of characters into a sequence of words.

    Examples:
        >>> char_to_word_seq(' hello my  friend ', [' '])
        [['h', 'e', 'l', 'l', 'o'], ['m', 'y'], ['f', 'r', 'i', 'e', 'n', 'd']]
        >>> char_to_word_seq([-2, 1, 2, 3, -1, 1, 2, -2, 3], [-1, -2])
        [[1, 2, 3], [1, 2], [3]]

    Args:
        sequence_of_characters (iterable): A list of symbols representing the
            characters in a sentence.
        delimiters (iterable): A set of symbols representing the word
            delimiters. Any sequence of characters

    Returns:
        A list of lists containing the characters that form each word.
        Delimiters are not included.
    """
    delimiters = set(delimiters)
    word_seq = [[]]
    prev_is_delim = True
    for c in sequence_of_characters:
        if c in delimiters:
            if not prev_is_delim:
                word_seq.append([])
            prev_is_delim = True
        else:
            word_seq[-1].append(c)
            prev_is_delim = False
    if not word_seq[-1]:
        word_seq = word_seq[:-1]
    return word_seq
