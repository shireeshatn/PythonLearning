import random


def generate_random_number(start, end):
    return random.randint(start, end)


def shuffle_list(input_list):
    random.shuffle(input_list)
    return input_list


def select_random_element(input_list):
    return random.choice(input_list)
