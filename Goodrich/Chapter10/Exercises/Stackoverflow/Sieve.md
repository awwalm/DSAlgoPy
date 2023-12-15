## Empirical Analysis and Visualization of Various Approaches to the Sieve of Eratosthenes

I discovered this algorithm at the end of the 10<sup>th</sup> chapter (_Maps, Hash Tables, and Skip Lists_)
of ["Data Structures & Algorithms in Python"][1]. I ended up writing three versions:

- A naive implementation with a nasty cubic runtime (amongst many other issues, later resolved).
- A suboptimal version after some [thorough research][2], but I still wanted to get rid of the square-based multiples.
- A fast and efficient version on par with the [selected answer][3] performance-wise, but with additive multiples (more intuitive for those less-mathematically inclined).

### Naive SOE

Out of all the issues, the additional space usage in the return statement takes the cake as the worst.
```python
def naive_sieve(m: int):
    BA = [True] * m
    for i, k in zip(range(2, m + 1), range(len(BA))):
        if BA[k] is False: continue
        for j in range(2, i):
            if i % j == 0:
                BA[k] = False
                f = k + j
                while f < len(BA):
                    BA[f] = False
                    f += j
                break
    return [i for i,j in zip(range(2, m + 1), BA) if j is True]
```

### Suboptimal SOE

A drastic improvement, but still lacking on space usage, and an unfriendly inner-loop interval progression.
```python
def suboptimal_sieve(m: int):
    BA = [True] * m
    for i, k in zip(range(2, m + 1), range(2, len(BA))):
        if BA[k] is False: continue
        for j in range(i**2, m, i):
            BA[j] = False
    return [i for i,j in zip(range(2, m + 1), BA[2:]) if j is True]
```

### Fast SOE

Easy to understand (note the usage of fractional exponent to be explicitly consistent with the mathematical definition of roots)
and just as performant as @Pi Delport's answer.
```python
def fast_sieve(m: int):
    BA = [True] * m
    rtm = int(m**(1/2)) + 1
    for i in range(2, len(BA)):
        if BA[i]:
            yield i
            if i < rtm:
                f = i
                while f < len(BA):
                    BA[f] = False
                    f += i
```

### Empirical Analysis

To compare all three implementations, along with the selected answer from @Pi Delport, 
I ran it through 45 iterations from primes in range 100, until primes in range 4500, at intervals of 100
(that's the sweet spot for the visualization, because despite the consistency of the shape of the graphs,
the growth of the naive implementation dwarves the visibility of the other three). 
You can tweak the visualization code on the [GitHub gist][4], but here's one sample output:

![Empirical Analysis and Visualization of Various Approaches to the Sieve of Eratosthenes
][5]

<!-- References -->
  [1]: https://www.wiley.com/en-us/Data+Structures+and+Algorithms+in+Python-p-9781118290279

  [2]: https://www.youtube.com/watch?v=pKvGYOnO9Ao&

  [3]: https://stackoverflow.com/a/3941967/13488161 

  [4]: https://gist.github.com/awwalm/ea56394332880af846e942733670dec0#file-sieve-py

  [5]: https://i.stack.imgur.com/2JSU1.png