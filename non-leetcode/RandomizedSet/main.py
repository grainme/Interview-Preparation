"""
Implement RandomizedSet class

- RandomizedSet() init the RandomizedSet object
- bool insert(int val): inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
- bool remove(int val): Removes an item val from the set if present. Returns true if the item was present, false othewise.
- int getRandom(): Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.
"""

from random import randint


class RandomizedSet:
    def __init__(self) -> None:
        self.dict = {}
        self.bucket = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.bucket.append(val)
        self.dict[val] = len(self.bucket) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        ind = self.dict[val]
        self.dict[self.bucket[-1]] = ind
        self.bucket[ind] = self.bucket[-1]
        self.bucket.pop()
        self.dict.pop(val)
        return True

    def getRandom(self) -> int:
        random_index = randint(0, len(self.bucket) - 1)
        return self.bucket[random_index]


def main():
    st = RandomizedSet()
    st.insert(5)
    st.insert(9)
    st.insert(2)
    st.remove(3)
    print(st.getRandom())


if __name__ == "__main__":
    main()
