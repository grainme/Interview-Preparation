"""
This week's question:
    Given a string s consisting only of 'a' and 'b', you may swap adjacent characters any number of times.

    Return the minimum number of adjacent swaps needed to transform s into an alternating string, either "ababab..." or "bababa...", or return -1 if it's impossible.

    Example:

    minSwapsToAlternate('aabb')
    > 1

    minSwapsToAlternate('aaab')
    > -1

    minSwapsToAlternate('aaaabbbb')
    > 6
"""


def is_alternating(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True


def minSwapsToAlternate(s: str) -> int:
    # we can add the base case here (count(a) > count(b)+1 ==> impossible)
    sl = list(s)
    swaps = 0
    for i, c in enumerate(sl):
        k = i + 1
        should_swap = False
        while k < len(sl) and sl[i] == sl[k]:
            should_swap = True
            k += 1

        if should_swap and k < len(sl):
            sl[i + 1], sl[k] = sl[k], sl[i + 1]
            swaps += k - i - 1

        if is_alternating(sl):
            return swaps

    return -1


def main():
    res = minSwapsToAlternate("aaab")
    print(res)

    res = minSwapsToAlternate("aabb")
    print(res)

    res = minSwapsToAlternate("aaaabbbb")
    print(res)

    res = minSwapsToAlternate("abababab")
    print(res)

    res = minSwapsToAlternate("babababa")
    print(res)

    res = minSwapsToAlternate("aabbaabb")
    print(res)


if __name__ == "__main__":
    main()
