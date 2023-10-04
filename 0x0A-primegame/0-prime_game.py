#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n, they take turns choosing a prime
number from the set and removing that number and its multiples from the set.
The player that cannot make a move loses the game.
"""


def isWinner(x, nums):
    """
    Determines the winner of the Maria and Ben game.

    Args:
        x: The number of rounds.
        nums: An array of integers starting from 1 up to and including n.

    Returns:
        The name of the player that won the most rounds, or None if the
        winner cannot be determined.
    """
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not sieve[i]:
            continue
        for j in range(i*i, n + 1, i):
            sieve[j] = False

    sieve[0] = sieve[1] = False
    c = 0
    for i in range(len(sieve)):
        if sieve[i]:
            c += 1
        sieve[i] = c

    player1 = 0
    for n in nums:
        player1 += sieve[n] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
