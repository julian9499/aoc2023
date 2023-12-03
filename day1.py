import re


f = open("files/day1.txt")

conv = [x.strip() for x in f.readlines()]
conv = [w.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three").replace("four", "four4fiyr").replace("five","five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine") for w in conv]
nums = [int(''.join([re.findall('[0-9]', x)[0] + re.findall('[0-9]', x)[-1]])) for x in conv]


print(conv)
print(sum(nums))