#!/usr/bin/python

from levenshtein import levenshtein_distance

print("Testing Levenstein distance")
print(levenshtein_distance("hello", "hell") == 1)
print(levenshtein_distance("aie", "aei") == 2)
print(levenshtein_distance("aie", "aei") == 2)
