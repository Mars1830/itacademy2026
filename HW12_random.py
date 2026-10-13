import random
from random import choice


# task1
def dice_roll():
    print(f"Dice roll: {random.randint(1,6)}")


#task 2
def password_generator():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sequence_length = 8
    sequence = "".join([choice(alphabet) for _ in range(sequence_length)])
    print(sequence)


# task 3
def random_method():
    http_methods = ["GET", "POST", "PUT", "DELETE"]
    return random.choice(http_methods)


# task 4
def shuffle_tests():
    tests = ["test_login", "test_logout", "test_add_to_cart", "test_checkout"]
    print(f"Original tests: {tests}")
    random.shuffle(tests)
    print(f"Shuffled tests: {tests}")


# task 5
def random_users():
    users = ["alice", "bob", "carol", "dave", "erin"]
    sample_size = 2
    sample = random.sample(users, sample_size)
    print(sample)


# task 6
def run_flaky_test():
    result = random.random()
    if result < 0.7:
        return "PASSED"
    else:
        return "FAILED"


# task 7
def lottery():
    all_numbers = [_ for _ in range(1, 49)]
    sample_size = 6
    lottery_ticket = random.sample(all_numbers, sample_size)
    print(f"Lottery ticket: {lottery_ticket}")


# task 8
def generate_test_data(n):
    data = [random.randint(0, 100) for _ in range(n)]
    return data


if __name__ == '__main__':
    dice_roll()
    password_generator()
    print(random_method())
    shuffle_tests()
    random_users()
    print(run_flaky_test())
    lottery()
    print(f"Test data: {generate_test_data(n=10)}")