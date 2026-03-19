"""
API Rate Limiter

Build a RateLimiter class that tracks API requests per user:

Requirements:

- Each user gets max_requests within a sliding window_seconds
- Old requests outside the window should expire (not block forever)
- allow(user_id) → returns True/False
- get_usage(user_id) → returns a dict with request count, remaining, and seconds until reset
- Handle users that have never made a request

Use time.time() for timestamps. No external libraries.
"""

from time import time
from typing import Dict


class UserUsage:
    def __init__(self, requests: int, resets_in: float) -> None:
        self.requests = requests
        self.resets_in = resets_in

    def __str__(self) -> str:
        return f"requests: {self.requests}\nresets_int: {self.resets_in}"


class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: float) -> None:
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.bucket: Dict[str, UserUsage] = {}

    def allow(self, user: str) -> bool:
        if user not in self.bucket:
            self.bucket[user] = UserUsage(1, time())
            return True

        user_usage = self.bucket[user]

        if time() - user_usage.resets_in > self.window_seconds:
            user_usage = self.bucket[user] = UserUsage(0, time())

        if user_usage.requests < self.max_requests:
            user_usage.requests += 1
            return True

        return False

    def get_usage(self, user: str) -> dict:
        if user not in self.bucket:
            return {
                "user": user,
                "requests": 0,
                "remaining": self.max_requests,
                "resets_in": 0,
            }

        user_usage = self.bucket[user]
        return {
            "user": user,
            "requests": user_usage.requests,
            "remaining": self.max_requests - user_usage.requests,
            "resets_in": self.window_seconds - (time() - user_usage.resets_in),
        }


def main():
    limiter = RateLimiter(max_requests=3, window_seconds=60)

    allowed = limiter.allow("user_1")  # True  (1st request)
    print(allowed)
    allowed = limiter.allow("user_1")  # True  (2nd)
    print(allowed)
    allowed = limiter.allow("user_1")  # True  (3rd)
    print(allowed)
    allowed = limiter.allow("user_1")  # False (exceeded limit)
    print(allowed)
    allowed = limiter.allow("user_2")  # True  (different user, own limit)
    print(allowed)

    usage = limiter.get_usage("user_1")
    print(usage)
    # {"user": "user_1", "requests": 3, "remaining": 0, "resets_in": 45}


if __name__ == "__main__":
    main()
