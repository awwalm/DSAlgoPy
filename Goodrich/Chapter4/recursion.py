"""Four fundamental examples of recursion.

- Factorial:     A function n! defined as n * n-1 * n-2 * ... * 2 * 1.
- English Ruler: Recursive pattern of fractal structure.
- Binary Search: Allows efficient location of desired value in a set with upwards of billion entries.
- File System:   Nested directories.
"""

import os


def factorial(n):  										# Factorial
    return 1 if n == 0 else n * factorial(n - 1)


def draw_line(tick_length, tick_label=""):  			# English ruler
    """Draw one line with given tick length (followed by optional label)."""
    line = "-" * tick_length
    if tick_label:
        line += " " + tick_label
    print(line)


def draw_interval(center_length):  						# Supporting function for English ruler.
    """Draw tick interval based upon a central tick length."""
    if center_length > 0:  								# Stop when length drops to 0.
        draw_interval(center_length - 1)  				# Recursively draw top ticks.
        draw_line(center_length)  						# Draw center tick.
        draw_interval(center_length - 1)  				# Recursively draw bottom ticks.


def draw_ruler(num_inches, major_length):  				# Supporting function for English ruler.
    """Draw English ruler with given number of inches, major tick length.\n
    :param num_inches: Total number of inches specified.
    :param major_length: The length of the tick designating a whole inch.
    """
    draw_line(major_length, "0") 						# Draw inch 0 line.
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)  				# Draw interior ticks for inch.
        draw_line(major_length, str(j))  				# Draw inch j line and label.


def binary_search(data, target, low, high):  			# Binary search
    """Return ``True`` if target is found in indicated portion of a Python ``list``.\n
    The search only considers the portion from ``data[low]`` to ``data[high]`` inclusive.
    """
    if low > high:
        return False  									# Interval is empty; no match.
    else:
        mid = (low + high) // 2
        if target == data[mid]:  						# If a match is found.
            return True
        elif target < data[mid]:  						# Recur on the portion left of the middle.
            return binary_search(
                data, target, low, mid - 1)
        else:  											# Recur on the portion right of the middle.
            return binary_search(
                data, target, mid + 1, high)


def disk_usage(path):  									# File system
    """Return the number of bytes used by a file/folder and any descendants."""
    total = os.path.getsize(path)  						# Account for direct usage.
    if os.path.isdir(path):  							# If this is a directory (super-folder?)...
        for filename in os.listdir(path):  				# then for each child...
            childpath = os.path.join(path, filename)    # compose full path to child.
            total += disk_usage(childpath)  			# Add child's usage to total.

    print("{0:<7}".format(total), path)  				# Descriptive output (optional).
    return total


def bad_fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)
