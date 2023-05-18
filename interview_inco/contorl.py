from functools import cache


def control(
    profile: list[tuple[str, float, float]], target, price
) -> tuple[list[tuple[str, float]], float]:
    """
    Returns a plan the max profit. Format of plan: [(str, float)]
    """

    @cache
    def choose(max_idx, target) -> tuple[list[float], float]:
        """
        Returns a plan and the max profit
        """
        if max_idx == 0:
            if capacities[0] <= target and profits[0] > 0:
                return [capacities[0]], profits[0]
            else:
                return [0], 0

        # Never turn on a non-profitable turbine nor a too powerful one
        if profits[max_idx] <= 0 or capacities[max_idx] > target:
            plan_n, profit_n = choose(max_idx - 1, target)
            return plan_n + [0], profit_n

        # Turn on max_turbinx_idx
        plan_y, profit_y = choose(max_idx - 1, target - capacities[max_idx])
        # Not turn on max_turbinx_idx
        plan_n, profit_n = choose(max_idx - 1, target)
        if profit_y + profits[max_idx] > profit_n:
            return plan_y + [capacities[max_idx]], profit_y + profits[max_idx]
        else:
            return plan_n + [0], profit_n

    capacities = list(map(lambda p: p[1], profile))
    profits = list(map(lambda p: p[1] * (price - p[2]), profile))
    plan, max_profit = choose(len(profile) - 1, target)
    return list(zip(list(map(lambda p: p[0], profile)), plan, strict=True)), max_profit
