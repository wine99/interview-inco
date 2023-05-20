from functools import cache


def plan(profile: list[tuple[str, float, float]], target, price):
    """
    Returns a plan with the total profit and cost. Format of plan: [(str, float, float)]
    """

    @cache
    def choose(max_idx, target) -> tuple[list[float], float]:
        """
        Returns a plan and the total profit
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
    plan, total_profit = choose(len(profile) - 1, target)
    costs = map(lambda p: p[2], profile)
    total_cost = sum(map(lambda p_c: p_c[0] * p_c[1], zip(plan, costs)))
    return {
        "plan": list(zip(list(map(lambda p: p[0], profile)), plan, strict=True)),
        "total_production": sum(plan),
        "total_cost": total_cost,
        "total_profit": total_profit,
    }
