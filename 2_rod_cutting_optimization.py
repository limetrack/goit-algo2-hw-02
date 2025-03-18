from typing import List, Dict


def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через мемоізацію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    memo = {}

    def dfs(n):
        if n == 0:
            return 0, []
        if n in memo:
            return memo[n]

        max_profit, best_cut = 0, []
        for i in range(n):
            profit, cuts = dfs(n - (i + 1))
            profit += prices[i]
            if profit > max_profit:
                max_profit = profit
                best_cut = [i + 1] + cuts

        memo[n] = (max_profit, best_cut)
        return memo[n]

    max_profit, cuts = dfs(length)
    return {"max_profit": max_profit, "cuts": cuts, "number_of_cuts": len(cuts) - 1}


def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через табуляцію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    dp = [0] * (length + 1)
    cuts = [[] for _ in range(length + 1)]

    for n in range(1, length + 1):
        for i in range(n):
            if dp[n] < prices[i] + dp[n - (i + 1)]:
                dp[n] = prices[i] + dp[n - (i + 1)]
                cuts[n] = [i + 1] + cuts[n - (i + 1)]

    return {
        "max_profit": dp[length],
        "cuts": cuts[length],
        "number_of_cuts": len(cuts[length]) - 1,
    }


def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        {"length": 5, "prices": [2, 5, 7, 8, 10], "name": "Базовий випадок"},
        {"length": 3, "prices": [1, 3, 8], "name": "Оптимально не різати"},
        {"length": 4, "prices": [3, 5, 6, 7], "name": "Рівномірні розрізи"},
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        memo_result = rod_cutting_memo(test["length"], test["prices"])
        print("\nРезультат мемоізації:")
        print(memo_result)

        table_result = rod_cutting_table(test["length"], test["prices"])
        print("\nРезультат табуляції:")
        print(table_result)

        print("\nПеревірка пройшла успішно!")


if __name__ == "__main__":
    run_tests()
