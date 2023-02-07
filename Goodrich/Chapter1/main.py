# NOTE TO VIEWERS: Other code snippets have been skipped as I found them too basic.

# Generators

# Traditional function that computes factors
def factors(n):                 # traditional function that computes factors
    results = []                # store factors in a new list
    for k in range(1, n + 1):
        if n % k == 0:          # divides evenly, thus k is a factor
            results.append(k)   # add k to the list of factors
    return results              # return the entire list


# Generator version of the same function
# noinspection PyRedeclaration
def factors(n):                 # generator that computes factors
    for k in range(1, n + 1):
        if n % k == 0:          # divides evenly, thus k is a factor
            yield k             # yield this factor as next result
