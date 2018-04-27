#!/usr/bin/python

from levenshtein import levenshtein_distance
from levenshtein_reduced_memory import levenshtein_distance as l_distance
from damerau_levenshtein import damerau_levenshtein_distance
from damerau_levenshtein_reduced_memory import damerau_levenshtein_distance as dl_distance
from reduced_levenshtein import levenshtein

print("Testing Levenshtein distance")
print(levenshtein_distance("hello", "hell") == 1)
print(levenshtein_distance("aie", "aei") == 2)
print(levenshtein_distance("aie", "aei") == 2)

#print("Testing Damerau-Levenshtein distance")
#print(damerau_levenshtein_distance("hello", "hell") == 1)
#print(damerau_levenshtein_distance("aie", "aei") == 1)  # Testing transposition working

print("Testing Levenshtein distance, pythonic reduced memory algorithm")
print(levenshtein_distance("hello", "hell") == 1)
print(levenshtein_distance("aie", "aei") == 2)
print(levenshtein_distance("aie", "aei") == 2)

print("Testing Levenshtein distance, reduced memory algorithm")
print(l_distance("hello", "hell") == 1)
print(l_distance("aie", "aei") == 2)
print(l_distance("aie", "aei") == 2)


print("Testing Damerau-Levenshtein distance, reduced memory algorithm")
print(dl_distance("hello", "hell") == 1)
print(dl_distance("aie", "aei") == 1) # Testing transposition working






