from sys import stdin

lines = [l.strip() for l in stdin.readlines()]

len_n, nums = int(lines[0]), [int(s) for s in lines[1].split()]

# print(len_n, nums)

dp = []

dp.append(nums[0])
for i in range(1, len_n):
    if dp[i - 1] == 0:
        dp.append(nums[i])
    else: 
        dp.append(dp[i - 1] * nums[i])
print(dp)

neg = 0
zero = 0
pos = 0

for l in range(len_n):
    for r in range(l, len_n):
        if l == 0 or dp[l - 1] == 0:
            prod = dp[r]
        else:
            prod = dp[r] / dp[l - 1]
        if prod < 0: neg += 1
        if prod == 0: zero += 1
        if prod > 0: pos += 1

print(neg, zero, pos)


