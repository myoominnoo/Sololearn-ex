'''
You are trying to determine which of two apartments has a larger balcony. Both balconies are rectangles, and you have the length and width, but you need the area.

Task 
Evaluate the area of two different balconies and determine which one is bigger.

Input Format 
Your inputs are two strings where the measurements for height and width are separated by a comma. The first one represents apartment A, the second represents apartment B.

Output Format: 
A string that says whether apartment A or apartment B has a larger balcony.

Sample Input 
'5,5'
'2,10'

Sample Output 
Apartment A

Explanation 
Since the area of apartment A's balcony is 25 and the area of apartment B's balcony is 20, Apartment A is the correct answer.
'''

apartment_A = input().split(',')
apartment_B = input().split(',')
apartment_A = list(apartment_A)
apartment_B = list(apartment_B)

area_A = int(apartment_A[0]) * int(apartment_A[1])
area_B = int(apartment_B[0]) * int(apartment_B[1])

if area_A > area_B:
    print('Apartment A')
else:
    print('Apartment B')