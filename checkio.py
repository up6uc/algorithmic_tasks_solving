"""In this mission you should check if all elements in the given list are equal.
Input: List.
Output: Bool."""


def elements_equals(some_list: list) -> bool:
    if some_list:
        return True if some_list.count(some_list[0]) == len(some_list) else False
    return True


"""Stephan and Sophia forget about security and use simple passwords for everything.
Help Nikola develop a password security check module. The password will be considered strong enough if its length is 
greater than or equal to 10 symbols, it has at least one digit, as well as containing one uppercase letter and one 
lowercase letter in it. The password contains only ASCII latin letters or digits.
Input: A password as a string.
Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean."""


def secure_password(data: str) -> bool:
    import re
    return True if len(data) >= 10 and re.search("[a-z]+", data) and re.search("[A-Z]+", data) and re.search("[0-9]+", data) else False


"""You are given a text, which contains different english letters and punctuation symbols. You should find the most 
frequent letter in the text. The letter returned must be in lower case. While checking for the most wanted letter, 
casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, 
digits and whitespaces, only letters. If you have two or more letters with the same frequency, then return the letter 
which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
Input: A text for analysis as a string.
Output: The most frequent letter in lower case as a string."""

def most_frequent_letter(data: str) -> str:
