import random

random.seed(1000)


def get_random_int():
    return random.randint(0, 100)


def get_random_dec():
    return 100 * random.random()


def get_random_int_list():
    random_lst = []
    for n in range(0, 1000):
        n = random.randint(0, 1000)
        random_lst.append(n)
        return random_lst


def get_random_float_list():
    random_lst = []
    for n in range(0, 1000):
        n = 1000 * random.random()
        random_lst.append(n)
        return random_lst
