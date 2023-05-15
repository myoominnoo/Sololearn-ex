"""
You are trying to send a secret message, and you've decided to encode it by replacing every letter in your message with its corresponding letter in a backwards version of the alphabet.
What do your messages look like?

Task:
Create a program that replaces each letter in a message with its corresponding letter in a backwards version of the English alphabet.

Input Format:
A string of your message in its normal form.

Output Format:
A string of your message once you have encoded it (all lower case).

Sample Input:
Hello World

Sample Output:
svool dliow

Explanation:
If you replace each letter in 'Hello World' with the corresponding letter in a backwards version of the alphabet, you get 'svool dliow'.
"""

x = input()
letters = 'abcdefghijklmnopqrstuvwxyz'
encoded_msg = ''

for char in x.lower():
    if char.isalpha():
        index = letters.index(char)
        encoded_char = letters[::-1][index]
        encoded_msg += encoded_char
    else:
        encoded_msg += char

print(encoded_msg)
