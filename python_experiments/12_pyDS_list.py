# -*- coding: utf-8 -*-
__author__ = 'vishy'
#print("{}".format())


#Syntax for creating a list:
#indices
#:      0   1    2   3   4  5
nums = [11, 22, 33, 44, 55, 66]
print("list nums = {}\n".format(nums))

#list indexing
info = "list indexing : nums[{}] = {}"
print(info.format(0, nums[0]))
print(info.format(1, nums[1]))
#Negative indexes are allowed:
print(info.format(-1, nums[-1]))
print(info.format(-2, nums[-2]))

print("\n")

#List slicing
info1 = "list slicing : nums[:{}] = {}"
info2 = "list slicing : nums[{}:] = {}"
info3 = "list slicing : nums[{}:{}] = {}"
info4 = "list slicing : nums[:] = {}"

print(info1.format(2, nums[:2]))
print(info1.format(4, nums[:4]))

print(info2.format(2, nums[2:]))
print(info2.format(3, nums[3:]))

print(info3.format(2, 4, nums[2:4]))
print(info3.format(1, 4, nums[1:4]))

print(info4.format(nums[:]))

#List comprehension
print("\nConditional List Comprehension")
number_list = [ x for x in range(20) if x % 2 == 0]
command = "number_list = [ x for x in range(20) if x % 2 == 0]"
print("command : {}".format(command))
print("number_list = {}\n".format(number_list))

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
command = "num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]"
print("command : {}".format(command))
print("list num_list = {}\n".format(num_list))

#Membership testing
print("\nlist nums = {}".format(nums))
info1 = "{} in nums = {}"
info2 = "{} not in nums = {}"

print(info1.format(22, 22 in nums))
print(info2.format(22, 22 not in nums))

#Iterating over lists
print("\nIterating over lists")
info1 = "\tIterating over nums"

print(info1)
for x in nums:
    print("\t\t{}".format(x))

#List Methods
print("\nlist nums = {}".format(nums))
info1 = "methods in list to remember : max, min, sorted, append, join, "
info2 = "{} of nums = {}"
print(info1)
print(info2.format("max", max(nums)))
print(info2.format("min", min(nums)))
print(info2.format("sorting", sorted(nums)))
print(info2.format("reverse sorting", sorted(nums, reverse=True)))
sum = 0
for i in nums:
    sum += i;
info3 = "+".join(str(n) for n in nums)
print(info2.format(info3, sum))

nums.append(77)
print("nums after appending 77 = {}".format(nums))
