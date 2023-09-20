#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total.

    Prototype: def makeChange(coins, total)
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    coins is a list of the values of the coins in your possession
    The value of a coin will always be an integer greater than 0
    You can assume you have an infinite number of each denomination of coin
    in the list
    Your solution’s runtime will be evaluated in this task
"""


def makeChange(coins, total):
    """
    the aforementioned function
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for j in coins:
            if i - j >= 0:
                dp[i] = min(dp[i], 1 + dp[i - j])

    return dp[total] if dp[total] != total + 1 else -1
