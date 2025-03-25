# +----+----+----+
# | a1 | a2 | a3 |
# +----+----+----+
# As shown above. There are three grids. Each grid fill in a number(let's call a1, a2 and a3). Such that 0 ≤ a1, a2, a3 ≤ n, where n is given, and meet the following rules:
#
# - a1 + a2 is a multiple of 2;
# - a2 + a3 is a multiple of 3;
# - a1 + a2 + a3 is a multiple of 5;
# Your task is to find a set of a1, a2, a3, which makes a1 + a2 + a3 maximum. Returns the sum of a1, a2, a3.
#
# Input/Output
# [input] integer n
#
# A non-negative integer. It's the maximum possible value of a1, a2, a3.
#
# 0 ≤ n ≤ 10000
#
# [output] an integer
#
# The maximum sum of a1, a2, a3.
#
# Example
# For n = 0, the output should be 0.
#
# The possible value of a1, a2, a3 can be a1 = 0, a2 = 0, a3 = 0.
#
# For n = 3, the output should be 5.

def find_max_sum(n):
    sum = 0
    for i in range(0, 1000):
        sub_a1 = i % 10
        sub_a2 = (i // 10) % 10
        sub_a3 = (i // 100) % 10

        if sub_a1 <= n and sub_a2 <= n and sub_a3 <= n:
            new_a1 = n - sub_a1
            new_a2 = n - sub_a2
            new_a3 = n - sub_a3

            if (new_a1 + new_a2) % 2 == 0 and (new_a2 + new_a3) % 3 == 0 and (new_a1 + new_a2 + new_a3) % 5 == 0:
                if new_a1 + new_a2 + new_a3 > sum:
                    sum = new_a1 + new_a2 + new_a3
    return sum
