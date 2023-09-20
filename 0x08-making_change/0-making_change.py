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
    dp = [[0] * (total + 1) for _ in range(len(coins))]
    dp[0][0] = 0
    for i in range(len(coins)):
        for j in range(i + 1, total + 1):
            dp[i][j] = min(dp[i][j], dp[i - 1][j - coins[i]] + 1)
    if dp[len(coins) - 1][total] == 0:
        return -1
    return dp[len(coins) - 1][total]
