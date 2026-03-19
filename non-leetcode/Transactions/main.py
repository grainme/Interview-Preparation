"""
Problem 2:
    Write a function that takes a list of transactions [{"user": "alice", "amount": 50}, ...]
    - returns each user's total balance, sorted by balance descending.
"""

from typing import List


class UserTransaction:
    def __init__(self, user: str, amount: int) -> None:
        self.user = user
        self.amount = amount


def usersBalance(transactions: List[UserTransaction]):
    userB = {}
    for tr in transactions:
        if tr.user not in userB:
            userB[tr.user] = 0
        userB[tr.user] += tr.amount

    res = []
    for k in userB:
        res.append({"user": k, "balance": userB[k]})

    res.sort(key=lambda o: o["balance"], reverse=True)
    return res


def main():
    transactions = [
        UserTransaction("alice", 50),
        UserTransaction("bob", 30),
        UserTransaction("alice", 20),
        UserTransaction("bob", -10),
        UserTransaction("charlie", 40),
    ]

    _ = [
        {"user": "alice", "balance": 70},
        {"user": "charlie", "balance": 40},
        {"user": "bob", "balance": 20},
    ]

    actual = usersBalance(transactions)
    print(actual)


if __name__ == "__main__":
    main()
