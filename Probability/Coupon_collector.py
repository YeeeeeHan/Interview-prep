import random

def number_of_coupons(n):
    """
    :param n: number of coupons to be collected
    :return: number of draws to collect all coupons
    """
    collected = set()
    tries = 0
    coupon_list = random.sample(range(1, n + 1), n)


    while True:
        if len(collected) == n:             # break if collected all coupons
            break

        draw = random.choice(coupon_list)   # Get a random coupon from the list of coupons

        if draw not in collected:           # Add uncollected draw
            collected.add(draw)

        tries += 1                          # Increment number of tries

    return tries


if __name__ == '__main__':
    trials = 0
    for i in range (0,1000):    # Repeat trial for 1000 times
        trials += number_of_coupons(5)
    print(f"Expected number of tries to collect all coupons = {trials/1000}")      # Average number of tries