#!/usr/bin/python3
"""This function determine the winner of the game"""


def SieveOfEratosthenes(n):
    """Determine the number of prime number before n"""
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] is True):
            for i in range(p * p, n+1, p):
                prime[i] = False
                p += 1
    values = []
    for p in range(2, n+1):
        if prime[p]:
            values.append(p)
    return values


def isWinner(x, nums):
    """Determine the winner"""
    score = {"Maria": 0, "Ben": 0}
    for i in range(x):
        n = len(SieveOfEratosthenes(nums[i]))
        if n % 2 == 0:
            score["Ben"] += 1
        else:
            score["Maria"] += 1
    if score["Maria"] > score["Ben"]:
        return "Maria"
    return "Ben"
