# -*- coding: utf-8 -*-
__author__ = 'vishy'

week = ['mon', 'tue', 'wed', 'thur', 'fri', 'sat']

#methods in list - len, max, min, sorted

print("max in the list {} is {}".format(week, max(week)))
print("min in the list {} is {}".format(week, min(week)))

print("alphabetically sorting the list {} looks like ==>  {}".format(week, sorted(week)))
print("alphabetically reverse sorting the list {} looks like ==>  {}".format(week, sorted(week, reverse=True)))


# join, append
print("-".join(week))

week.append('sun')
print("list after appending sun = {}".format(week))

