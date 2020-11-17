# Imports
from random import gauss, seed
from math import sqrt, exp


def create_GBM(s0, mu, sigma):
    st = s0

    def generate_value():
        nonlocal st
        st *= exp((mu - 0.5 * sigma ** 2) * (1. / 365.) + sigma * sqrt(1. / 365.) * gauss(mu=0, sigma=1))
        return st

    return generate_value


if __name__ == "__main__":
    seed(1234)
    gbm = create_GBM(100, 0.1, 0.05)

    for _ in range(1000):
        st = gbm()
        print(st)
        if st >= 130.:
            print("Target reached, take profit.")
            break
    else:
        print("Did not reach target price.")

    print(st)
