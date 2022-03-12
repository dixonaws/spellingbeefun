import re

def sortkey(n):
    return len(n)

file_words = open('dictionaries/clean_wordlist.txt', 'r')

lst_words = file_words.read().splitlines()
file_words.close()

print("Loaded " + str(len(lst_words)) + " possible solutions (lst_words)")

file_letters = open('letters.txt', 'r')
lst_letters = file_letters.read().splitlines()
file_letters.close()

lst_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

str_required_letter = lst_letters[0]

# remove the required letter from the list
lst_letters.remove(str_required_letter)

# create a list of allowable letters
lst_allowable_letters = []
for letter in lst_alphabet:
    if letter in lst_letters: lst_allowable_letters.append(letter)

print("Required letter: " + str_required_letter)
print("Allowable letters: " + str(lst_allowable_letters))

print("Searching words for candidates that include the letter: " + str_required_letter + "... ")

# create a list of words that contain the required letter
lst_req_letter_words = []
for str_word in lst_words:
    if str_required_letter in str_word:
        lst_req_letter_words.append(str_word)

print("There are " + str(len(lst_req_letter_words)) + " possible solutions which contain the required letter")
lst_solutions = []

# create a regular expression that searches for words that contain the inverse of the allowable letters
# str_re_expression="^((?!b|d|f|g|h|i|j|k|l|z|x|y|w|o|v|u|r|s).)*$"
lst_inverse_allowable = lst_alphabet
for letter in lst_allowable_letters:
    lst_alphabet.remove(letter)

lst_inverse_allowable.remove(str_required_letter)

# str_re_expression = "^((?!" + str_required_letter + "|"
str_re_expression = "^((?!"
for letter in lst_inverse_allowable:
    str_re_expression += letter + "|"

# remove the last '|' character
lst_re_expression = str_re_expression.rsplit(("|"), 1)
str_re_expression = lst_re_expression[0]

str_re_expression += ").)*$"

print("str_re_expression: " + str_re_expression)

for str_word in lst_req_letter_words:
    # search for words that do not contain the letters
    x = re.search(str_re_expression, str_word)
    # x = re.search("^((?!a|b|c|f|g|h|i|j|k|l|m|q|r|s|t|v|w|y|z).)*$", str_word)

    try:
        str_possible_solution = x.string
        str_possible_solution = str_possible_solution.rstrip()

        # limit the solution to greater than 3 letters
        if len(str_possible_solution) >= 4 and str_possible_solution not in lst_solutions:
            lst_solutions.append(str_possible_solution)

    except AttributeError:
        pass

# print(lst_m_words)
print("Found " + str(len(lst_solutions)) + " possible solutions")

# sort the list with the longest solutions appearing first
lst_solutions.sort(key=sortkey, reverse=True)

for solution in lst_solutions:
    print(solution)
