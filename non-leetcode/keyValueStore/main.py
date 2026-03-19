"""
Problem 3:
    Design a simple in-memory key-value store with
    get(key), set(key, value), and get_history(key) that returns all past values of a key.
"""


class KVStore:
    def __init__(self) -> None:
        self.buffer = {}

    def get(self, key):
        if key not in self.buffer:
            return None
        return self.buffer[key][-1]

    def set(self, key, val):
        if key not in self.buffer:
            self.buffer[key] = []
        self.buffer[key].append(val)

    def get_history(self, key):
        if key not in self.buffer:
            return []
        return list(self.buffer[key])


def main():
    store = KVStore()

    print(store.get("x"))
    print(store.get_history("x"))

    store.set("a", 1)
    store.set("b", 10)
    store.set("a", 2)
    store.set("a", 3)
    store.set("b", 20)

    print(store.get("a"))
    print(store.get("b"))

    print(store.get_history("a"))
    print(store.get_history("b"))

    store.set("c", 100)

    print(store.get("c"))
    print(store.get_history("c"))

    print(store.get("missing"))
    print(store.get_history("missing"))


if __name__ == "__main__":
    main()
