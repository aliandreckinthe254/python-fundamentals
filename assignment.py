#A program to check weather a year is a leap year

year=2008
if year%4==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")


# A program to check whether a letter is a consonant or a vowel
letter="A"
letter=letter.lower()
if letter in["a","e","i","o","u"]:
    print(letter,"is a vowel")
elif letter.isalpha():
    print(letter,"is a consonant")
else:
    print("Error!! Invalid input")
