"""In this mission you should check if all elements in the given list are equal.
Input: List.
Output: Bool."""


def elements_equals(some_list: list) -> bool:
    if some_list:
        return True if some_list.count(some_list[0]) == len(some_list) else False
    return True


"""The password will be considered strong enough if its length is 
greater than or equal to 10 symbols, it has at least one digit, as well as containing one uppercase letter and one 
lowercase letter in it. The password contains only ASCII latin letters or digits.
Input: A password as a string.
Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean."""


def secure_password(data: str) -> bool:
    import re
    return True if len(data) >= 10 and re.search("[a-z]+", data) and re.search("[A-Z]+", data) and re.search("[0-9]+", data) else False


"""You are given a sequence of strings. You should join these strings into chunk of text where the initial strings are
separated by commas. You should replace all cases of the words "right" with the word "left", even if it's a part of 
another word. All strings are given in lowercase.
Input: A sequence of strings as a tuple of strings (unicode).
Output: The text as a string."""


def left_join(phrases: tuple) -> str:
    return ','.join([i.replace('right', 'left') for i in phrases])


"""You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters. 
You should check if the string contains three words in succession. For example, the string "start 5 one two three 7 end"
contains three words in succession.
Input: A string with words.
Output: The answer as a boolean."""


def words_count(words: str) -> bool:
    res = words.split()
    count = 0
    for i in res:
        if i.isalpha():
            count += 1
        else:
            if count < 3:
                count = 0
    return True if count >= 3 else False


"""Find the TOP most expensive goods. The amount we are looking for will be given as a first argument and the whole
data as the second one
Input: int and list of dicts. Each dicts has two keys "name" and "price"
Output: the same as the second Input argument."""


def bigger_price(limit: int, data: list) -> list:
    return list(reversed(sorted(data, key=lambda x: x.get('price'))[-limit:]))


"""
Input: An array of numbers , a tuple..
Output: The list or tuple (but not a generator) sorted by absolute values in ascending order."""


def abs_sort(numbers_array: tuple) -> list:
    return sorted(numbers_array, key=lambda x: abs(x))


"""At the input of your function are given 2 arguments: the text and the array of words the popularity of which you 
need to determine. The words should be sought in all registers.
Input: The text and the search words array.
Output: The dictionary where the search words are the keys and values are the number of times when those words 
are occurring in a given text."""


def popular_words(text: str, words: list) -> dict:
    res = text.lower().split()
    return {wrd: res.count(wrd) for wrd in words}


"""Given a list of numbers, you should find the sum of these numbers. Your solution should not contain any of the 
banned words, even as a part of another word.
The list of banned words are as follows:
sum
import
for
while
reduce
Input: A list of numbers.
Output: The sum of numbers."""


def restricted_sum(data):
    return data[0] + restricted_sum(data[1:]) if data else 0


"""You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the
 on-unique elements in this list. To do so you will need to remove all unique elements 
(elements which are contained in a given list only once). When solving this task, do not change the order of the list.
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3]"""


def non_unique_elements(data: list) -> list:
    return [elem for elem in data if data.count(elem) > 1]
