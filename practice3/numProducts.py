from sys import stdin

lines = [l.strip() for l in stdin.readlines()]

n, nums = int(lines[0]), [int(s) for s in lines[1].split()]

dp = [[0, 0, 0] for _ in range(n)]

if nums[0] > 0:
    dp[0][0] += 1
elif nums[0] == 0:
    dp[0][1] += 1
else:
    dp[0][2] += 1

for i, num in enumerate(nums):
    if i > 0:
        if num > 0:
            dp[i][0] += 1
            dp[i][0] += dp[i - 1][0]
            dp[i][1] += dp[i - 1][1]
            dp[i][2] += dp[i - 1][2]
        elif num == 0:
            dp[i][1] += 1
            dp[i][1] += dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]
        else:
            dp[i][2] += 1
            dp[i][0] += dp[i - 1][2]
            dp[i][1] += dp[i - 1][1]
            dp[i][2] += dp[i - 1][0]

numPositive = sum([x for x, _, _ in dp])
numZero = sum([x for _, x, _ in dp])
numNegative = sum([x for _, _, x in dp])

print(numNegative, numZero, numPositive)
