"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martin Prchal
email: prchalmartin2@gmail.com
"""

# Začátek kódu

SEPARATOR = "-" * 60

USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

TEXTS = [
    (
        'Situated about 10 miles west of Kemmerer, Fossil Butte is a '
        'ruggedly impressive topographic feature that rises sharply '
        'some 1000 feet above Twin Creek Valley to an elevation of '
        'more than 7500 feet above sea level. The butte is located '
        'just north of U.S. 30N and the Union Pacific Railroad, '
        'which traverse the valley.'
    ),
    (
        'At the base of Fossil Butte are the bright red, purple, yellow '
        'and gray beds of the Wasatch Formation. Eroded portions of '
        'these horizontal beds slope gradually upward from the valley '
        'floor and steepen abruptly. Overlying them and extending to '
        'the top of the butte are the much steeper buff-to-white beds '
        'of the Green River Formation, which are about 300 feet thick.'
    ),
    (
        'The monument contains 8198 acres and protects a portion of '
        'the largest deposit of freshwater fish fossils in the world. '
        'The richest fossil fish deposits are found in multiple '
        'limestone layers, which lie some 100 feet below the top of '
        'the butte. The fossils represent several varieties of perch, '
        'as well as other freshwater genera and herring similar to '
        'those in modern oceans. Other fish such as paddlefish, '
        'garpike and stingray are also present.'
    ),
]

# Login
username = input("username:")
password = input("password:")

# Verification of empty entries
if username == "" or password == "" or username not in USERS or \
   USERS[username] != password:
    print("Unregistered user, terminating the program.")
    exit()

print(SEPARATOR)
print(f"Welcome to the app, {username}")
print(f"We have {len(TEXTS)} texts to be analyzed.")
print(SEPARATOR)

choice = input("Enter a number btw. 1 and 3 to select: ")
if not choice.isdigit():
    print("The selection is not a number, terminating the program.")
    exit()

index = int(choice)
if index < 1 or index > len(TEXTS):
    print("The selected number is out of range, terminating the program.")
    exit()

text = TEXTS[index - 1]

# Getting a list of words from the text
punctuation = '.,;:!?()"\''
raw_words = text.split()
words = []

for word in raw_words:
    clean_word = word.strip(punctuation)
    clean_word = clean_word.replace(".", "").replace(",", "")

    if clean_word and clean_word[0].isdigit():
        while len(clean_word) > 0 and not clean_word[-1].isdigit():
            clean_word = clean_word[:-1]

    if clean_word:
        words.append(clean_word)

# Statistics
words_total = len(words)

titlecase = 0
uppercase = 0
lowercase = 0
numbers_cnt = 0
numbers_sum = 0

for t in words:
    if t[:1].isupper() and t[1:].islower():
        titlecase += 1
    if t.isupper():
        uppercase += 1
    if t.islower():
        lowercase += 1
    if t.isdigit():
        numbers_cnt += 1
        numbers_sum += int(t)

print(SEPARATOR)
print(f"There are {words_total} words in the selected text.")
print(f"There are {titlecase} titlecase words.")
print(f"There are {uppercase} uppercase words.")
print(f"There are {lowercase} lowercase words.")
print(f"There are {numbers_cnt} numeric strings.")
print(f"The sum of all the numbers {numbers_sum}")
print(SEPARATOR)

# Lens histogram
lengths = {}
for t in words:
    length = len(t)
    if length not in lengths:
        lengths[length] = 0
    lengths[length] += 1

print("LEN|  OCCURRENCES  |NR.")
print(SEPARATOR)
for length in sorted(lengths):
    count = lengths[length]
    stars = "*" * count
    print(f"{length:>3} | {stars:<20} | {count}")
