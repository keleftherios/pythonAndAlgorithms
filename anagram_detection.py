from collections import defaultdict, Counter


def anagram_detection_v1(str1: str, str2: str) -> bool:
    dict1 = dict()
    dict2 = dict()

    for letter in str1:
        if letter not in dict1:
            dict1[letter] = 1
        else:
            dict1[letter] += 1

    for letter in str2:
        if letter not in dict2:
            dict2[letter] = 1
        else:
            dict2[letter] += 1

    return dict1 == dict2


def anagram_detection_v2(str1: str, str2: str) -> bool:
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)

    for letter in str1:
        dict1[letter] += 1

    for letter in str2:
        dict2[letter] += 1

    return dict1 == dict2


def anagram_detection_v3(str1: str, str2: str) -> bool:
    dict1 = defaultdict(int)

    for letter in str1:
        dict1[letter] += 1

    for letter in str2:
        dict1[letter] -= 1

    return set(dict1.values()) == {0}


def hash_func(astring: str, tablesize: int) -> int:
    asum = 0
    for pos in range(len(astring)):
        asum += ord(astring[pos])
    return asum % tablesize


def anagram_detection_v4(str1: str, str2: str) -> bool:
    """
    Book solution
    """
    table_size = 11
    return hash_func(str1, table_size) == hash_func(str2, table_size)


def anagram_detection_v5(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)


def anagram_detection_v6(str1: str, str2: str) -> bool:
    return Counter(str1) == Counter(str2)


def test_anagram_detection(functions):

    test1 = ("python", "typhon")
    test2 = ("marina", "aniram")
    test3 = ("google", "gouglo")
    test4 = ("buffy", "bffyu")
    test5 = ("buffy", "bffya")
    test6 = ("listen", "silent")
    test7 = ("bad", "dad")

    tests = [test1, test2, test3, test4, test5, test6, test7]
    exp_results = [True, True, False, True, False, True, False]

    for function in functions:
        for test, expected_result in zip(tests, exp_results):
            result = function(*test)
            assert result == expected_result, \
                f"function: {function.__name__} -- args: {test} -- exp_result: {expected_result} vs result: {result}"
            print(f"function: {function.__name__} -- args: {test} -- result: {result}")
        print()

            

if __name__ == "__main__":

    functions_under_test = [anagram_detection_v1, anagram_detection_v2,
                            anagram_detection_v3, anagram_detection_v4,
                            anagram_detection_v5, anagram_detection_v6]

    test_anagram_detection(functions_under_test)


