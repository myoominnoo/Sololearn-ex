'''You and your friends are going to Europe! You have made plans to travel around Europe with your friends, but one thing you need to take into account so that everything goes according to play, is that the format of their date is different than from what is used in the United States. Your job is to convert all your dates from MM/DD/YYYY to DD/MM/YYYY.

Task: 
Create a function that takes in a string containing a date that is in US format, and return a string of the same date converted to EU.

Input Format: 
A string that contains a date formatting 11/19/2019 or November 19, 2019.

Output Format: 
A string of the same date but in a different format: 19/11/2019.

Sample Input: 
7/26/2019

Sample Output: 
26/7/2019


Note, that the input can be in two different formats, 11/19/2019 or November 19, 2019.
'''


month =  {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
us_date = input()
if("/" in us_date):
 date = us_date.split('/')
 date[0],date[1] = date[1],date[0]
 print(date[0]+'/'+date[1]+'/'+date[2])
 
else:
 for i in range(1,13):
  if(month[i] in us_date):
   date = us_date.split(' ')
   mon = date[1].split(',')
   print(mon[0]+ '/' + str(i)+ '/' + date[2])