# Data Structures and Algorithms (Python)

A repository for practicing DS/Algo in Python, based on 
Rance D. Necaise<sup>[^1](#Ran11)</sup> and Michael T. Goodrich et al.<sup>[^2](#Mic13)</sup>   

### Contents

| Folders    | Corresponding Directories            [^1](#Ran11) | [^2](#Mic13)                                            |
|:-----------|:--------------------------------------------------|:--------------------------------------------------------|
| Chapter 1  | [Abstract Data Types](RDNecaise/Chapter1)         | [Python Primer](Goodrich/Chapter1)                      |
| Chapter 2  | [Arrays](RDNecaise/Chapter2)                      | [Object-Oriented Programming](Goodrich/Chapter2)        |
| Chapter 3  | [Sets and Maps](RDNecaise/Chapter3)               | [Algorithm Analysis](Goodrich/Chapter3)                 |
| Chapter 4  | Algorithm Analysis                                | [Recursion](Goodrich/Chapter4)                          |
| Chapter 5  | [Searching and Sorting](RDNecaise/Chapter5)       | [Array-Based Sequences](Goodrich/Chapter5)              |
| Chapter 6  | [Linked Structures](RDNecaise/Chapter6)           | [Stacks, Queues, and Deques](Goodrich/Chapter6)         |
| Chapter 7  | [Stacks](RDNecaise/Chapter7)                      | [Linked Lists](Goodrich/Chapter7)                       |
| Chapter 8  | [Queues](RDNecaise/Chapter8)                      | [Trees](Goodrich/Chapter8)                              |
| Chapter 9  | Advanced Linked Lists                             | [Priority Queues](Goodrich/Chapter9)                    |
| Chapter 10 | Recursion                                         | [Maps, Hash Tables, and Skip Lists](Goodrich/Chapter10) |
| Chapter 11 | Hash Tables                                       | [Search Trees](Goodrich/Chapter11)                      |
| Chapter 12 | [Advanced Sorting](RDNecaise/Chapter12)           | [Sorting and Selection](Goodrich/Chapter12)             |
| Chapter 13 | [Binary Trees](RDNecaise/Chapter13)               | [Text Processing](Goodrich/Chapter13)                   |
| Chapter 14 | [Search Trees](RDNecaise/Chapter14)               | [Graph Algorithms](Goodrich/Chapter14)                  |
| Chapter 15 |                                                   | Memory Management and B-Trees                           |

## Getting Started

After cloning the repository, you may run the programs using **PyCharm** or an IDE/editor of your choice. 

### Release Notes

- Python 3.6 is used up until commit [`36f2d11`](https://github.com/awwalm/DSAlgoPy/commit/36f2d11). 
Subsequent commits use Python 3.10 (or higher) features.

- Commit [`4466df5`](https://github.com/awwalm/DSAlgoPy/commit/4466df5) uses `__future__.annotations`<sup>[^3](#Ofpy3)</sup> 
to set recursive type-hinting (requires Python 3.7 or higher).

- [`progression.py`](Goodrich/Chapter2/progression.py) uses the `@override` decorator<sup>[^4](#Kor23)</sup> to emphasize polymorphism.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [GNU GPL v3](https://choosealicense.com/licenses/gpl-3.0/) License.

## Acknowledgments

* Hat tip to anyone whose code was used

## References

1. Necaise, R. D. (2011). <a id="Ran11" href="https://www.amazon.com/Data-Structures-Algorithms-Using-Python/dp/0470618299">
_Data Structures and Algorithms using Python_</a>. Hoboken, NJ, USA: Wiley.

2. Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2013). <a id="Mic13" href="https://www.wiley.com/en-us/Data+Structures+and+Algorithms+in+Python-p-9781118290279">
_Data Structures and Algorithms in Python_.</a> (B. L. Golub, Ed.) Hoboken, NJ, USA: Wiley.

3. <span id="Ofpy3">"**`__future__`** Statement Definitions. Retreived from the Official Python Documentation: </span> 
https://docs.python.org/3.11/library/__future__.html

4. <span id="Kor23">Korpela, M. (6 August 2023). `overrides`</span>. Retrieved from PyPI: https://pypi.org/project/overrides/

5. Stroud, K. A., & Booth, D. J. (2020). [_Engineering Mathematics_](
https://www.amazon.com/Engineering-Mathematics-K-Stroud/dp/1352010275) (8th ed.). 
London, UK: Red Globe Press (Macmillian).

6. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). 
[_Introduction to Algorithms_](https://dl.acm.org/doi/10.5555/1614191) 
(3rd ed.). Massachussetts, USA: MIT Press.

7. Lutz, M. (2013). [_Learning Python_](https://www.oreilly.com/library/view/learning-python-5th/9781449355722/) 
(5th ed.). Sebastopol, CA, USA: O'Reilly Media, Inc.

8. Levitin, A. (2012). [_Introduction To The Design & Analysis of Algorithms_](
https://www.amazon.com/Introduction-Design-Analysis-Algorithms-3rd/dp/0132316811) (3rd ed.). 
Essex, UK: Pearson Education.

9. Gusfield, D. (1997). [_Algorithms on Strings, Trees and Sequences: Computer Science and Computational Biology_](
https://doi.org/10.1017/CBO9780511574931). Cambridge University Press.

10. Tustumi, W. H. A., Gog, S., Telles, G. P., & Louza, F. A. (2016). 
[_An improved algorithm for the all-pairs suffixprefix problem_](https://dx.doi.org/10.1016/j.jda.2016.04.002). 
Journal of Discrete Algorithms, 37(C), 34–43.

11. Kim, D.K., Kim, M. & Park, H. [_Linearized Suffix Tree: an Efficient Index Data Structure 
with the Capabilities of Suffix Trees and Suffix Arrays_](https://doi.org/10.1007/s00453-007-9061-2). 
Algorithmica 52, 350–377 (2008).

12. Nong, G., Zhang, S., & Chan, W. H. (2009). _Linear SAIS (Suffix Array Construction by Almost Pure Induced-Sorting)_. 
2009 Data Compression Conference (pp. 193-202). Snowbird, UT, USA: IEEE. 
[doi:10.1109/DCC.2009.42](https://ieeexplore.ieee.org/document/4976463)

13. Li, Z., Li, J., & Huo, H. (2018). _Optimal In-Place Suffix Sorting._ Tsinghua University, IIIS. 
Beijing: arXiv. [arXiv:1610.08305v6](https://arxiv.org/abs/1610.08305)

14. Guruprasad, H. S. (25 June 2020). _Horspool Algorithm_. 
Retrieved from YouTube: https://www.youtube.com/watch?v=W4h6555g5qo

15. Kettani, H. (2024). [Space & Time Tradeoffs: Boyer-Moore Algorithm](
https://www.collegesidekick.com/study-docs/4797428). _CSC 3323 Analysis of Algorithms_. Morocco.

16. Ramesh, B. (21 April 2020). _Boyer-Moore-Horspool Algorithm_.
Retrieved from YouTube: https://youtu.be/4Oj_ESzSNCk

17. Langmead, Ben. (2024). Suffix-based indexing data structures: learning materials. figshare. Collection. 
[https://doi.org/10.6084/m9.figshare.c.7205547](https://www.youtube.com/playlist?list=PL2mpR0RYFQsDFNyRsTNcWkFTHTkxWREeb)

18. Harris, E. (27 March 2020). _SAIS (Suffix Array Induced Sorting) Part 1_.
Retrieved from YouTube: https://www.youtube.com/watch?v=yb0Os_MTU_4

19. [Trie - Wikipedia](https://en.wikipedia.org/wiki/Trie)

20. [Suffix Tree - Wikipedia](https://en.wikipedia.org/wiki/Suffix_tree)

21. [Suffix Array - Wikipedia](https://en.wikipedia.org/wiki/Suffix_array)

22. [LCP Array - Wikipedia](https://en.wikipedia.org/wiki/LCP_array)

23. [Suffix Array and LCP Generator](https://visualgo.net/en/suffixarray)

24. [Ukkonen Visualizer](http://brenden.github.io/ukkonen-animation/)

25. [Applications of Suffix Array and LCPs](https://mediathek.hhu.de/watch/b4d092e2-06ba-4786-abe4-7ffc614b2244#)
