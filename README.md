# Data Structures and Algorithms (Python)

A repository for practicing DS/Algo in Python using resources from 
Rance D. Necaise<span title="Rance D. Necaise - Data Structures and Algorithms using Python">[^1]</span>,
as well as Michael T. Goodrich et al.<span title="Michael T. Goodrich, Roberto Tamassia & Michael H. Goldwasser - Data Structures & Algorithms in Python">[^2]</span>.

### Contents

| Folders    | Corresponding Directories            [^1] | [^2]                                                    |
|:-----------|:------------------------------------------|:--------------------------------------------------------|
| Chapter 1  | [Abstract Data Types](RDNecaise/Chapter1) | [Python Primer](Goodrich/Chapter1)                      |
| Chapter 2  | [Arrays](RDNecaise/Chapter2)              | [Object-Oriented Programming](Goodrich/Chapter2)        |
| Chapter 3  | [Sets and Maps](RDNecaise/Chapter3)       | [Algorithm Analysis](Goodrich/Chapter3)                 |
| Chapter 4  | Algorithm Analysis                        | [Recursion](Goodrich/Chapter4)                          |
| Chapter 5  | Searching and Sorting                     | [Array-Based Sequences](Goodrich/Chapter5)              |
| Chapter 6  | [Linked Structures](RDNecaise/Chapter6)   | [Stacks, Queues, and Deques](Goodrich/Chapter6)         |
| Chapter 7  | [Stacks](RDNecaise/Chapter7)              | [Linked Lists](Goodrich/Chapter7)                       |
| Chapter 8  | [Queues](RDNecaise/Chapter8)              | [Trees](Goodrich/Chapter8)                              |
| Chapter 9  | Advanced Linked Lists                     | [Priority Queues](Goodrich/Chapter9)                    |
| Chapter 10 | Recursion                                 | [Maps, Hash Tables, and Skip Lists](Goodrich/Chapter10) |
| Chapter 11 | Hash Tables                               | [Search Trees](Goodrich/Chapter11)                      |
| Chapter 12 | Advanced Sorting                          | Sorting and Selection                                   |
| Chapter 13 | [Binary Trees](RDNecaise/Chapter13)       | Text Processing                                         |
| Chapter 14 | [Search Trees](RDNecaise/Chapter14)       | Graph Algorithms                                        |
| Chapter 15 |                                           | Memory Management and B-Trees                           |

## Getting Started

After cloning the repository, you may run the programs using **PyCharm** or an IDE/editor of your choice. 

### Release Notes

- Python 3.6 is used up until commit [`36f2d11`](https://github.com/awwalm/DSAlgoPy/commit/36f2d11). 
Subsequent commits use Python 3.10 (or higher) features.

- Commit [`4466df5`](https://github.com/awwalm/DSAlgoPy/commit/4466df5) uses 
<span title=" __future__ — Future Statement Definitions - Official Python Documentation">`__future__.annotations`[^3]</span> 
to set recursive type-hinting (requires Python 3.7 or higher).

- [`progression.py`](Goodrich/Chapter2/progression.py) uses the `@override` decorator[^4] to emphasize polymorphism.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [GNU GPL v3](https://choosealicense.com/licenses/gpl-3.0/) License.

## Acknowledgments

* Hat tip to anyone whose code was used

<!-- Footnotes -->

[^1]: **Rance D. Necaise** - [Data Structures and Algorithms using Python](
                            https://www.amazon.com/Data-Structures-Algorithms-Using-Python/dp/0470618299)

[^2]: **Michael T. Goodrich, Roberto Tamassia & Michael H. Goldwasser** - [Data Structures & Algorithms in Python](
                            https://www.wiley.com/en-us/Data+Structures+and+Algorithms+in+Python-p-9781118290279)

[^3]: **`__future__` — Future Statement Definitions** - [Official Python Documentation](
                            https://docs.python.org/3.11/library/__future__.html)

[^4]: **Mikko Korpela** - [`overrides` — PyPI](
                            https://pypi.org/project/overrides/)
