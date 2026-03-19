"""
Problem 1:
    Given a list of log entries like "2024-03-15 ERROR Database connection failed".

    write a function that returns the count of each log level (ERROR, WARN, INFO)
    and the most recent error message.
"""

from typing import List


def logParsing(logs: List[str]):
    logsLevel = {"ERROR": 0, "WARN": 0, "INFO": 0}
    most_recent_error = ""

    for log in logs:
        logSplit = log.split()
        if "ERROR" in logSplit:
            logsLevel["ERROR"] += 1
            most_recent_error = log
        if "INFO" in logSplit:
            logsLevel["INFO"] += 1
        if "WARN" in logSplit:
            logsLevel["WARN"] += 1

    most_recent_error = " ".join(most_recent_error.split()[2:]) if most_recent_error != "" else ""

    return {
        "counts": logsLevel,
        "most_recent_error": most_recent_error,
    }


def main():
    logs = [
        "2024-03-14 INFO User logged in",
        "2024-03-15 ERROR Database connection failed",
        "2024-03-16 WARN Disk space low",
        "2024-03-17 ERROR Timeout occurred",
        "2024-03-18 INFO File uploaded",
    ]

    _ = {
        "counts": {"INFO": 2, "ERROR": 2, "WARN": 1},
        "most_recent_error": "Timeout occurred",
    }

    actual = logParsing(logs)
    print(actual)


if __name__ == "__main__":
    main()
