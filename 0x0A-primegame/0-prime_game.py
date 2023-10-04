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

    # Initialize the winners' scores.
    maria_wins = 0
    ben_wins = 0

    # Play each round of the game.
    for i in range(x):
        # Maria always goes first.
        maria_move = find_next_prime(nums)
        if maria_move is None:
            ben_wins += 1
            break

        # Remove Maria's move and its multiples from the set.
        remove_multiples(nums, maria_move)

        # Ben's move.
        ben_move = find_next_prime(nums)
        if ben_move is None:
            ben_wins += 1
            break

        # Remove Ben's move and its multiples from the set.
        remove_multiples(nums, ben_move)

    # Determine the winner.
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def find_next_prime(nums):
    """
    Finds the next prime number in the given array of integers.

    Args:
        nums: An array of integers.

    Returns:
        The next prime number in the array, or None if there are no prime
        numbers left.
    """

    for num in nums:
        if is_prime(num):
            return num

    return None


def remove_multiples(nums, prime):
    """
    Removes all multiples of the given prime number from the given array of
    integers.

    Args:
        nums: An array of integers.
        prime: A prime number.
    """

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] % prime == 0:
            nums.remove(nums[i])


def is_prime(num):
    """
    Checks if the given number is a prime number.

    Args:
        num: An integer.

    Returns:
        True if the number is prime, False otherwise.
    """

    if num <= 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True
