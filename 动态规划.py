def coin_change_dp(coins, amount):
    """
    动态规划求解最少硬币数

    思路：
    1. 定义 dp[i] = 凑出 i 元需要的最少硬币数
    2. 初始：dp[0] = 0，其他 dp[i] = 无穷大（表示暂时不可达）
    3. 状态转移：dp[i] = min(dp[i - c] + 1) 对所有 c in coins 且 c <= i
    4. 最终答案：dp[amount]（如果是无穷大则返回 -1）
    """

    # 1. 初始化 dp 数组
    # 长度 = amount + 1（需要索引 0 到 amount）
    # 初始值设为正无穷，表示暂时无法凑出
    dp = [float("inf")] * (amount + 1)

    # 凑 0 元需要 0 枚硬币（基础情况）
    dp[0] = 0

    # 2. 自底向上计算每个金额的最小硬币数
    # 从 1 元开始，一直计算到目标金额
    for i in range(1, amount + 1):
        # 尝试每一种硬币作为"最后一枚"
        for c in coins:
            # 只有硬币面额 <= 当前金额时才有意义
            if c <= i:
                # 状态转移：用这枚硬币，之前需要凑 i-c 元
                # dp[i-c] 是凑 i-c 元的最少硬币数
                # +1 是加上当前这枚硬币
                dp[i] = min(dp[i], dp[i - c] + 1)

    # 3. 返回结果
    if dp[amount] == float("inf"):
        return -1  # 无法凑出
    else:
        return dp[amount]


# ========== 测试代码 ==========
if __name__ == "__main__":
    # 测试用例1：标准情况
    coins1 = [10, 9, 1]
    amount1 = 18
    result1 = coin_change_dp(coins1, amount1)
    print(f"硬币面额: {coins1}, 目标金额: {amount1}")
    print(f"最少硬币数: {result1}")  # 输出 2（两个9元）
    print()

    # 测试用例2：贪心会失败的情况
    coins2 = [10, 9, 1]
    amount2 = 27
    result2 = coin_change_dp(coins2, amount2)
    print(f"硬币面额: {coins2}, 目标金额: {amount2}")
    print(f"最少硬币数: {result2}")  # 输出 3（三个9元，贪心会拿两个10+七个1=9枚）
    print()

    # 测试用例3：无法凑出
    coins3 = [10, 5]
    amount3 = 3
    result3 = coin_change_dp(coins3, amount3)
    print(f"硬币面额: {coins3}, 目标金额: {amount3}")
    print(f"最少硬币数: {result3}")  # 输出 -1（无法凑出）
    print()

    # 测试用例4：最小硬币不是1
    coins4 = [10, 9, 5]
    amount4 = 18
    result4 = coin_change_dp(coins4, amount4)
    print(f"硬币面额: {coins4}, 目标金额: {amount4}")
    print(f"最少硬币数: {result4}")  # 输出 2（两个9元）
    print()

    # 测试用例5：金额为0
    coins5 = [1, 2, 5]
    amount5 = 0
    result5 = coin_change_dp(coins5, amount5)
    print(f"硬币面额: {coins5}, 目标金额: {amount5}")
    print(f"最少硬币数: {result5}")  # 输出 0
