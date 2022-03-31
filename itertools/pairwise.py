from itertools import pairwise

nums = [1, 2, 3, 4]
for x, y in pairwise(nums):
   print("{} + {} = {}".format(x, y, y-x))

# 2 - 1 = 1
# 3 - 2 = 1
# 4 - 3 = 1
