#!/usr/bin/python3
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
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def playGame(n):
        primes = [i for i in range(2, n + 1) if isPrime(i)]
        player = 0
        while primes:
            p = primes.pop(0)
            player = (player + 1) % 2
            for i in range(p, n + 1, p):
                if i in primes:
                    primes.remove(i)
        return player

    winners = []
    for n in nums:
        winners.append(playGame(n))

    if winners.count(0) > winners.count(1):
        return "Maria"
    elif winners.count(1) > winners.count(0):
        return "Ben"
    else:
        return None
