#!/usr/bin/env python3

# Advent of Code 2023 Day 1

"""
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look.
The Elves have even given you a map;
on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by
December 25th.

Collect stars by solving puzzles.
Two puzzles will be made available on each day in the Advent calendar;
the second puzzle is unlocked when you complete the first.
Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and
where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions")
and hang on did you just say the sky ("of course, where do you think snow comes from")
when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input)
has been amended by a very young Elf who was apparently just excited to show off her art skills.
Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text;
each line originally contained a specific calibration value that the Elves now need to recover.
On each line, the calibration value can be found by combining the first digit and the last digit (in that order)
to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

"""

num_dict = {"one": '1', "two": "2", 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
                'nine': '9'}
keys = list(num_dict.keys())

def day1_prob1(file,part_2 = False):
    the_sum = 0

    with open(file) as fin:
        data = fin.readlines()
    for datum in data:
        num = ''
        for i, let in enumerate(datum):
            if let.isdigit():
                num += let
            elif part_2:
                try:
                    num += word_finder(i,datum)
                except ValueError:
                    pass
                except IndexError:
                    pass
                except KeyError:
                    pass
                except TypeError:
                    pass
        the_sum += int(num[0] + num[-1])

    return the_sum


def word_finder(i, datum):
    word = "".join(datum[i:i + 3])
    if word in keys:
        return num_dict[word]
    elif datum[i + 2].isdigit():
        raise ValueError()
    elif word + datum[i + 3] in keys:
        return num_dict[word + datum[i + 3]]

    elif datum[i + 4].isdigit():
        raise ValueError()
    elif word + "".join(datum[i + 3:i + 5]) in keys:
        return num_dict[word + "".join(datum[i + 3:i + 5])]

print(f'Part 1 answer: {day1_prob1("Day1_1.txt")}')
print(f'Part 2 answer: {day1_prob1("Day1_1.txt",True)}')
