#!/usr/bin/env python


class Solution:
    digit_letter_map = {
        '2': ("a", "b", "c"),
        '3': ("d", "e", "f"),
        '4': ("g", "h", "i"),
        '5': ("j", "k", "l"),
        '6': ("m", "n", "o"),
        '7': ("p", "q", "r", "s"),
        '8': ("t", "u", "v"),
        '9': ("w", "x", "y", "z")
    }

    def next(self, digits, combinations, results):
        if digits:
            for ch in self.digit_letter_map[digits[0]]:
                self.next(digits[1:], combinations + ch, results)
        else:
            results.append(combinations)

    def letter_combinations(self, digits: str):
        results = []
        if digits:
            self.next(digits, '', results)
        return results


def test():
    solu = Solution()
    assert solu.letter_combinations('2') == ['a', 'b', 'c']
    assert solu.letter_combinations('23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert solu.letter_combinations('34') == ["dg", "dh", "di", "eg", "eh", "ei", "fg", "fh", "fi"]
    assert solu.letter_combinations('') == []
