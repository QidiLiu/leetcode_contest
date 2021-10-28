"""
A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.

A token is a valid word if all three of the following are true:

It only contains lowercase letters, hyphens, and/or punctuation (no digits).
There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
There is at most one punctuation mark. If present, it must be at the end of the token ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".

Given a string sentence, return the number of valid words in sentence.

 

Example 1:

Input: sentence = "cat and  dog"
Output: 3
Explanation: The valid words in the sentence are "cat", "and", and "dog".
Example 2:

Input: sentence = "!this  1-s b8d!"
Output: 0
Explanation: There are no valid words in the sentence.
"!this" is invalid because it starts with a punctuation mark.
"1-s" and "b8d" are invalid because they contain digits.
Example 3:

Input: sentence = "alice and  bob are playing stone-game10"
Output: 5
Explanation: The valid words in the sentence are "alice", "and", "bob", "are", and "playing".
"stone-game10" is invalid because it contains digits.
Example 4:

Input: sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
Output: 6
Explanation: The valid words in the sentence are "he", "bought", "pencils,", "erasers,", "and", and "pencil-sharpener.".
 

Constraints:

1 <= sentence.length <= 1000
sentence only contains lowercase English letters, digits, ' ', '-', '!', '.', and ','.
There will be at least 1 token.
"""

def countValidWords(self, sentence: str) -> int:
    word_sum = 0
    character_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-']
    spliter = [',', '.', '!', '?']
    spliter2 = spliter+['-']
    words = sentence.split(' ')
    for word in words:
        is_word = True
        num_minus = 0
        num_mark = 0
        if len(word)==0:
            is_word = False
            continue
        elif word == '-':
            is_word = False
            continue
        for i in range(len(word)):
            if word[i] == '-':
                num_minus += 1
                if i == 0 or i == len(word)-1:
                    is_word = False
                    continue
                elif word[i+1] not in character_list:
                    is_word = False
                    continue
            if (word[i] not in character_list and word[i] not in spliter) or (word[i] in spliter and i != len(word)-1) or num_minus>1:
                is_word = False
                continue
        if is_word:
            word_sum += 1
            print(word)
            continue
    return word_sum


"""
An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.

Given an integer n, return the smallest numerically balanced number strictly greater than n.

 

Example 1:

Input: n = 1
Output: 22
Explanation: 
22 is numerically balanced since:
- The digit 2 occurs 2 times. 
It is also the smallest numerically balanced number strictly greater than 1.
Example 2:

Input: n = 1000
Output: 1333
Explanation: 
1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times. 
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.
Example 3:

Input: n = 3000
Output: 3133
Explanation: 
3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000.
 

Constraints:

0 <= n <= 1e6
"""


def nextBeautifulNumber(n: int) -> int:
    test = 0
    while test <= 1e9:
        if test <= n:
            test += 1
            continue
        else:
            num_list = list(str(test))
            if '0' in num_list:
                test += 1
                continue
            elif ('1' in num_list and num_list.count('1') != 1) or ('2' in num_list and num_list.count('2') != 2) or ('3' in num_list and num_list.count('3') != 3) or ('4' in num_list and num_list.count('4') != 4) or ('5' in num_list and num_list.count('5') != 5) or ('6' in num_list and num_list.count('6') != 6) or ('7' in num_list and num_list.count('7') != 7) or ('8' in num_list and num_list.count('8') != 8) or ('9' in num_list and num_list.count('9') != 9):
                test += 1
                continue
            else:
                return test

print(nextBeautifulNumber(74601))