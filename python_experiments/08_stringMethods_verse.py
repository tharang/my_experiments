# -*- coding: utf-8 -*-
__author__ = 'vishy'
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
lenOfVerse = len(verse)
fIndexAnd = verse.find("and")
lIndexYou = verse.rfind("you")
countYou = verse.count("you")

outputString = "Length of the Verse is {}, first index of word \'you\' is {}, last index of word \'you\' is {}, no of occurences of the word \'you\' is {}"
print("\n")
print(outputString.format(lenOfVerse, fIndexAnd, lIndexYou, countYou))