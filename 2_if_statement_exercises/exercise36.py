## Exercise 36: Vowel or Consonant

letter = input("Enter a letter of the alphabet: ")
vowels = ['a', 'e', 'i', 'o', 'u']

if letter in vowels:
    print(f"{letter} is a vowel.")
elif letter == 'y':
    print(f"{letter} is sometimes a vowel... and sometimes a consonant.")
else:
    print(f"{letter} is a consonant.")