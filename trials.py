"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums

def get_odd_indices(items):
    result = []

    for idx, value in enumerate(items):
        if idx % 2 != 0:
            result.append(value)
    
    return result


def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f"{i}. {item}")
        i += 1

# items=['a', 'b']
# print_as_numbered_list(items)

def get_range(start, stop):
    nums = []

    for num in range(start, stop):
        nums.append(num)
    
    return nums


def censor_vowels(word):
    chars = []

    for letter in word:
        if letter.lower() in "aeiou":
            chars.append("*")
        else:
            chars.append(letter)

    return "".join(chars)


def snake_to_camel(string):
    camel_case = []
    string = string.split("_")
    for word in string:
        camel_case.append(f"{word[0].upper()}{word[1:]}")
    print("".join(camel_case))

    return "".join(camel_case)

snake_to_camel("snake_camel")

def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest

def truncate(string):
    result = []
    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)
   
    return "".join(result)


def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
        if parens < 0:
            return False

    return parens == 0


def compress(string):
    compressed = []
    curr_char = ""
    char_count = 0

    for char in string:
        if char != curr_char:
            compressed.append(curr_char)
            if char_count > 1:
                compressed.append(str(char_count))
            
            curr_char = char
            char_count = 0

        char_count += 1
    
    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return "".join(compressed)

print(compress('Hello, world! Cows go moooo...'))
    