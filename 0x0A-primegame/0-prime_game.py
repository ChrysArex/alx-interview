#!/usr/bin/python3
"""This module define a fuction that return the winner of the prime game"""


def isWinner(x, nums):
    """For each number in nums the function execute the sieve of eratosthen
       and attribut each removal to Maria and Ben succesively. By doing so the
       function identify the winner for each turn and cummulate the points to
       have the final winner.
    """
    score = {"Maria": 0, "Ben": 0}
    for n in nums:
        numbers = list(range(1, n + 1))
        rocket = ["Maria", "Ben", ""]
        if len(numbers) > 1:
            while (len(numbers) != 1):
                print(rocket[0])
                target = numbers[1]
                for i in numbers[1:]:
                    if i % target == 0:
                        numbers.remove(i)
                rocket[2] = rocket[0]
                rocket[0] = rocket[1]
                rocket[1] = rocket[2]
            score[rocket[1]] += 1
        else:
            score["Ben"] += 1

    if score["Maria"] > score["Ben"]:
        return "Maria"
    elif score["Maria"] == score["Ben"]:
        return None
    else:
        return "Ben"
