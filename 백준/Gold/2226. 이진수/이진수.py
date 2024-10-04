n = int(input())
dp = [0];
for i in range(1, n):
    dp.append(2 ** (i - 1) - dp[i - 1])
print(dp[n - 1])