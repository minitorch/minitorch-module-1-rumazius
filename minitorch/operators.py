"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


def mul(x, y):
    return x * y


def id(x):
    return x


def add(x, y):
    return x + y


def neg(x):
    return -x


def lt(x, y):
    return x < y


def eq(x, y):
    return x == y


def max(x, y):
    return y if lt(x, y) else x


def is_close(x, y):
    return abs(x - y) < 1e-2


def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x)) if x >= 0 else math.exp(x) / (1.0 + math.exp(x))


def relu(x):
    return (x > 0) * x


def log(x):
    return math.log(x)


def exp(x):
    return math.exp(x)


def inv(x):
    return 1.0 / x


def relu_back(x, y):
    return (x > 0) * y


def log_back(x, y):
    return y / x


def inv_back(x, y):
    return -y / (x**2)


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


def map(fn, lst):
    return [fn(x) for x in lst]


def zipWith(fn, lst1, lst2):
    return [fn(x, y) for x, y in zip(lst1, lst2)]


def reduce(fn, lst, fst_val):
    res = fst_val
    for x in lst:
        res = fn(res, x)
    return res


def negList(lst):
    return map(neg, lst)


def addLists(lst1, lst2):
    return zipWith(add, lst1, lst2)


def sum(lst):
    return reduce(add, lst, 0)


def prod(lst):
    return reduce(mul, lst, 1)


# TODO: Implement for Task 0.3.
