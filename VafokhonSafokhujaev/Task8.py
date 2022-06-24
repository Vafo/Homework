def get_pairs(lst: list) -> list[tuple]:
    if len(lst) < 2:
        return None

    first = lst[:-1]
    second = lst[1:]

    return [ el for el in zip(first, second)]

tmp = get_pairs(['need', 'to', 'sleep', 'more'])

print(tmp)