#A program to check weather a year is a leap year

year=2004
if year%4==0:
    print("leap year")
else:
    print("unleap")


# A program to check whether a letter is a consonant or a vowel
letter="u"
letter=letter.lower()
if letter in["a","e","i","o","u"]:
    print(letter,"is a vowel")
elif letter.isalpha():
    print(letter,"is a consonant")
else:
    print("Error!! Invalid input")
