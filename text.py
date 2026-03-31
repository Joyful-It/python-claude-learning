INF = float('inf')

# 读取木板数量和查询次数
n, q = map(int, input().split())
boards = []

for _ in range(n):
    l, r = map(int, input().split())
    boards.append((l, r))

# 处理每个查询
for _ in range(q):
    a, b = map(int, input().split())
    # 初始化dp数组
    dp = [INF] * (b + 1)
    dp[a-1] = 0  # 覆盖到a-1时平方和为0
    
    # 动态规划过程
    for x in range(a-1, b):
        if dp[x] == INF:
            continue
        for l, r in boards:
            if l <= x + 1 and r >= x + 1:
                if r > b:
                    continue
                if dp[r] > dp[x] + (r - l + 1)**2:
                    dp[r] = dp[x] + (r - l + 1)**2
    
    # 输出结果
    print(dp[b] if dp[b] != INF else -1)