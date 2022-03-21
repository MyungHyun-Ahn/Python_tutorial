from math import pow

total = 90
spam = 90
none_spam = 0

GI = 1 - pow(spam/total, 2) - pow(none_spam/total, 2)

GI

GI1 = 0.266

GI2 = 0

(GI1 * 95 + GI2 * 90 ) / 185