''' DYNAMIC PROGRAMMING --[COIN CHANGE]-min number of coin required to give the change amount'''
def coinchange(coins,amount):
	coins.sort()
	dp=[amount+1]*(amount+1)
	dp[0]=0
	for i in range(0,amount+1):
		for j in coins:
			if j<=i:
				dp[i]=min(dp[i],1+dp[i-j])
	return dp[amount] if dp[amount]<amount else -1
print(coinchange([1,2,5],46))