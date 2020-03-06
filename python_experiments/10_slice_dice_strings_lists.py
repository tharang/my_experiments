# -*- coding: utf-8 -*-
__author__ = 'vishy'

verse = "bangalore"
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

print("verse = {}".format(verse))
print("months = {}".format(months))
#similarities in accessing lists and strings
#1 - Len() function
print("Length of string len(verse) = {}".format(len(verse)))
print("Length of list len(months) = {}".format(len(months)))

#2 - slicing

print("verse[:3] = {}".format(verse[:3]))
print("months[:6] = {}".format(months[:6]))

print("verse[3:] = {}".format(verse[3:]))
print("months[6:] = {}".format(months[6:]))

#3 - in and not in
print("gal in {} = {}".format(verse, 'gal' in verse))
print("Oct in {} = {}".format(months, 'Oct' in months))

print("her not in {} = {}".format(verse, 'her' not in verse))
print("Sunday not in {} = {}".format(months, 'Sunday' not in months))


print("gal not in {} = {}".format(verse, 'gal' not in verse))
print("Oct not in {} = {}".format(months, 'Oct' not in months))