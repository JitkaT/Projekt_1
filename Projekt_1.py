"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jitka Tichá

email: jitka.ticha@gmail.com

discord: jitkaticha

"""
user_name = input("Your username: ")
password = input("Your password: ")
separator = "-"*40
print(separator)
registred_usernames = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
if user_name in registred_usernames and registred_usernames[user_name] == password:
    print(f"Welcome to the app {user_name}!\nWe have 3 texts to be analyzed.")
    print(separator)
    texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
    ]
    text_choice_for_user = input("Enter a number btw. 1 and 3 to select: ")
    print(separator)
    if not text_choice_for_user.isnumeric():
        print("The value is not a number, program needs to finish")
    elif int(text_choice_for_user) in range (1,4):
        text_choice_nr = texts[int(text_choice_for_user) - 1]
        words = text_choice_nr.split()
        print (f"There are {len(words)} words in the selected text.")
        uppercase_words = list()
        titlecase_words = list()
        lowercase_words = list()
        digit_words = list()
        for word in words:
            if word.istitle() and word.isalpha():
                titlecase_words.append(word)         
            if word.isupper() and word.isalpha():
                uppercase_words.append(word)
            if word.islower() and word.isalpha():
                lowercase_words.append(word)
            if word.isdigit():
                digit_words.append(word)
        sum_of_digit_words = sum(int(word) for word in words if word.isnumeric())             
        print (f"There are {len(titlecase_words)} titlecase words.")          
        print (f"There are {len(uppercase_words)} uppercase words.")          
        print(f"There are {len(lowercase_words)} lowercase words.")
        print(f"There are {len(digit_words)} numeric strings.")
        print(f"The sum of all the numbers {sum_of_digit_words}.")
    else:
        print("It is not a number btw 1 and 3, the program needs to end.")
    print(separator)
    print("LEN|","OCCURENCES".center(30),"|NR.")
    print(separator)
    lenght_of_words = [len(word) for word in words]
    sorted_length_words = sorted(lenght_of_words)
    presence = {}
    for lenght in sorted_length_words:
        if lenght in presence:
            presence[lenght] += 1
        else: 
            presence[lenght] = 1
    for lenght, value in presence.items():
        alignment_1 = str(lenght).rjust(2)
        alignment_2 = "*" * value
        alignment_3 = str(alignment_2).ljust(30)
        print(alignment_1, "|", alignment_3, "|", value)
else:
    print("unregistered user, terminating the program..")







