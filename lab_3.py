first = [1, 2, 3, 4, 5]
second = ["1", "2", "3", "4", "5"]


def returndict (keys, values):

    dictionary = {keys: keys for keys in range(len(values)+1)}
    return dictionary

print(returndict(first, second))