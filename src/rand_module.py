import random


def get_random_id():
    return random.randint(0, 100000000)


def get_random_iterable_item(smth_iterable):
    return smth_iterable.__getitem__(
        random.randint(0, len(smth_iterable) - 1)
    )

