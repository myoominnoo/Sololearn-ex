'''
Task:
Count the number of ones in the binary representation of a given integer.

Input Format:
An integer.

Output Format:
An integer representing the count of ones in the binary representation of the input.

Sample Input:
9

Sample Output:
2

Explanation:
The binary representation of 9 is 1001, which includes 2 ones.
'''

num = int(input())
count = 0
binary_num = bin(num).split()
for i in binary_num:
    if '1' in str(i):
        for j in str(i):
            if str(j) == '1':
                count += 1
print(count)