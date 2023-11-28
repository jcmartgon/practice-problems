# Jesus Carlos Martinez Gonzalez
# 28/11/2023
# Is it a vowel or consonant (https://www.codechef.com/problems/VOWELTB)

"""
Write a program to take a character (C) as input and check whether the given character is a vowel or a
consonant.
NOTE : — Vowels are 'A', 'O'. 'U. Rest all alphabets are called consonants.
"""


vowels = ["a", "e", "i", "o", "u"]

print("Vowel" if input().lower() in vowels else "Consonant")
