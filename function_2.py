import random
#if 1 tree return a rnd number in domain, if multiple make a list
a = random.uniform(y[0], y[1]) if x == 1 else [random.uniform(y[0], y[1]) for i in range(0, x)]